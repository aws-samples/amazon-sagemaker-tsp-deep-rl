#!/bin/bash -ex

WORKING_DIR=./.myenv
# get the env name
line=$(head -n 1 environment.yml)
ENV_NAME="${line/name:\ /}"

mkdir -p "${WORKING_DIR}"
PWD=$(pwd)

# fix an issue for displaying plotly
# jupyter labextension install jupyterlab-plotly

# Install Miniconda to get a separate python and pip
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O "$WORKING_DIR/miniconda.sh"

# Install Miniconda into the working directory
bash "$WORKING_DIR/miniconda.sh" -b -u -p "$WORKING_DIR/miniconda"

# Install pinned versions of any dependencies
source "$WORKING_DIR/miniconda/bin/activate"

# Set cuda variable if GPU is needed for some packages 
# export CUDA_VISIBLE_DEVICES=0

conda env create -f environment.yml

conda activate $ENV_NAME

# add this as a kernel
pip install ipykernel

# Cleanup
conda deactivate
source "${WORKING_DIR}/miniconda/bin/deactivate"
rm -rf "${WORKING_DIR}/miniconda.sh"

# Add the following env dir to envs_dirs
conda config --add envs_dirs "$PWD/$WORKING_DIR/miniconda/envs"

# Activate the kernel by list the envs
conda env list

# Optional
#sudo initctl restart jupyter-server --no-wait
