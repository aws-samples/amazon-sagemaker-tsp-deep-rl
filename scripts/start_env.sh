#!/bin/bash -ex

WORKING_DIR=./.myenv
# get the env name
line=$(head -n 1 environment.yml)
ENV_NAME="${line/name:\ /}"
PWD=$(pwd)

source "$WORKING_DIR/miniconda/bin/activate"
conda activate $ENV_NAME
