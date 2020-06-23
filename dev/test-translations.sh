#!/bin/bash

#set -e
#set -o pipefail

pushd dev

echo "Translating test sentences"
cat test-sentences-scn.txt | apertium -d .. scn-spa > test-sentences-scn-spa.txt

./test-grep.sh

popd

echo "Checking for differences"
git diff --exit-code
