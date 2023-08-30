#!/usr/bin/env bash

# Parse data directory argument
# while getopts ":p:" opt; do
#     case "$opt" in 
#         p) 
#         data_path="$OPTARG"
#         ;;
#     esac
# done
data_path="/mnt/share/femnist"

echo "Folder name :$data_path"
# download data and convert to .json format

if [ ! -d "$data_path/raw/all_data" ] || [ ! "$(ls -A $data_path/raw/all_data)" ]; then
    cd preprocess
    ./data_to_json.sh $data_path
    cd ..
fi

NAME="femnist" # name of the dataset, equivalent to directory name
# cd ../utils

# ./preprocess.sh --name $NAME $@ 

# cd ../$NAME