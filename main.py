#
# mian.py
# LittleHedgehogDocs
#
# Created by James Barrow on 09/02/2015.
# Copyright (c) 2015 James Barrow - Pig on a Hill Productions. All rights reserved.
#

#!/usr/bin/env python

import sys, argparse, os, subprocess, json
from bs4 import BeautifulSoup

def usage():
  print "This is a help file!"

def main():
  current_filepath = os.path.dirname(os.path.realpath(__file__))

  parser = argparse.ArgumentParser(prog='LittleHedgehogDocs', description='Parse Swift documentation into Markdown files.')
  parser.add_argument('-project', dest='project', help='The Xcode project to parse.')
  parser.add_argument('-scheme', dest='scheme', help='The Xcode scheme to parse.')
  parser.add_argument('-output', dest='output', default='', help='The output file.')

  args = parser.parse_args()
  subprocess.call('clear')

  print "\n---------------------------------------------------\n"

  print "Welcome to Little Hedgehog Docs"

  print "\n---------------------------------------------------\n"

  print "Runnig SourceKitten..."
  sourcekitten_result = subprocess.check_output(['sourcekitten', 'doc', '-project', args.project, '-scheme', args.scheme])
  sourcekitten_JSON = json.loads(sourcekitten_result)

  print "\n---------------------------------------------------\n"

  for item in sourcekitten_JSON:
    for structure in item['key.substructure']:
      print "%s" %(structure['key.name'])
      for substructure in structure['key.substructure']:
        # print substructure
        print "  %s" %(substructure['key.name'])
        try:
          soup = BeautifulSoup(substructure['key.doc.full_as_xml'])
          print "    %s" %(soup.para.get_text())
        except Exception, e:
          pass
      print ""

  print "\n---------------------------------------------------\n"

  output_filepath = os.path.join(current_filepath, args.output, 'SourceKitten.json')
  print "Saving to file to: '%s'" %(output_filepath)

  print "\n---------------------------------------------------\n"

  json_string = json.dumps(sourcekitten_JSON, sort_keys=True, indent=2, separators=(',', ': '))
  obj = open(output_filepath, 'w+b')
  obj.write(json_string)
  obj.close

  print "Saved! Have a nice day. :)"

  print "\n---------------------------------------------------\n"

  sys.exit()

if __name__ == '__main__':
  main()
