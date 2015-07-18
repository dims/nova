#!/usr/bin/env bash

set -o pipefail

TESTRARGS=$1

# --until-failure is not compatible with --subunit see:
#
# https://bugs.launchpad.net/testrepository/+bug/1411804
#
# this work around exists until that is addressed
if [[ "$TESTARGS" =~ "until-failure" ]]; then
    python setup.py testr -q --slowest --testr-args="$TESTRARGS"
else
    python setup.py testr -q --slowest --testr-args="--subunit $TESTRARGS" | subunit-trace -f --no-summary
fi
