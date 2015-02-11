#
# save_docs.py
# LittleHedgehogDocs
#
# Created by James Barrow on 10/02/2015.
# Copyright (c) 2015 James Barrow - Pig on a Hill Productions.
# All rights reserved.
#

#!/usr/bin/env python

import os


def save_pages(pages, filepath, name):
    output_filepath = create_root_dir(filepath, name)

    for (name, page) in pages:
        save_page(output_filepath, name, page)


def create_root_dir(filepath, name):
    if name is None:
        name = 'Docs'
    output_filepath = os.path.join(filepath, name)
    try:
        os.makedirs(output_filepath)
    except:
        pass
    return output_filepath


def save_page(filepath, name, page):
    filename = '%s.md' % (name)
    output_filepath = os.path.join(filepath, filename)
    obj = open(output_filepath, 'w+b')
    obj.write(page.encode('UTF-8'))
    obj.close
