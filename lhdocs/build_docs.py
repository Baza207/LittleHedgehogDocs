#
# build_docs.py
# LittleHedgehogDocs
#
# Created by James Barrow on 10/02/2015.
# Copyright (c) 2015 James Barrow - Pig on a Hill Productions.
# All rights reserved.
#

# !/usr/bin/env python

from debug import print_json
from bs4 import BeautifulSoup
import re


def build_sourcekitten(sourcekitten_json):
    pages = []
    for file_json in sourcekitten_json:
        for key in file_json:
            file_pages = file_json[key]['key.substructure']
            for page in file_pages:
                markdown_page = build_page(page)
                if markdown_page is not None:
                    pages.append(markdown_page)
    return pages


def build_page(page):
    page_type = page['key.kind'].split('.')[-1]
    if page_type in ['class']:
        page_name = page['key.name']
        page_content = build_class(page, page_name)

        sections = None
        try:
            sections = page['key.substructure']
        except KeyError:
            pass

        page_content += build_sections(sections)
        page_content += build_page_footer()

        return (page_name, page_content)
    elif page_type in ['global', 'enum', 'extension', 'protocol', 'free']:
        return None  # TODO: Parse global page types into 1 page per type.
    elif page_type in ['mark']:
        return None  # Never make pages for comments
    else:
        print "Unparsed page type: %s\n%s\n" % (
            page_type,
            print_json(page)
        )
        return None


def build_sections(page_sections):
    content = ''
    try:
        for section in page_sections:
            content += build_section(section)
    except TypeError:
        pass
    return content


def build_section(section):
    kind_components = section['key.kind'].split('.')
    language = kind_components[2]
    kind_type = kind_components[4]

    if kind_type in ['var', 'let']:
        return build_property(section, language)
    elif kind_type in ['function']:
        return build_function(section, language)
    elif kind_type in ['struct']:
        return build_struct(section, language)
    elif kind_type in ['enum']:
        return build_enum(section, language)
    elif kind_type in ['comment']:
        return build_comment(section, language, kind_components[-1])
    else:
        print "Unparsed section kind: %s\n%s\n" % (
            kind_type,
            print_json(section)
        )
    return ''


# # Class Name <key.name>
# [Description] <key.doc.full_as_xml>.para.get_text()
def build_class(page, name):
    description = ''
    try:
        description_soup = BeautifulSoup(page['key.doc.full_as_xml'], "lxml")
        description = description_soup.para.get_text()
    except (KeyError, AttributeError):
        pass
    return '# %s\n%s\n' % (name, description)


# ### Property Name <key.name>
# [Description] <key.doc.full_as_xml>.para.get_text()
#
# **Declaration**
# > <sub>**[Language]**</sub>
# > ``` <language>
# [Declaration] <key.parsed_declaration>
# ```
# ---
def build_property(section, language):
    name = section['key.name']
    description = build_description(section)
    declaration = section['key.parsed_declaration']
    return (
        '<br>\n\n'
        '### %s\n'
        '%s\n\n'
        '**Declaration**\n'
        '> <sub>**%s**</sub>  \n'
        '> ```%s  \n'
        '%s\n'
        '```\n'
        '---\n\n') % (
        name,
        description,
        language.capitalize(),
        language.lower(),
        declaration
    )


# ### Function Name <key.name>
# [Description] <key.doc.full_as_xml>.para.get_text()
#
# **Declaration**
# > <sub>**[Language]**</sub>
# > ``` <language>
# [Declaration] <key.parsed_declaration>
# ```
# ---
def build_function(section, language):
    name = section['key.name']
    description = build_description(section)
    declaration = section['key.parsed_declaration']
    attributes = build_attributes(section)
    return (
        '<br>\n\n'
        '### %s\n'
        '%s\n\n'
        '**Declaration**\n'
        '> <sub>**%s**</sub>  \n'
        '> ```%s  \n'
        '%s\n'
        '```\n'
        '%s---\n\n') % (
        name,
        description,
        language.capitalize(),
        language.lower(),
        declaration,
        attributes
    )


# {
#     <Constant>
#     ...
# }
#
# - AND -
#
# **Constants**
# - `<Constant Declaration>`
# ...
def build_constants(section):
    constants = ''
    constants_detail = ''
    try:
        sections = section['key.substructure']
        has_contents = False
        for constant in sections:
            has_contents = True
            name = constant['key.name']
            declaration = constant['key.parsed_declaration']
            description = build_description(constant)
            constants += '    %s\n' % (declaration)
            constants_detail += '- `%s`\n%s\n' % (name, description)

        if has_contents is True:
            constants = '{\n' + constants + '}'
            constants_detail = '**Constants**\n' + constants_detail
    except KeyError:
        pass
    return (constants, constants_detail)


# ### Structure Name <key.name>
# [Description] <key.doc.full_as_xml>.para.get_text()
#
# **Declaration**
# > <sub>**[Language]**</sub>
# > ``` <language>
# [Declaration] <key.parsed_declaration> {
#     <Constant>
#     ...
# }
# ```
# **Constants**
# - `<Constant Declaration>`
# ...
# ---
def build_struct(section, language):
    name = section['key.name']
    description = build_description(section)
    declaration = section['key.parsed_declaration']
    (constants, constants_detail) = build_constants(section)
    return (
        '<br>\n\n'
        '### %s\n'
        '%s\n\n'
        '**Declaration**\n'
        '> <sub>**%s**</sub>  \n'
        '> ```%s  \n'
        '%s'
        '%s\n'
        '```\n\n'
        '%s'
        '---\n\n') % (
        name,
        description,
        language.capitalize(),
        language.lower(),
        declaration,
        constants,
        constants_detail
    )


# ### Enum Name <key.name>
# [Description] <key.doc.full_as_xml>.para.get_text()
#
# **Declaration**
# > <sub>**[Language]**</sub>
# > ``` <language>
# [Declaration] <key.parsed_declaration> {
#     <Constant>
#     ...
# }
# ```
# **Constants**
# - `<Constant Declaration>`
# ...
# ---
# FIXME: Enum constants don't seem to be provided by SourceKitten.
# It needs to be checked if they're being returned in another place
# or if it's a parsing issue with SourceKitten.
def build_enum(section, language):
    name = section['key.name']
    description = build_description(section)
    declaration = section['key.parsed_declaration']
    (constants, constants_detail) = build_constants(section)
    return (
        '<br>\n\n'
        '### %s\n'
        '%s\n\n'
        '**Declaration**\n'
        '> <sub>**%s**</sub>  \n'
        '> ```%s  \n'
        '%s'
        '%s\n'
        '```\n\n'
        '%s'
        '---\n\n'
    ) % (
        name,
        description,
        language.capitalize(),
        language.lower(),
        declaration,
        constants,
        constants_detail
    )


# ## MARK Name <key.name>.split(' ')[-1]
def build_comment(section, language, comment_type):
    if comment_type in ('mark'):
        name_components = section['key.name']
        match = re.match(
            '^MARK:\s*(?P<heading>-)?\s*(?P<name>.*)$',
            name_components
        )
        name = match.group('name')
        header = '###'
        if match.group('heading'):
            header = '##'
        return '\n<br>\n%s %s  ' % (
            header,
            name
        )
    else:
        print "Unparsed comment: %s\n%s" % (
            comment_type,
            print_json(section)
        )
    return ''


# [Description]
def build_description(section):
    description = ''
    try:
        soup = BeautifulSoup(section['key.doc.full_as_xml'], "lxml")
        description = soup.para.get_text()
    except (KeyError, AttributeError):
        pass
    return description


# **Parameters**
# <table>
#   <tr><td>[Parameter]</td><td><[Description]/td></tr>
#   ...
# </table>
#
# **Return Value**
# [Return Description]
def build_attributes(section):
    content = ''
    try:
        soup = BeautifulSoup(section['key.doc.full_as_xml'], "lxml")
        has_contents = False
        for parameter in soup.find_all('parameter'):
            has_contents = True

            name = parameter.find('name').get_text()
            description = parameter.para.get_text()
            content += '<tr><td> `%s` </td><td> %s </td></tr>\n' % (
                name,
                description
            )

        if has_contents is True:
            content = '\n**Parameters**\n<table>\n' + content
            content += '<table>\n'

        return_description = soup.resultdiscussion.para.get_text()
        if return_description is not None:
            content += '\n**Return Value**  \n%s\n' % (return_description)
    except (KeyError, AttributeError):
        pass

    return content + '\n'


# Built with Little Hedgehog Docs by Pig on a Hill Productions.
def build_page_footer():
    return (
        '<div class="footer" align="center">'
        '<sub>Built with '
        '<a href="'
        'https://github.com/Baza207/LittleHedgehogDocs"'
        ' target="_blank">'
        'Little Hedgehog Docs'
        '</a> by '
        '<a href="mailto:james@pigonahill.com" target="_blank">'
        'James Barrow'
        '</a> - '
        '<a href='
        '"http://pigonahill.com"'
        ' target="_blank">'
        'Pig on a Hill Productions'
        '</a>.'
        '</sub>'
        '</div>\n'
    )
