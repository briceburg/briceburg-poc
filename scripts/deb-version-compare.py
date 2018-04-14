#!/usr/bin/env python
from __future__ import print_function
import argparse
import sys
import apt_pkg

class HelpParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help(sys.stderr)
        self.exit(1)

parser = HelpParser(description='prints debian package versions in descending order.')
parser.add_argument('versions', metavar='deb-version', type=str, nargs='+',
                   help='version string ([epoch:]upstream-version[-debian-revision])')
args = parser.parse_args()
versions = args.versions

if len(versions) > 1:
    apt_pkg.init_system()
    print(*sorted(versions, cmp=apt_pkg.version_compare, reverse=True), sep='\n')
else:
    print(versions[0])
