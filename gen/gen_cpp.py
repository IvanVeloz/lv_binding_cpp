#!/usr/bin/env python3

# SPDX-License-Identifier: MIT
# Copyright (C) 2025 Ivan Veloz, 2021 LVGL

import sys

from sys import argv
from argparse import ArgumentParser
from os.path import dirname, abspath, commonprefix

script_path = dirname(abspath(__file__))
sys.path.insert(0, '%s/../pycparser' % script_path)
from pycparser import c_parser, c_ast, c_generator

#
# Argument parsing
#
argParser = ArgumentParser()
argParser.add_argument('-I', '--include', dest='include', help='Preprocesor include path', metavar='<Include Path>', action='append')
argParser.add_argument('-D', '--define', dest='define', help='Define preprocessor macro', metavar='<Macro Name>', action='append')
argParser.add_argument('-E', '--external-preprocessing', dest='ep', help='Prevent preprocessing. Assume input file is already preprocessed', metavar='<Preprocessed File>', action='store')
argParser.add_argument('-J', '--lvgl-json', dest='json', help='Provde a JSON from the LVGL JSON generator for missing information', metavar='<JSON file>', action='store')
argParser.add_argument('-M', '--module_name', dest='module_name', help='Module name', metavar='<Module name string>', action='store')
argParser.add_argument('-MP', '--module_prefix', dest='module_prefix', help='Module prefix that starts every function name', metavar='<Prefix string>', action='store')
argParser.add_argument('-MD', '--metadata', dest='metadata', help='Optional file to emit metadata (introspection)', metavar='<MetaData File Name>', action='store')
argParser.add_argument('input', nargs='+')
argParser.set_defaults(include=[], define=[], ep=None, json=None, input=[])
args = argParser.parse_args()

module_name = args.module_name
module_prefix = args.module_prefix if args.module_prefix else args.module_name

def main():
    if not args.input:
        print("No input files provided.")
        sys.exit(1)
    else:
        print("Input files: %s" % args.input)


if __name__ == "__main__":
    main()
