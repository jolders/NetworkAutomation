#! /usr/bin/python3
# Get information from a JSON / XML / YML 
# read a file from different file types and output the result.

import json
import yaml
import xmltodict

json_path = "db.json"
yml_path = "db.yml"
xml_path = "db.xml"

# json output
print('---- json output ----')
with open(json_path) as f:
    import json
    data = json.load(f) 
    print(data)

# yml
# pip install pyyaml
print('---- yml output ----')
with open(yml_path) as f:
    data = yaml.safe_load(f) 
    print(data)

# xml
# pip install xmltodict
print('---- xml output ----')
with open(xml_path) as f:
    data = xmltodict.parse(f.read())["root"]
    print(data)
