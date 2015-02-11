# LittleHedgehogDocs
[![Build Status](https://travis-ci.org/Baza207/LittleHedgehogDocs.svg)](https://travis-ci.org/Baza207/LittleHedgehogDocs)  

Little Hedgehog Docs is a Swift documentation comments to Markdown document builder. It runs off of [SourceKitten](https://github.com/jpsim/SourceKitten) to parse the documentation comments from Xcode and then builds Markdown files for use in GitHub Wiki.

**NOTE:** This is currently still a work in progress. I want to be able to include Obj-C documentation in the future, as well as expand the range of the documents built for Swift.

## Installing

On it's way...

## Command Line Useage

On it's way...

## Roadmap
##### 0.1
- [x] Use the command line and parse in argemnts.
- [x] Basic parsing and building of documentation for classes, functions and paramiters.
- [x] Save markdown files to a directory.
- [x] Don't parse comments that are not in a class as a seperate file.
- [ ] Parse `&amp;` and similar symbols correctly.
- [ ] Create a working Python package for the project.

##### 0.2
- [ ] Build all global functions into pne file.
- [ ] Build all global paramiters into pne file.
- [ ] Build all global structs into pne file.
- [ ] Build all global enums into pne file.
- [ ] Build all global protocols into pne file.
- [ ] Build extension classes.

##### 0.3
- [ ] Add a table of contents with linking to the correct section at the beginig of each page.
- [ ] Save pages into folders depending on the tpye (class, struct, etc).
- [ ] Save global functions, etc into a single file (i.e. 1 global functions file, 1 global paramiters file, etc).

##### 0.4
- [ ] Add more options to set via the command line (clean before save, parse TODO: and/or FIXME:, etc).
- [ ] Only build items for specific accessibility options.
- [ ] Add the ability to build docs for single files.

##### 0.5
- [ ] Build Obj-C docs.

## License

MIT Licence

## Creator

[James Barrow](james@pigonahill.com)
