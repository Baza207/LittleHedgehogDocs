import json


def print_json(string):
    print json.dumps(
        string,
        sort_keys=True,
        indent=2,
        separators=(',', ': ')
    )
