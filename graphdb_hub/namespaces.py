from rdflib import Namespace
from rdflib.namespace import RDF, RDFS, OWL, XSD, DC, DCTERMS, SKOS

NCIT = Namespace("http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#")
SH = Namespace("http://www.w3.org/ns/shacl#")

NAMESPACES = {
    "RDF": RDF,
    "RDFS": RDFS,
    "OWL": OWL,
    "XSD": XSD,
    "DC": DC,
    "DCTERMS": DCTERMS,
    "SKOS": SKOS,
    "NCIT": NCIT,
    "SH": SH,
}