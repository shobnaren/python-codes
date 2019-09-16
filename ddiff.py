from deepdiff import DeepDiff

x = {"a": 1, "b": 2, "c": 3}
y = {"a": 1, "c": 43}

dd = DeepDiff(y, x)

from pprint import pprint

pprint(dd)
