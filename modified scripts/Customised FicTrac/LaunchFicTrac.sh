#!/bin/bash

# Navigate to the script's directory
cd "$(dirname "$0")"

# Get the current user's home directory
USER_FOLDER=$(echo "$HOME")  # Convert to Windows-style path

# Construct the path to the executable
EXECUTABLE_PATH="$USER_FOLDER/fictrac/bin/Release/fictrac.exe"

# Display the EXECUTABLE_PATH
echo "Executable Path: $EXECUTABLE_PATH"

# Run the command with the specified config file
"$EXECUTABLE_PATH" config.txt
