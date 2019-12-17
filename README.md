# JsonParser CLIENT PYTHON

A client for JsonParser and a way to generate it's portable distribution.

## Requirements

- Python (3.x)
- Pyinstaller


## How to generate your portable version

Just follow theese steps:

```shell
# Dont forget to install pyinstaller
pip3 install pyinstaller

# Then just hit for the send script
pyinstaller ./jsonp.py --hidden-import=json --hidden-import=argparse --onefile --name jsonp

# Then you will get some logs down here
46 INFO: PyInstaller: 3.5
46 INFO: Python: 3.5.2
48 INFO: Platform: Linux-4.15.0-72-generic-x86_64-with-Ubuntu-16.04-xenial
49 INFO: wrote /home/darker/ACTUALC/vagrant/PYTHON/github/jsonParser/jsonp.spec
58 INFO: UPX is available.
59 INFO: Extending PYTHONPATH with paths
['/home/darker/ACTUALC/vagrant/PYTHON/github/jsonParser',
 '/home/darker/ACTUALC/vagrant/PYTHON/github/jsonParser']
59 INFO: checking Analysis
60 INFO: Building Analysis because Analysis-00.toc is non existent
60 INFO: Initializing module dependency graph...
62 INFO: Initializing module graph hooks...
64 INFO: Analyzing base_library.zip ...
4592 INFO: Analyzing hidden import 'json'
4677 INFO: running Analysis Analysis-00.toc
....
```

Your distribution just got generated.


## How to use it

- This is how to use send :

```shell
usage: jsonp [-h] [-f FILE] [-s STRING] -k KEY

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  The file containing the JSON-STRING
  -s STRING, --string STRING
                        The Complete JSON-STRING
  -k KEY, --key KEY     The key of the JSON object you want

```

Example :

  - `python jsonp.py -s "{\"key\":\"value\"}" -k key`
  - `./jsonp -s "{\"key\":\"value\"}" -k key`

---------------------------

## Author

- Sanix-darker