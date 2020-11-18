#!/bin/bash
set -eo pipefail
rm -rf ./layer1
cd sample_code1
/Library/Frameworks/Python.framework/Versions/3.8/bin/pip3 install --target ../layer1/python -r requirements.txt
