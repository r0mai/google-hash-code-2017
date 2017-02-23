#!/bin/bash

for p in inputs/*; do
    ./build/hashcode < $p > "output/$(basename "$p").out" &
done
wait
