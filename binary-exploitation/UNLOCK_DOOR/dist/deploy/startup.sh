#/bin/bash

export PORT=8080
socat TCP-LISTEN:8080,reuseaddr,fork EXEC:./challenge,echo=0
