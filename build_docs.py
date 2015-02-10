#
# build_docs.py
# LittleHedgehogDocs
#
# Created by James Barrow on 10/02/2015.
# Copyright (c) 2015 James Barrow - Pig on a Hill Productions. All rights reserved.
#

#!/usr/bin/env python

import json
from bs4 import BeautifulSoup

def parseSourceKitten(sourcekitten_JSON):
  for file_JSON in sourcekitten_JSON:
    parseFile(file_JSON)

def parseFile(file_JSON):
  file_structure = file_JSON['key.substructure']
  for page in file_structure:
    parseStructure(page)

def parseStructure(page):
  structure_name = page['key.name']
  structure_doc = None

  try:
    structure_doc = parseDocumentationComment(page['key.doc.full_as_xml'])
  except Exception, e:
    pass

  if structure_doc != None and structure_name != None:
    print "%s - %s" %(structure_name, structure_doc)
  else:
    print "%s" %(structure_name)

  try:
    parseSubstructure(page['key.substructure'])
  except Exception, e:
    pass

def parseSubstructure(file_substructure):
  for substructure in file_substructure:
    substructure_name = substructure['key.name']
    substructure_doc = None

    try:
      substructure_doc = parseDocumentationComment(substructure['key.doc.full_as_xml'])
    except Exception, e:
      pass

    if substructure_doc != None and substructure_name != None:
      print "  %s - %s" %(substructure_name, substructure_doc)
    else:
      print "  %s" %(substructure_name)

def parseDocumentationComment(doc_comment):
  doc = None
  try:
    soup = BeautifulSoup(doc_comment)
    doc = soup.para.get_text()
  except Exception, e:
    pass
  return doc
