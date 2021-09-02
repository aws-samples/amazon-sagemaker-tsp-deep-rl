from utils import load_model, move_to
from problems.tsp.problem_tsp import nearest_neighbor_graph

import logging
import os
import torch
import requests
import json
import tqdm

logger = logging.getLogger(__name__)


def model_fn(model_dir):
    logger.info("In model_fn. Model directory is -")
    logger.info(model_dir)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model, model_args = load_model(os.path.join(model_dir, "model.pt"),
                                   extra_logging=True)
    model.to(device)
    model.set_decode_type("greedy")
    model.eval()
    return model

def input_fn(request_body, content_type='application/jsonlines'):
    if content_type == 'application/jsonlines':
        print("request received!!")
        print(type(request_body))
        # Warning: for some reason, when Sagemaker is doing batch transform,
        # it automatically adds a line break in the end, needs to strip the line break to avoid errors.
        # Sagemaker Endpoint doesn't have such issue.
        lines = request_body.decode("utf-8").rstrip(os.linesep).split(os.linesep)
        data = []
        print(len(lines))
        for line in lines:
            line = line.strip()
            print(type(line), len(line))
            input_data = json.loads(line)
            data.append(input_data)
        return data

    raise Exception(f'Requested unsupported ContentType in content_type {content_type}')

def predict_fn(input_data, model):
    prediction=[]
    for bat in tqdm.tqdm(input_data):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        nodes = bat['nodes']
        neighbors = bat['neighbors']
        x = move_to(torch.FloatTensor(nodes), device)
        g = []
        for n in nodes:
            gg = nearest_neighbor_graph(n,
                                       neighbors=neighbors,
                                       knn_strat='percentage')
            g.append(gg)
        graph = move_to(torch.ByteTensor(g),
                        device)
        cost, ll, pi = model(x, graph, return_pi=True)
        print(f'cost:{cost}')
        prediction.append(pi.tolist())
    return prediction
    
def output_fn(prediction, accept='application/jsonlines'):
    if accept == 'application/jsonlines':
        ret = ''
        for p in prediction:
            ret += json.dumps(p) + os.linesep
        return ret, accept
    raise Exception(f'Requested unsupported ContentType in Accept: {accept}')
