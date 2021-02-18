#!/bin/bash

while true
do
    inotifywait -qq -r -e create,close_write,modify,move,delete ./ && clear && pytest problem.py
done