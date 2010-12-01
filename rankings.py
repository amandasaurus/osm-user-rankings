#! /usr/bin/python
import sys
from xml.etree import ElementTree
from collections import defaultdict

def users_whove_edited(filename):
    for event, el in ElementTree.iterparse(open(filename)):
        if 'user' in el.attrib:
            yield el.attrib['user']
        el.clear()

def count_occurances(iter):
    results = defaultdict(int)
    for el in iter:
        results[el] += 1
    return sorted(((results[x], x) for x in results), reverse=True)

def rankings(filename):
    users = count_occurances(users_whove_edited(filename))
    for user in users:
        print "%10d %s" % user



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: %s FILENAME" % (sys.argv[0])
    else:
        rankings(sys.argv[1])
    
