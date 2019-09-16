import json
from pprint import pformat

# simplejson

fn = "test.json"
with open(fn) as fh:
    jd = json.load(fh)

print(pformat(jd))

print(type(jd))

print(type(json.dumps(jd)))

fn = "testbuggy.json"
with open(fn) as fh:
    jd = json.load(fh)

print(pformat(jd))
