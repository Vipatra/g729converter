#!/bin/bash

set -e

cd dpdg927

cmake . -DCMAKE_INSTALL_PREFIX=g729 -DCMAKE_PREFIX_PATH=g729 -DENABLE_TESTS=YES
make
make install