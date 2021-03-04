# UBDC CCTV API CLIENT

### Description

A python client to get cctv data from our public api services at

https://api.ubdc.ac.uk/cctv
### Installation

It's recommended to use a virtual environment to install this client in

```bash
# install from github since this package is not published yet
pip install git+https://github.com/urbanbigdatacentre/ubdc_cctvapi.git
```

### How to use

This package fetches data from UBDC's public API end point and makes them available for further processing. It is
straight forward how it can be used, as seen from the examples bellow:

```python
# import the client
from ubdc_cctvapi.api import CctvApi

api = CctvApi()
# fetch one day's data for the location LOCATION
# and return it as python dict.
data = api.get_data_for_location("LOCATION", "6/6/2020", "7/6/2020")
for k, v in data.items():
    ...
```

### Dev notes

#### install dev packages

pip install -r requirements

#### Update dev packages to the  version :

```bash
pip install pip-tools # if you haven't already done
pip-compile # to gather the latest version
pip-sync # to apply newest versions
```

#### Patch Version Bump

```bash
bumb2version -n --verbose patch
```

#### Minor or Major version bump:

```bash
#minor 
bumb2version -n --verbose minor

# major
bumb2version -n --verbose major
```

#### Test Running

```bash
pip install -e .
pytest
```

### Support

This project should be supported as long the CCTV project is running. 
