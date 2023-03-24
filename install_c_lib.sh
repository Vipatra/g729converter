#!/bin/bash

set -e

echo "PWD is `pwd`"

cd dpdg729


install(){
    install_prefix=$1
    cmake . -DCMAKE_INSTALL_PREFIX=${install_prefix} -DCMAKE_PREFIX_PATH=${install_prefix} -DENABLE_TESTS=YES
    make
    make install
}