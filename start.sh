#!/bin/bash

echo "Start Script!"
echo "Detect VENV"

if [ -d  "./venv" ]; then
    echo "VENV FOLDER exists!"
    if [ -f  "./venv/bin/activate" ];then
        echo "VENV exists!"
    fi
    
else
    echo "No virtual environment named "venv" found in the current directory."
    python3 -m venv venv
fi

source venv/bin/activate
pip3 install -r requirements.txt
uvicorn server:app --reload




