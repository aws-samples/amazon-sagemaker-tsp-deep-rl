source /home/ec2-user/anaconda3/bin/activate JupyterSystemEnv
pip uninstall --yes nbserverproxy
pip install --upgrade jupyter-server-proxy
sudo initctl restart jupyter-server --no-wait
