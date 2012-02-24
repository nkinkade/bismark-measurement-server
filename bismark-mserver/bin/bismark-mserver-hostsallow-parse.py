#!/usr/bin/python

import sys
import datetime

try:
    import json
except ImportError:
    # compensate for lack of json in python < 2.6
    try:
        import simplejson
        json = simplejson
    except ImportError, ie:
        print("\n# ERROR: %s" % ie)
        sys.exit(1)

try:
    f = open(sys.argv[1], 'r')
    j = json.load(f)
    print("# hosts.allow")
    print("# generated at %s UTC" % datetime.datetime.utcnow().isoformat())
    print("# generated by %s\n" % sys.argv[0])
    for k,v in j['hosts.allow'].iteritems():
        print("%s : %s" % (k,v))
except StandardError, e:
    print("\n# ERROR: %s" % e)
else:
    print("\n# done")

