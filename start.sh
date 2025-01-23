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
pm2 delete Image_Embed
pm2 start 'uvicorn server:app --port 7500 --host 0.0.0.0' -n Image_Embed




