from io import BytesIO
from zipfile import ZipFile
from rdflib import Graph, Literal, URIRef, DC, RDF, RDFS, SKOS
from urllib.request import urlopen
from namespaces import NAMESPACES, NCIT, SH
from helpers import curie_to_uri


class NciThesaurusTxtToRDF:
    def __init__(self, url):
        resp = urlopen(url)
        self.zipfile = ZipFile(BytesIO(resp.read()))
        self.graph = Graph()
        self.graph.namespace_manager.bind("dc", DC)
        self.graph.namespace_manager.bind("ncit", NCIT)
        self.graph.namespace_manager.bind("sh", SH)
        self.graph.namespace_manager.bind("skos", SKOS)
        self.graph.namespace_manager.bind("rdf", RDF)
        self.graph.namespace_manager.bind("rdfs", RDFS)

    def convert_to_rdf(self, see_also=""):
        cs_uri = URIRef("http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl")
        self.graph.add((cs_uri, RDF.type, SKOS.ConceptScheme))
        self.graph.add((cs_uri, DC.description, Literal("Ontology for NCI Thesaurus")))
        self.graph.add(
            (
                cs_uri,
                RDFS.seeAlso,
                Literal("https://ncithesaurus.nci.nih.gov/ncitbrowser/"),
            )
        )
        self.graph.add(
            (
                cs_uri,
                SH.namespace,
                URIRef("http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#"),
            )
        )

        for line in self.zipfile.open("Thesaurus.txt"):
            tokens = line.decode("utf-8").split("\t")
            uri = URIRef(tokens[1][1:-1])
            self.graph.add((uri, RDF.type, SKOS.Concept))
            self.graph.add((uri, SKOS.notation, Literal(tokens[0])))
            self.graph.add((uri, SKOS.prefLabel, Literal(tokens[3].split("|")[0])))
            self.graph.add((uri, SKOS.definition, Literal(tokens[4])))
            if tokens[2]:
                for code in tokens[2].split("|"):
                    code = code.strip()
                    sc_uri = URIRef(curie_to_uri(f"NCIT:{code}", NAMESPACES))
                    self.graph.add((uri, SKOS.broader, sc_uri))
            see_also = f"https://ncit.nci.nih.gov/ncitbrowser/pages/concept_details.jsf?dictionary=NCI%20Thesaurus&code={tokens[0]}"
            self.graph.add((uri, RDFS.seeAlso, Literal(see_also)))
            self.graph.add((uri, SKOS.inScheme, cs_uri))
        with open("ncit_skos.ttl", "w") as file:
            file.write(self.graph.serialize(format="turtle")).decode("utf-8")


if __name__ == "__main__":
    ncit_loader = NciThesaurusTxtToRDF(
        "https://evs.nci.nih.gov/ftp1/NCI_Thesaurus/Thesaurus.FLAT.zip"
    )
    ncit_loader.convert_to_rdf()
