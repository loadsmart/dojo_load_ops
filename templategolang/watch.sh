#!/bin/bash

go test ./...

while true
do
    inotifywait -qq -r -e create,close_write,modify,move,delete ./ && clear && go test ./...
done