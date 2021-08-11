#/bin/bash

apt-get update
ap-get install socat
gcc -ggdb  -fno-stack-protector -z execstack -static -o challenge record_keeper.c
