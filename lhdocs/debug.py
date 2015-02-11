import json


def printJSON(string):
    print json.dumps(
        string,
        sort_keys=True,
        indent=2,
        separators=(',', ': ')
    )
