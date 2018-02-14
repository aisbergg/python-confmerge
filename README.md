# ConfMerge - Python3 configuration file merge utility

*ConfMerge* lets you merge multiple configuration files into one. Currently supported file formats are INI, YAML and JSON.

**Table of contents:**
<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Installation](#installation)
- [Usage](#usage)
	- [Examples](#examples)
- [License](#license)

<!-- /TOC -->

---

## Installation

To install *ConfMerge* directly from Github:
```
pip install git+https://github.com/Aisbergg/python-confmerge@v0.1.0
```

## Usage

```
usage: confmerge [-h] [-d] [-f] [-m MODE] [-t FILE_TYPE] [--debug] [--version]
                 src [src ...] dest

Merge multiple configuration files into one.

positional arguments:
  src                   The source files.
  dest                  The destination file.

optional arguments:
  -h, --help            show this help message and exit
  -d, --dry-run         Print the resulting merged content but don't write it
                        into the destination file.
  -f, --force           Force overwriting of an existing file.
  -m MODE, --mode MODE  File mode for newly created configuration file.
  -t FILE_TYPE, --type FILE_TYPE
                        Type of file can be one of 'ini', 'json' or 'yaml'. If
                        not specified the type will be guessed from the file
                        extension.
  --debug               Print debug trace on error.
  --version             Prints the program version and quits.
```

### Examples

Merge multiple INI files and write result into `res.ini`
```
confmerge -f 1.ini 2.ini 3.ini res.ini
```

Merge different types of configuration files:
```
confmerge -f 1.yml 2.json 3.ini res.yml
```

Perform a dry run (don't write output file but print result on stdout):
```
confmerge -d 1.yml 2.yml not-touched.yml
```

## License

ConfMerge is released under the LGPL v3 License. See LICENSE for more information.
