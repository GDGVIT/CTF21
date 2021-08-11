#/bin/bash

export PORT=8080
socat TCP-LISTEN:$PORT,reuseaddr,fork EXEC:./challenge,pty,echo=0
