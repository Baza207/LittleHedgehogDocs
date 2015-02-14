# LittleHedgehogDocs
[![Build Status](https://travis-ci.org/Baza207/LittleHedgehogDocs.svg)](https://travis-ci.org/Baza207/LittleHedgehogDocs)  

Little Hedgehog Docs is a Swift documentation comments to Markdown document builder. It runs off of
[SourceKitten](https://github.com/jpsim/SourceKitten) to parse the documentation comments from Xcode
and then builds Markdown files for use in GitHub Wiki.

**Note:** This is currently still a work in progress. I want to be able to include Obj-C
documentation in the future, as well as expand the range of the documents built for Swift.

## Installing

Before installing LHDocs you will need to install SourceKitten. Goto the link below and follow the
install instructions.
[github.com/jpsim/SourceKitten](https://github.com/jpsim/SourceKitten#command-line-usage)

Once you have installed SourceKitten successfully, clone or download LHDocs and cd to the package's
root directory in the terminal. From there you can call `[sudo] python setup.py install` which will
install the LHDocs package.

And that's it!

**Note:** I am looking to submit LHDocs to PyPI to be able to install with `pip` around version 0.4.

## Usage

LHDocs currently runs with 3 options to pass in, 2 of which are required.  
- `-project`: **required** The Xcode project file for the project you want to build docs for.
- `-target`: **required** The Xcode target in the project you want to build docs for. This will also
be used as the directory name all your documentation files are written to.
- `-output`: The location you want to save the docs. By default this is set to `~/`.

**Note:** More options will be introduced for working with Workspaces, specifying the name of the
save directory and so on in version 0.4.

#### Example
```shell
lhdocs -project MyAwesomeProject.xcodeproj -scheme MyAwesomeProject
```  
-or-  
```shell
lhdocs -project path/to/my/project/MyAwesomeProject.xcodeproj -scheme MyAwesomeProject -output ../
```

## Sample Documentation

On it's way...

## Roadmap
##### 0.1 - Complete
- [x] Use the command line and parse in options.
- [x] Basic parsing and building of documentation for classes, functions and parameters.
- [x] Save markdown files to a directory.
- [x] Don't parse comments that are not in a class as separate files.
- [x] Create a working Python package for the project.

##### 0.2 - _Current_
- [ ] Build all global functions into one file.
- [ ] Build all global parameters into one file.
- [ ] Build all global structs into one file.
- [ ] Build all global enums into one file.
- [ ] Build all global protocols into one file.
- [ ] Build extension classes.

##### 0.3
- [ ] Add a table of contents with linking to the correct section at the beginning of each page.
- [ ] Save pages into folders depending on the type (class, struct, etc).
- [ ] Save global functions, etc into a single file (i.e. 1 global functions file, 1 global
parameters file, etc).

##### 0.4
- [ ] Add more options to set via the command line (clean before save, parse TODO: and/or FIXME:,
etc).
- [ ] Only build items for specific accessibility options.
- [ ] Add the ability to build docs for single files.
- [ ] Submit to PyPI.

##### 0.5
- [ ] Build Obj-C docs.

## License

MIT Licence

## Creator

[James Barrow](james@pigonahill.com)
