#! /bin/bash

do_build() {
    mkdir -p build 
    cd build
    cmake ..
    make
    cd ..
}

time do_build
