#!/bin/bash
echo "Installing packages..."
source activate pytorch_latest_p36
pip install -r requirements.txt


echo "Compressing pretrained model..."
model_path=learning-tsp/pretrained/tsp_20-50/rl-ar-var-20pnn-gnn-max_20200313T002243
cd $model_path
mv epoch-99.pt model.pt
tar -cvzf model.tar.gz *

echo "Moving training and inference files to single source directory..."
cd -
cp -r learning-tsp/{nets,problems,reinforce_baselines.py,utils} src
