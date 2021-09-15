# Solving the Travelling Salesperson Problem with deep reinforcement learning on Amazon SageMaker

## Introduction

The [Travelling Salesperson Problem ](https://en.wikipedia.org/wiki/Travelling_salesman_problem) (TSP) is one of the most popular [NP-hard](https://xlinux.nist.gov/dads/HTML/nphard.html) combinatorial problems in the  theoretical computer science and operations research (OR) community. It asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?".

The problem has been studied for decades, and many traditional optimization algorithms have been proposed to solve it, such as [dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming) and [branch-and-bound](https://en.wikipedia.org/wiki/Branch_and_bound). Although these optimization algorithms are capable of solving TSP with dozens of nodes, it is usually intractable to use these algorithms to solve optimally above thousands of nodes on modern computers due to their exponential execution times.

In this repository, we demonstrate show how to train, deploy, and make inferences using deep reinforcement learning to solve the Travelling Salesperson Problem.

For additional explanation, see the forthcoming blog post: [Solving the Travelling Salesperson Problem with deep reinforcement learning on Amazon SageMaker](.)

## Getting Started

**1. Create a SageMaker notebook instance.**

This repository is meant to be run on a SageMaker notebook instance. For details on how to create a notebook instance, see the [aws documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/howitworks-create-ws.html).

**2. Clone the repository with submodule into the SageMaker directory.**

This will clone the current repository as well as the submodule repository: [learning-tsp](https://github.com/chaitjo/learning-tsp).

```
cd SageMaker
git clone --recurse-submodules https://github.com/aws-samples/amazon-sagemaker-tsp-deep-rl.git
cd amazon-sagemaker-tsp-deep-rl
```

From here on out, scripts are to be run from the git project root.

**3. Create the virtual environment and install dependencies.**

```
scripts/build_env.sh
```

This would be a good time to grab a coffee or tea. This step takes a few minutes to run. This step does not need to be repeated on notebook restart (see [Restarting the notebook](#restarting-the-notebook)).

**4. Combine relevant files into single source directory for SageMaker.**

This will combine all of the training and inference code in a single source directory and create a model.tar.gz file for inference with a pre-trained model.

```
scripts/set_up_sagemaker.sh
```

## Training (Optional)

Opon the notebook named [notebooks/pytorch_training.ipynb](notebooks/pytorch_smdataparallel_tsp_demo.ipynb) to see how to train on multiple GPU nodes on SageMaker. 

Note that this step is optional.

To run training you need to have 18-19 GB of available disk space on your notebook instance to download the training data.

## Inference 

Open the notebook titled [notebooks/pytorch_inference.ipynb](notebooks/pytorch_inference.ipynb) to see how to run inference in three different ways:

1. Locally on the notebook instance
2. SageMaker Endpoint
3. Batch Transform

## Streamlit Demo

**1. Update the Jupyter Notebook instance environment for hosting streamlit.**

```
scripts/set_up_streamlit.sh
```

**2. Run the steamlit app.**

```
WORKING_DIR=./.myenv
# get the env name
line=$(head -n 1 environment.yml)
ENV_NAME="${line/name:\ /}"
source "$WORKING_DIR/miniconda/bin/activate"
conda activate $ENV_NAME

streamlit run src/streamlit_demo.py
```

**3. View the streamlit app via a browser.**

Go to `https://$YourInstance$.notebook.$YourRegion$.sagemaker.aws/proxy/8501/`

![2021-08-11-routing-blog-demo-2-low](https://user-images.githubusercontent.com/6405428/131402564-3dd1ac21-4566-42c8-9b20-3e218b92b333.gif)

## Restarting the notebook

After you start/stop a SageMaker notebook instance, you do not need to re-install the packages. Simply open a SageMaker terminal session and run:

```
cd SageMaker/amazon-sagemaker-tsp-deep-rl
scripts/start_env.sh
```

## Acknowledgements

This code base is an extension of Chaitanya Joshi's excellent repo [learning-tsp](https://github.com/chaitjo/learning-tsp).

For additional detail check out the paper (Joshi et al., 2021): [Learning TSP Requires Rethinking Generalization](https://arxiv.org/abs/2008.07054).

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This code is licensed under the MIT-0 License. See the LICENSE file.

This code downloads and installs Miniconda. See here for the [end-user-license-agreement](miniconda-eula.txt).

## Authors

* [Yin Song](https://github.com/yinsong1986)
* [Chen Wu](https://github.com/chenwuperth)
* [Josiah Davis](https://github.com/josiahdavis)
* [Eden Duthie](https://github.com/edenduthie)
