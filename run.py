#!/usr/bin/env python3

import os
import json

results = {"errors": [], "warnings": []}

with open('config.json') as config_f:
    config = json.load(config_f)
    ashs_dir = config["ashs"]

if not os.listdir(ashs_dir):
    results['errors'].append("Output directory is empty")

#bypass output
if not os.path.exists("output"):
    os.mkdir("output")
if os.path.lexists("output/ashs"):
    os.remove("output/ashs")
os.symlink("../"+ashs_dir, "output/ashs")

#copy qa directory frmo ashs
if not os.path.exists("secondary"):
    os.mkdir("secondary")
if os.path.lexists("secondary/qa"):
    os.remove("secondary/qa")
os.symlink("../"+ashs_dir+"/qa", "secondary/qa")

