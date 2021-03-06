﻿#!/usr/bin/env python
# encoding: utf-8

from waflib import Utils

def configure(ctx):
    print("Configure from: " + ctx.path.abspath())

def build(ctx):
    print("Build from: " + ctx.path.abspath())

    key = ["small", "large"]

    import os
    import os.path
    import re

    abspath = ctx.path.abspath()
    lib = os.path.basename(abspath)

    for k in key:

	filter = "|".join([x for x in key if not x == k])

        src = [f for f in os.listdir(abspath) if re.match(r'.*\.c$', f) and not re.match(r'.*('+filter+').*\.c$', f)]
        print lib, k, src

        install_dir = "${DATADIR}/" +  lib

        #ctx.install_files(install_dir, ['config.tsv', 'base_output'])
        #ctx.install_files(install_dir, [f for f in os.listdir(abspath) if re.match(r'input_.*$', f)])
        #ctx.install_files(install_dir, ['check', 'progress'], chmod=Utils.O755)

        name = lib + "_" + k + ".x"

        task = ctx(features='c cprogram', target=name, source=src)
        task.install_path = install_dir
        task.chmod = Utils.O755
	


