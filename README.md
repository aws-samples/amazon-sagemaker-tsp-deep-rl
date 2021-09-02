# Solving the Travelling Salesperson Problem with deep reinforcement learning on Amazon SageMaker

This repository includes the code for the AWS Open Source blog: [Solving the Travelling Salesperson Problem with deep reinforcement learning on Amazon SageMaker](.)

For additional detail check out the paper (Joshi et al., 2021): [Learning TSP Requires Rethinking Generalization](https://arxiv.org/abs/2008.07054).

## Getting Started

1. Create a SageMaker notebook instance

This repository is meant to be run on a SageMaker notebook instance. 

See the [aws documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/howitworks-create-ws.html) for additional  details.

2. Clone the repository with submodule.

This will clone the current repository as well as the submodule repository: [learning-tsp](https://github.com/chaitjo/learning-tsp).

```
git clone --recurse-submodules https://github.com/aws-samples/amazon-sagemaker-tsp-deep-rl.git
```

3. Combine relevant files into single source directory for SageMaker.

SageMaker requires the specification of a single source directory for training and inference as well as a tar.gz file.
```
./set_up_sagemaker.sh
```



## Training (Optional)

How to train on multiple GPU nodes on SageMaker. 

This step is optional.

To run training you need to have 18-19 GB of available disk space on your notebook instance to download the training data.

[pytorch_training.ipynb](pytorch_smdataparallel_tsp_demo.ipynb)

## Inference 

How to run inference in three different ways:
1. Locally on the notebook instance
2. SageMaker Endpoint 
3. Batch Transform

[pytorch_inference.ipynb](pytorch_inference.ipynb)

## Streamlit Demo

1. Update the Jupyter Notebook instance environment for hosting streamlit.

    `set_up_streamlit.sh`
    
2. Build the conda python environment for the streamlit app

    `./build_env.sh`

3. Run the steamlit app

    ```
    WORKING_DIR=./.myenv
    # get the env name
    line=$(head -n 1 environment.yml)
    ENV_NAME="${line/name:\ /}"
    source "$WORKING_DIR/miniconda/bin/activate"
    conda activate $ENV_NAME
    
    streamlit run streamlit_demo.py
    ```

4. View the streamlit app via a browser at https://$YourInstance$.notebook.$YourRegion$.sagemaker.aws/proxy/8501/

![2021-08-11-routing-blog-demo-2-low](https://user-images.githubusercontent.com/6405428/131402564-3dd1ac21-4566-42c8-9b20-3e218b92b333.gif)


## Acknowledgements

This code base is an extension of Chaitanya Joshi's excellent repo [learning-tsp](https://github.com/chaitjo/learning-tsp).

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This code is licensed under the MIT-0 License. See the LICENSE file.

This code downloads and installs Miniconda. See here for the [end-user-license-agreement](miniconda-eula.txt).
