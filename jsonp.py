#!/usr/bin/env python
# By Sanix Darker

from json import loads as jsonloads
from argparse import ArgumentParser

# To test it, run:
# python jsonp.py -s "{\"key\":\"value\"}" -k key

# Initialize the arguments
prs = ArgumentParser()
prs.add_argument('-f', '--file', help='The file containing the JSON-STRING', type=str, default=None)
prs.add_argument('-s', '--string', help='The Complete JSON-STRING', type=str, default=None)
prs.add_argument('-k', '--key', help='The key of the JSON object you want', type=str, required=True)
prs = prs.parse_args()

try:
    objJson = {}
    if prs.file is None:
        objJson = jsonloads(prs.string)
    else:
        with open(prs.file, "r+") as fil:
            objJson = jsonloads(fil.read())

    objJson = {x.replace(' ', ''): v
                    for x, v in objJson.items()}
    print(objJson[prs.key])
except Exception as es:pass
