source /home/ec2-user/anaconda3/bin/activate JupyterSystemEnv
pip uninstall --yes nbserverproxy
pip install --upgrade jupyter-server-proxy
sudo systemctl restart jupyter-server
