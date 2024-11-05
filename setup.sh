#!/bin/bash

# 환경 이름 설정
ENV_NAME="py10"

# Conda 환경 생성
# Conda 자체가 잡히지 않을 때 절대 경로로 지정해준다. 
echo "Creating Conda environment: $ENV_NAME with Python 3.10..."
/Users/imseohyeon/Documents/code/bin/conda create -n $ENV_NAME python=3.10 -y

# Conda 환경 활성화
echo "Activating environment: $ENV_NAME..."
source /Users/imseohyeon/Documents/code/bin/activate $ENV_NAME

# pip 설치 및 설정
echo "Installing pip and configuring pip interop..."
/Users/imseohyeon/Documents/code/bin/conda install -c anaconda pip -y
/Users/imseohyeon/Documents/code/bin/conda config --set pip_interop_enabled true

# Conda로 basemap_data_hires 설치
echo "Installing basemap_data_hires using conda..."
/Users/imseohyeon/Documents/code/bin/conda install -c conda-forge basemap-data-hires -y

# requirements.txt 설치
pip install -r requirements.txt

# 완료 메시지 출력
echo "Environment setup complete. To deactivate, use 'conda deactivate'."
