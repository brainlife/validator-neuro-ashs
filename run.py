#!/usr/bin/env python3

import os
import json
from shutil import copytree

results = {"errors": [], "warnings": []}

src_dir = 'output/ashs'
sec_dir = 'secondary'

if not os.listdir(src_dir):
    results['errors'].append("Output directory is empty")

qa_dir = src_dir + '/qa'
copytree(qa_dir, sec_dir)