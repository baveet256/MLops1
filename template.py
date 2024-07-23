import os
from pathlib import Path
files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/data_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/utils.py",
    "src/utils/__init__.py",
    "src/logger/logging.py",
    "src/exception/exceptions.py",
    "test/unit/__init__.py",
    "test/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"  
]

for i in files:
    file_path = Path(i)
    filedir,filename = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(file_path)):
        with open(file_path,'w') as f:
            pass ## creates the file!!!!

