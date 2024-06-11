import os
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name='cnnClassifier'

list_of_files= [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/components/data_ingestion.py',
    f'src/{project_name}/components/base_model.py',
    f'src/{project_name}/components/model_trainer.py',
    f'src/{project_name}/components/model_evaluation.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/pipeline/data_ingestion.py',
    f'src/{project_name}/pipeline/base_model.py',
    f'src/{project_name}/pipeline/model_trainer.py',
    f'src/{project_name}/pipeline/model_evaluation.py',
    'setup.py',
    'params.yaml',
    'main.py',
    'dvc.yaml',
    'requirements.txt',
    'DOCKER',
    'research/trials.ipynb',
    ]

for filepath in list_of_files:

    filepath=Path(filepath)
    filedir,filename =os.path.split(filepath)

    if filedir !='':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'creating directory; {filedir} for the file: {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:

            pass
            logging.info(f'creating empty file:{filepath}')

    else:
        logging.info(f'{filename} already exists')
