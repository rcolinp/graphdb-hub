# National Cancer Institute Thesaurus & Neosemantics (N10s)

## Objective

__Utilizing the python module rdflib, create an serialize the National Cancer Institute Thesaurus's monthly flat file release as an RDF Graph and  (located -> `https://evs.nci.nih.gov/ftp1/NCI_Thesaurus/Thesaurus.FLAT.zip`) to take the National Cancer Institues raw monthly release (flat text file format), create an RDF serialization of the data and map the RDF graph to Neo4j's Label Property Graph using Neosemantics.__

- Refer to `src/nci_thesaurus_to_rdf.py` for python script that outputs the RDF graph (`ncit.ttl`)
- For those who want to access the data directly with Cypher etc & not mess with python:
  - The input zipped input .txt file can be found via following relative directory `data/Thesaurus.FLAT.zip`
  - The turtle (.ttl) serialization of NCI Thesaurus can be found in the following relative directory `data/ncit.ttl.gz` 
for those who want to access the data directly with Cypher etc.

The RDF graph will be mapped to Neo4j's Label Property Graph using Neosemantics (n10s) plugin!

![MapNs_MapDef](https://raw.githubusercontent.com/rcolinp/graphdb-hub/main/graphdb_hub/national_cancer_institute_n10s/images/_MapNs_MapDef.png)

__S/P import:__

![MapNs_MapDef](https://raw.githubusercontent.com/rcolinp/graphdb-hub/main/graphdb_hub/national_cancer_institute_n10s/images/nodes_rels_props.png)
