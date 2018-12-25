#!/bin/bash
echo "Cleaning File..."
> "README.md"
echo "Adding Title..."
echo "# Site Screenshots" >> "README.md"
for filename in *.png; do
        echo "Adding image: $filename"
        echo "## Image: $filename" >> "README.md" 
        echo "![$filename]($filename)" >> "README.md"
done
