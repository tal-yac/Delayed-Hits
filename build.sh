#! /bin/bash

do_build() {
    cd build
    cmake ..
    make
    cd ..
}

time do_build
