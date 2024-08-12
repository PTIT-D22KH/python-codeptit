#!/bin/bash

# Function to update README.md with all files in the directory
update_readme() {
    local dir=$1
    local readme_file="$dir/README.md"

    # Clear the existing content in README.md
    echo "## $dir" > "$readme_file"
    # echo "![alt text](image.png)" >> "$readme_file"
    echo "" >> "$readme_file"
    
    # Add hyperlinks to all files in the directory
    for file in "$dir"/*; do
        if [ -f "$file" ]; then
            filename=$(basename -- "$file")
            echo "- [$filename]($filename)" >> "$readme_file"
        fi
    done
}

# Get the directory of the Python file
dir=$(dirname -- "$1")

# Update README.md before running the script
update_readme "$dir"

# Get the base name of the Python file
filename=$(basename -- "$1")
filename="${filename%.*}"

# Run the Python script
python3 "$1" < "$dir/input.txt"