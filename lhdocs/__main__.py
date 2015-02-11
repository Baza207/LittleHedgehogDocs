#
# mian.py
# LittleHedgehogDocs
#
# Created by James Barrow on 09/02/2015.
# Copyright (c) 2015 James Barrow - Pig on a Hill Productions.
# All rights reserved.
#

#!/usr/bin/env python

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
        help='The Xcode project to parse.'
    )
    parser.add_argument(
        '-scheme',
        dest='scheme',
        help='The Xcode scheme to parse.'
    )
    parser.add_argument(
        '-output',
        dest='output',
        default='~/',
        help='The output file.'
    )

    args = parser.parse_args()
    subprocess.call('clear')

    print "\n---------------------------------------------------\n"

    print "Welcome to Little Hedgehog Docs"

    print "\n---------------------------------------------------\n"

    print "Runnig SourceKitten..."
    sourcekitten_result = subprocess.check_output([
        'sourcekitten',
        'doc',
        '-project',
        args.project,
        '-scheme',
        args.scheme
    ])
    sourcekitten_JSON = json.loads(sourcekitten_result)

    print "Building docs..."
    pages = build_docs.build_sourcekitten(sourcekitten_JSON)

    print "Saving docs..."
    save_docs.save_pages(pages, args.output, args.scheme)

    print "\n---------------------------------------------------\n"

    print "Complete! Have a nice day. :)"

    print "\n---------------------------------------------------\n"

    sys.exit()

if __name__ == '__main__':
    main()
