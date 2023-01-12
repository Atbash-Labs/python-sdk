# Fortress Python SDK

## Usage:

You can download the module by executing the following command 
(replace `<tag>` with the version you would like to download):
```bash
pip install git+https://github.com/Atbash-Labs/python-sdk@<tag>
```

The module can then be used as follows:
```python
from fortress_sdk import Buyer
```

check out these [demo](./examples)  interactions with the library

## Local setup:

```bash
#  Local doc metadata files auto generate
sphinx-apidoc -o docs/ fortress_sdk/
```
```bash
#  To local preview docs and generated docs will be loacted in docs/_build
cd docs/
make html 
```

