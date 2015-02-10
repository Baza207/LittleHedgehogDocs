#
# mian.py
# LittleHedgehogDocs
#
# Created by James Barrow on 09/02/2015.
# Copyright (c) 2015 James Barrow - Pig on a Hill Productions. All rights reserved.
#

#!/usr/bin/env python

import sys, argparse, os, subprocess, json
import build_docs

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

  pages = build_docs.build_sourcekitten(sourcekitten_JSON)

  print "\n---------------------------------------------------\n"

  filename = None
  if args.scheme != None:
    filename = args.scheme
  else:
    filename = 'Docs'
  filename = '%s.md' %(filename)

  output_filepath = os.path.join(current_filepath, args.output, filename)
  print "Saving to file to: '%s'" %(output_filepath)

  print "\n---------------------------------------------------\n"

  markdown_content = pages[3][1]
  obj = open(output_filepath, 'w+b')
  obj.write(markdown_content)
  obj.close

  print "Saved! Have a nice day. :)"

  print "\n---------------------------------------------------\n"

  sys.exit()

if __name__ == '__main__':
  main()
