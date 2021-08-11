#/bin/bash

apt-get update
apt-get install socat
gcc -ggdb  -fno-stack-protector -static -o challenge destructinator_login.c
