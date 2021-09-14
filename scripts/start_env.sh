#!/bin/bash -ex

WORKING_DIR=./.myenv
# get the env name
line=$(head -n 1 environment.yml)
ENV_NAME="${line/name:\ /}"
PWD=$(pwd)

# fix an issue for displaying plotly
# jupyter labextension install jupyterlab-plotly

source "$WORKING_DIR/miniconda/bin/activate"
conda activate $ENV_NAME

# Cleanup
conda deactivate
source "${WORKING_DIR}/miniconda/bin/deactivate"

# Add the following env dir to envs_dirs
conda config --add envs_dirs "$PWD/$WORKING_DIR/miniconda/envs"

# Activate the kernel by list the envs
conda env list

# Required for notebook to show the environment
sudo initctl restart jupyter-server --no-wait
