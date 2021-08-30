import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk
import os
import healpy as hp
import joblib
import sys
sys.path.append("./src")

import boto3

from problems.tsp.problem_tsp import TSP
from torch.utils.data import DataLoader

import random
import datetime
import time
from collections import Counter

import matplotlib.pyplot as plt
from scipy.spatial import distance

from sagemaker.predictor import Predictor
from sagemaker.serializers import JSONLinesSerializer
from sagemaker.deserializers import JSONLinesDeserializer

"""
    To demonstrate features of GNN and RL-based routing
"""

def generate_one_tsp_problem(neighbors = 0.20,
                             num_nodes=10):
    dataset_path = None
    batch_size = 1
    accumulation_steps = 80
    num_samples = 1
    knn_strat = 'percentage'
    
    dataset = TSP.make_dataset(
        filename=dataset_path,
        batch_size=batch_size,
        num_samples=num_samples,
        min_size=num_nodes,
        max_size=num_nodes,
        neighbors=neighbors,
        knn_strat=knn_strat,
        supervised=False
    )
    dataloader = DataLoader(dataset,
                        batch_size=batch_size,
                        shuffle=False,
                        num_workers=0)
    # transform data
    data = []
    for bat_idx, bat in enumerate(dataloader):
        input = {}
        input["nodes"] = bat["nodes"].tolist()
        data.append(input)
    for record in data:
        record["neighbors"] = neighbors
    return data

def show_err_msg(st, msg):
    st.markdown(
        f"""
            {msg}
            """
    )

def plot_route_on_normspace(sequence, X1, Y1, station, plot_arrow=True):
    plt.grid(linestyle='--')
    plt.scatter(X1, Y1, facecolors='none', edgecolors='b')
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    if (plot_arrow):
        st_x = X1[sequence[0]]
        st_y = Y1[sequence[0]]
        plt.scatter(st_x, st_y, facecolors='none', edgecolors='r', s=135)
        for i in range(len(X1) - 1):
            plt.arrow(X1[sequence[i]], Y1[sequence[i]], X1[sequence[i + 1]] - X1[sequence[i]], Y1[sequence[i + 1]] - Y1[sequence[i]], head_width=0.03, head_length=0.02, fc='b', ec='k', alpha=.3)
        i = -1
        plt.arrow(X1[sequence[i]], Y1[sequence[i]], X1[sequence[i + 1]] - X1[sequence[i]], Y1[sequence[i + 1]] - Y1[sequence[i]], head_width=0.03, head_length=0.02, fc='g', ec='k', alpha=.6)
    plt.axes().set_aspect('equal')
    return plt.gcf()

def get_latest_endpoint():
    client = boto3.client("sagemaker")

    # Get the trained sklearn model
    response = client.list_endpoints(
        NameContains="pytorch-inference",
        SortBy="CreationTime",
        SortOrder="Descending",
    )
    endpoint_name = response['Endpoints'][0]['EndpointName']
    return endpoint_name

def inference_endpoint(data,
                       endpoint_name,
                       serializer,
                       deserializer):
    """
    Inference via Sagemaker endpoint.
    """
    # get the predictor from the endpoint
    predictor = Predictor(endpoint_name=endpoint_name, 
          sagemaker_session=None,
          serializer=serializer,
          deserializer=deserializer,)
    # Send the data to endpoint for inference
    prediction = predictor.predict(data)
    
    # Get the rank list
    so_list = np.array(prediction[0][0])

    X = np.array(data[0]["nodes"])
    rank_list = [-1] * X.shape[1]
    for i, rank in enumerate(so_list):
        try:
            rank_list[rank] = i
        except:
            raise Exception(f'{i}, {rank}')
    
    return rank_list, so_list

def main():
    """
    TSP demo.
    """
    route_length = st.slider('Route length', 10, 300, 50, step=10)
    
    if 'data' not in st.session_state:
        st.session_state.data = None
    
    if st.button('Generate a new TSP problem'):
        st.session_state.data = generate_one_tsp_problem(num_nodes=route_length)
        X = np.array(st.session_state.data[0]["nodes"])
        st.info(f'The TSP problem has {route_length} nodes')
        fig_norm = plot_route_on_normspace(np.arange(0, route_length), X[0, :, 0], X[0, :, 1], 0, plot_arrow=False)
        print("data loaded ...")
        if (fig_norm is not None):
            st.pyplot(fig_norm)
    serializer = JSONLinesSerializer()
    deserializer = JSONLinesDeserializer()
    
    # get the latest endpoint
    endpoint_name = get_latest_endpoint()

    if st.button('Routing via the Deep Reinforcement Learning model...'):
        # Retrieve app state
        app_state = st.experimental_get_query_params()  
    
        rank_list, so_list = inference_endpoint(st.session_state.data,
                   endpoint_name,
                   serializer,
                   deserializer)
        X = np.array(st.session_state.data[0]["nodes"])
        fig_norm = plot_route_on_normspace(so_list, X[0, :, 0], X[0, :, 1], 0)
        print("route loaded ...")
        if (fig_norm is not None):
            st.pyplot(fig_norm)

if __name__ == "__main__":
    main()
