#!/bin/bash

# Only keep time directories that are:
# - folder "0"
# - multiples of 10 (like 10, 20, 30, ..., 1000)

echo "🧹 Cleaning unwanted time directories..."

for dir in [0-9]*; do
    if [[ -d "$dir" && "$dir" =~ ^[0-9]+$ ]]; then
        if [[ "$dir" != "0" && $((dir % 10)) -ne 0 ]]; then
            echo "Deleting $dir"
            rm -rf "$dir"
        fi
    fi
done

# Now clean subdirectories in postProcessing (like forces/3, etc.)
echo "🧹 Cleaning postProcessing junk..."

find postProcessing -type d -regex '.*/[0-9]+' ! -regex '.*/\(0\|[0-9]\{2,\}0\)' -exec rm -r {} +

echo "✅ Done cleaning."
