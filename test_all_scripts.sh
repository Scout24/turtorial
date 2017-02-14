#!/bin/bash

# Test to see if all my example scripts still work.

for turtorial_file in ./*.py; do
    echo hello | $turtorial_file || {
        echo "Test failed!"
        exit 1
    }
done

echo "Test successful"
