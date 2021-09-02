#!/bin/bash

echo "Compressing pretrained model..."
model_path=learning-tsp/pretrained/tsp_20-50/rl-ar-var-20pnn-gnn-max_20200313T002243
mv $model_path/{epoch-99.pt,model.pt}
tar -cvzf $model_path/model.tar.gz $model_path/

cp -r learning-tsp/{nets,problems,reinforce_baselines.py,utils} src
# mkdir learning-tsp/src
# mv learning-tsp/{nets,problems,reinforce_baselines.py,utils} learning-tsp/src
# mv src/*.py learning-tsp/src
