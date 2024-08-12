#!/bin/bash

# Save the current directory
current_dir=$(pwd)

# Check if the 'code' command is available
if ! command -v code &> /dev/null
then
    echo "'code' command could not be found"
    exit
fi

if [ -d "$1" ]; then
    cd $1
    count=$(ls -1 $1*.py 2>/dev/null | wc -l)
    filename=$1_$count.py

    touch $filename
    # Add hyperlink to the new file in README.md
    echo "- [$filename]($filename)" >> README.md

    code $filename
else
    mkdir -p $1
    cd $1
    touch $1.py input.txt output.txt

    echo "## $1" >> README.md
    # Add hyperlinks to the files in README.md
    echo "- [$1.py]($1.py)" >> README.md
    echo "- [input.txt](input.txt)" >> README.md
    echo "- [output.txt](output.txt)" >> README.md

    code $1.py
fi

# Go back to the original directory
cd $current_dir