#!/bin/bash
#get the byte size of the http response for a given URL.

curl -s "$1" -o /dev/null -w '%{size_download}\n'

