from namespaces import NAMESPACES


def compact_uri_to_uri(compact_uri: str, compact_uri_map=NAMESPACES) -> str:
    if ":" not in compact_uri:
        return compact_uri
    [prefix, local_id] = compact_uri.split(":", 1)
    if prefix.upper() in compact_uri_map:
        return compact_uri_map[prefix.upper()] + local_id
    return compact_uri
