from json import loads


def to_dict(string: str) -> dict:
    """This function helps convert from string to dict"""
    if type(string) != int:
        myJson = loads(string)

        return myJson
