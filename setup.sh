#!/bin/bash

# 환경 이름 설정
ENV_NAME="py11"
CONDA_PATH="/home/ish/anaconda3/bin/conda"

# Conda 환경 생성
echo "Creating Conda environment: $ENV_NAME with Python 3.10..."
$CONDA_PATH create -n $ENV_NAME python=3.10 -y || { echo "Error creating Conda environment"; exit 1; }

# Conda 환경 활성화
echo "Activating environment: $ENV_NAME..."
source /home/ish/anaconda3/etc/profile.d/conda.sh  # Conda 명령 사용을 위한 설정
conda activate $ENV_NAME || { echo "Error activating environment"; exit 1; }

# pip 설치 및 설정
echo "Installing pip and enabling pip interoperability..."
$CONDA_PATH install -c anaconda pip -y || echo "Error installing pip"
$CONDA_PATH config --set pip_interop_enabled true

# Conda 패키지 설치
echo "Installing additional packages with Conda..."

# wrf-python 및 basemap-data-hires 설치
$CONDA_PATH install -c conda-forge wrf-python -y || echo "Error installing wrf-python"
$CONDA_PATH install -c conda-forge basemap-data-hires -y || echo "Error installing basemap-data-hires"

# gfortran, netcdf4 및 ncview 설치
$CONDA_PATH install -c conda-forge gfortran -y || echo "Error installing gfortran"
$CONDA_PATH install -c conda-forge netcdf4 ncview -y || echo "Error installing netcdf4 or ncview"

# pip 관련 패키지 설치 및 캐시 정리
echo "Upgrading setuptools, pip, and wheel..."
pip install --upgrade --force-reinstall setuptools || echo "Error upgrading setuptools"
pip install --upgrade pip wheel || echo "Error upgrading pip and wheel"
pip cache purge || echo "Error purging pip cache"

# requirements.txt 설치
echo "Installing packages from requirements.txt..."
pip install -r DataProcessing_TRC/requirements.txt || echo "Error installing packages from requirements.txt"

# 완료 메시지 출력
echo "Environment setup complete. To deactivate, use 'conda deactivate'."
