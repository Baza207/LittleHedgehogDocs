#
# __mian__.py
# LittleHedgehogDocs
#
# Created by James Barrow on 09/02/2015.
# Copyright (c) 2015 James Barrow - Pig on a Hill Productions.
# All rights reserved.
#

# !/usr/bin/env python

import sys
import argparse
import subprocess
import json
import build_docs
import save_docs


def main():
    parser = argparse.ArgumentParser(
        prog='LittleHedgehogDocs',
        description='Parse Swift documentation into Markdown files.'
    )
    parser.add_argument(
        '-project',
        dest='project',
        nargs='+',
        required=True,
        help='The Xcode project to parse.'
    )
    parser.add_argument(
        '-module-name',
        dest='module_name',
        nargs='+',
        required=True,
        help='The name of the module to parse.'
    )
    parser.add_argument(
        '-output',
        dest='output',
        default='~/',
        help='The output file.'
    )

    args = parser.parse_args()
    args.project = ' '.join(args.project)
    args.module_name = ' '.join(args.module_name)

    subprocess.call('clear')

    print "\n---------------------------------------------------\n"

    print "Welcome to Little Hedgehog Docs"

    print "\n---------------------------------------------------\n"

    print "Runnig SourceKitten..."
    sourcekitten_result = subprocess.check_output([
        'sourcekitten',
        'doc',
        '--module-name',
        args.module_name,
        '--',
        '-project',
        args.project
    ])
    sourcekitten_json = json.loads(sourcekitten_result)

    print "Building docs..."
    pages = build_docs.build_sourcekitten(sourcekitten_json)

    print "Saving docs to..."
    save_docs.save_pages(pages, args.output, args.module_name)

    print "\n---------------------------------------------------\n"

    print "Complete! Have a nice day. :)"

    print "\n---------------------------------------------------\n"

    sys.exit()


if __name__ == '__main__':
    main()
