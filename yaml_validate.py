#!/usr/bin/env python

"""This module will iterate through all direct subdirectories and process as follows:
- validate "./{subdir}/template.yaml" against the schema in "./_schema/template.json"
- validate "./{subdir}/config.yaml" against the schema in "./_schema/config.json"
- validate "./{subdir}/signing/template.yaml" against the schema in "./_schema/signing/template.json"
"""

import glob
from jsonschema import validate
import yaml
import json


def yaml_validate_file(schema_path, yaml_path):
    print("validating {} with {}".format(yaml_path, schema_path))
    with open(schema_path, 'r') as s:
        schema = json.load(s)

    with open(yaml_path, 'r') as y:
        yaml_file = yaml.safe_load(y)

    return validate(instance=yaml_file, schema=schema)


consent_dirs = [x for x in glob.glob('*/') if not x.startswith('_')]
yaml_file_locations = ['template', 'config', 'signing/template']

for i in consent_dirs:
    print("processing consent dir {}".format(i))
    for j in yaml_file_locations:
        yaml_validate_file("./_schema/{}.json".format(j), "./{}{}.yaml".format(i, j))
