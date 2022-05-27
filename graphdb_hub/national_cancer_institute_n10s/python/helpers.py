from namespaces import NAMESPACES


def curie_to_uri(curie: str, curie_map=NAMESPACES) -> str:
    if ":" not in curie:
        return curie
    [prefix, local_id] = curie.split(":", 1)
    if prefix.upper() in curie_map:
        return curie_map[prefix.upper()] + local_id
    return curie
