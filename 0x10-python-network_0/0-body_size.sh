#!/bin/bash
#get the byte size of the http response for a given URL.

curl -s "$1" | wc -c
