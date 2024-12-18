#!/bin/sh

echo "Starting installation ..."
eval "$(conda shell.bash hook)"
py_env="parkinsons-env"
conda create --name $py_env python=3.10 -y
conda activate $py_env

pip install -r requirements.txt

echo "Setup done. Execute:-"
echo "conda activate $py_env"