// Create uniquness constraint -> guarantees the uniqueness of the of the resources by URI 
CREATE CONSTRAINT n10s_unique_uri ON (r:Resource) ASSERT r.uri IS UNIQUE;

// Create graphConfig -> Define the characteristics of the graph.
// handleVocabUris 
call n10s.graphconfig.init({ 
    handleVocabUris: 'MAP',
    handleRDFTypes: 'LABELS_AND_NODES'
});

// Defining custom prefixes for namespaces in the graph
// `addNamespacePrefixesFromText` method -> define prefixes for namespaces as explicitly defined in the .ttl serialization
WITH ' 
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix ncit: <http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> . 
' AS txt
CALL n10s.nsprefixes.addFromText(txt) YIELD prefix, namespace
RETURN prefix, namespace;

// Node types
call n10s.mapping.add('http://www.w3.org/2004/02/skos/core#Concept', 'ConceptReference');
call n10s.mapping.add('http://www.w3.org/2004/02/skos/core#ConceptScheme', 'ConceptSystem');

// Object Properties
call n10s.mapping.add('http://www.w3.org/2004/02/skos/core#broader', 'HAS_PARENT');
call n10s.mapping.add('http://www.w3.org/2004/02/skos/core#inScheme', 'DEFINED_IN');

// Data Type Properties
call n10s.mapping.add('http://www.w3.org/2004/02/skos/core#notation', 'code');
call n10s.mapping.add('http://www.w3.org/2004/02/skos/core#prefLabel', 'pref_label');
call n10s.mapping.add('http://www.w3.org/2004/02/skos/core#definition', 'definition');
call n10s.mapping.add('http://www.w3.org/2000/01/rdf-schema#seeAlso', 'reference');

// Import Turtle serialization
CALL n10s.rdf.import.fetch("file:///var/lib/neo4j/import/ncit.ttl", "Turtle")

// It can be quite common when working with manually curated taxonomies to have multi-hop hierarchical relationships represented \
// as single-hop relationships. For example, HAS_PARENT within our Neo4j Graph or <http://www.w3.org/2004/02/skos/core#broader>) \
// represented as a single hop within in manually curated taxonomies.
// To ensure that these relationships are represented as single-hop relationships, we can delete all relationships where a 2+ hop \
// relationship is represented as a single hop relationship.
MATCH (v:ConceptReference)<-[:HAS_PARENT*2..]-(child)-[shortcut:HAS_PARENT]->(v) DELETE shortcut;
// -> Deleted 40 relationships, completed after 84829 ms.




