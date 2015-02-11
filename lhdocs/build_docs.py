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

def build_sourcekitten(sourcekitten_JSON):
  pages = []
  for file_JSON in sourcekitten_JSON:
    build_file(pages, file_JSON)
  return pages

def build_file(pages, file_JSON):
  file_pages = file_JSON['key.substructure']
  for page in file_pages:
    pages.append(build_page(page))

def build_page(page):
  page_name = page['key.name']
  page_content = build_class(page, page_name)
  
  try:
    sections = page['key.substructure']
    page_content += build_sections(sections)
  except Exception, e:
    pass
  page_content += build_page_footer()

  return (page_name, page_content)

def build_sections(page_sections):
  content = ''
  for section in page_sections:
    content += build_section(section)
  return content

def build_section(section):
  kind_components = section['key.kind'].split('.')
  language = kind_components[2]
  kind_type = kind_components[4]

  if kind_type in ['var', 'let']:
    return build_property(section, language)
  elif kind_type in ['function']:
    return build_function(section, language)
  elif kind_type in ['comment']:
    return build_comment(section, language, kind_components[-1])
  else:
    print "Unparsed kind: %s\n%s" %(kind_type, json.dumps(section, sort_keys=True, indent=2, separators=(',', ': ')))
    return ''

'''
# Class Name <key.name>
[Description] <key.doc.full_as_xml>.para.get_text()

'''
def build_class(page, name):
  description = ''
  try:
    description_soup = BeautifulSoup(page['key.doc.full_as_xml'])
    description = description_soup.para.get_text()
  except Exception, e:
    pass
  return '# %s\n%s\n' %(name, description)

'''
### Property Name <key.name>
[Description] <key.doc.full_as_xml>.para.get_text()

**Declaration**
> <sub>**[Language]**</sub>
> ``` <language>
[Declaration] <key.parsed_declaration>
```
---
'''
def build_property(section, language):
  name = section['key.name']
  description = build_description(section)
  declaration = section['key.parsed_declaration']
  return '<br>\n\n### %s\n%s\n\n**Declaration**\n> <sub>**%s**</sub>  \n> ```%s  \n%s\n```\n---\n\n' %(name, description, language.capitalize(), language, declaration)

'''
### Function Name <key.name>
[Description] key.doc.full_as_xml <XML>.para.get_text()

Declaration
> [Lang]
> [Declaration] key.parsed_declaration
'''
def build_function(section, language):
  name = section['key.name']
  description = build_description(section)
  declaration = section['key.parsed_declaration']
  attributes = build_attributes(section)
  return '<br>\n\n### %s\n%s\n\n**Declaration**\n> <sub>**%s**</sub>  \n> ```%s  \n%s\n```\n%s---\n\n' %(name, description, language.capitalize(), language, declaration, attributes)

'''
## MARK Name <key.name>.split(' ')[-1]
'''
def build_comment(section, language, comment_type):
  if comment_type in ('mark'):
    name = section['key.name'].split(' ')[-1]
    return '## %s\n' %(name)
  else:
    print "Unparsed comment: %s\n%s" %(comment_type, json.dumps(section, sort_keys=True, indent=2, separators=(',', ': ')))
    return ''

'''
[Description]
'''
def build_description(section):
  description = ''
  try:
    soup = BeautifulSoup(section['key.doc.full_as_xml'])
    description = soup.para.get_text()
  except Exception, e:
    pass
  return description

'''
**Parameters**
<table>
  <tr><td>[Parameter]</td><td><[Description]/td></tr>
  ...
</table>

**Return Value**
[Return Description]
'''
def build_attributes(section):
  content = ''
  try:
    soup = BeautifulSoup(section['key.doc.full_as_xml'])
    has_contents = False
    for parameter in soup.find_all('parameter'):
      has_contents = True
      content += '<tr><td> `%s` </td><td> %s </td></tr>\n' %(parameter.find('name').get_text(), parameter.para.get_text())

    if has_contents == True:
      content = '\n**Parameters**\n<table>\n' + content
      content += '<table>\n'

    return_description = soup.resultdiscussion.para.get_text()
    if return_description != None:
      content += '\n**Return Value**  \n%s\n' %(return_description)
  except Exception, e:
    pass
  return content + '\n'

'''
Built with Little Hedgehog Docs by Pig on a Hill Productions.
'''
def build_page_footer():
  return '<div class="footer" align="center"><sub>Built with <a href="https://github.com/Baza207/LittleHedgehogDocs" target="_blank">Little Hedgehog Docs</a> by <a href="mailto:james@pigonahill.com" target="_blank">James Barrow</a> - <a href="http://pigonahill.com" target="_blank">Pig on a Hill Productions</a>.</sub></div>\n'
