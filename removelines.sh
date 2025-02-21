#!/bin/bash
input_file=$1
clean_file=$2
awk '!/^[[:space:]]*$/' "input_file" > "clean_file"
