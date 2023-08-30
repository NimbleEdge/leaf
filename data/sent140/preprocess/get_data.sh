#!/usr/bin/env bash

cd ../data/raw_data

if [ ! -f trainingandtestdata.zip ]; then
    gdown 0B04GJPshIjmPRnZManQwWEdTZjg
fi

unzip trainingandtestdata.zip

mv training.1600000.processed.noemoticon.csv training.csv
mv testdata.manual.2009.06.14.csv test.csv

rm trainingandtestdata.zip

cd ../../preprocess