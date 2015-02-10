#
# save_docs.py
# LittleHedgehogDocs
#
# Created by James Barrow on 10/02/2015.
# Copyright (c) 2015 James Barrow - Pig on a Hill Productions. All rights reserved.
#

#!/usr/bin/env python

import os, errno

def save_pages(pages, filepath, name):
  output_filepath = create_root_dir(filepath, name)

  for (name, page) in pages:
    save_page(output_filepath, name, page)

def create_root_dir(filepath, name):
  if name == None:
    name = 'Docs'
  output_filepath = os.path.join(filepath, name)
  try:
    os.makedirs(output_filepath)
  except OSError as exception:
    pass
    # print exception
  return output_filepath

def save_page(filepath, name, page):
  filename = '%s.mb' %(name)
  output_filepath = os.path.join(filepath, filename)
  obj = open(output_filepath, 'w+b')
  obj.write(page)
  obj.close
