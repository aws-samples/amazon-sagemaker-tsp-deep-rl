# Getting Started

## Distributed Training (Optional)

[pytorch_smdataparallel_tsp_demo.ipynb](pytorch_smdataparallel_tsp_demo.ipynb)

## Inference (Local, Endpoint and Batch Transform)

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

![Streamlit Demo](pics/2021-08-11-routing-blog-demo-2-low.gif)


## Acknowledgements

This code base is an extension of Chaitanya Joshi's excellent repo [learning-tsp](https://github.com/chaitjo/learning-tsp).

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
