from pprint import pformat, pprint


import xmltodict
import genson

fn = "xml_example1.xml"
with open(fn) as fh:
    xd = xmltodict.parse(fh.read())

print(pformat(xd))

print(pformat(xd['catalog']['book']))

fan_books = [x['title'] for x in xd['catalog']['book'] if x['genre'] == "Fantasy"]
print(" {} {}".format(len(fan_books), fan_books))

sb = genson.SchemaBuilder()
sb.add_object(xd)
print(sb.to_json(indent=2))