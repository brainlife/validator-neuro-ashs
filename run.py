#!/usr/bin/env python3

import os
import json
from shutil import copyfile

results = {"errors": [], "warnings": []}

src_dir = 'output/ashs'
sec_dir = 'secondary'

if not os.listdir(src_dir):
    results['errors'].append("Output directory is empty")

if not os.path.exists(sec_dir):
    os.mkdir(sec_dir)

qa_dir = src_dir + '/qa'
fig_left = '/qa_seg_multiatlas_corr_nogray_left_qa.png'
fig_right = '/qa_seg_multiatlas_corr_nogray_right_qa.png'

copyfile(qa_dir + fig_left, sec_dir + fig_left)
copyfile(qa_dir + fig_right, sec_dir + fig_right)