def serializeDict(a) -> dict:
    if a is None:
        return None

    return {
        **{i: str(a[i]) for i in a if i == "_id"},
        **{i: a[i] for i in a if i != "_id"},
    }


def serializeList(a) -> list:
    return [serializeDict(i) for i in a]
