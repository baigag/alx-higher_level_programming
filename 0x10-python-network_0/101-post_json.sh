#!/bin/bash
#sends a JSON POST request to a given URL with a given JSON file
curl -sL -X POST -d "@$2" -H "Content-Type: application/json" "$1"
