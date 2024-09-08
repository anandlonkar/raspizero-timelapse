#!/bin/bash

# schedule for crontab
# */5 6-20 * * * /home/<username>/raspitimelapse.sh 2>&1

# Directory containing the images
DIR="~/raspitimelapse"

# Find the highest number in the filenames
max_num=$(ls $DIR/img_*.jpg | awk -F'[_|.]' '{print $3}' | sort -n | tail -1)

# Increment the number
new_num=$(printf "%05d" $((10#$max_num + 1)))

# Get the current date in YYYYMMDD format
current_date=$(date +%Y%m%d)

# Create the new filename
new_filename="$DIR/img_${current_date}_${new_num}.jpg"


rpicam-still -v 0 -o $new_filename 
timestamp=$(date +"%Y-%m-%d %H:%M:%S")
convert "$new_filename" -gravity NorthEast -pointsize 40 -fill red -undercolor '#00000080' -annotate +10+10 "$timestamp" "$new_filename"

echo "Created new file: $new_filename"