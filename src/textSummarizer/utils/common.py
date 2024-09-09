import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads YAML File and returns ConfigBox Object

    Args:   
        path_to_yaml: path to the YAML file         

    Returns:
        ConfigBox: Configuration Box object with YAML file contents 

    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info("yaml parsed")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Invalid YAML file")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    create list of directories
    Args:
        path_to_directories: list of path of directories
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size in KB
    Args:
        path: path of the file
    """
    size_in_kb = round(os.path.getsize(path)/1024, 2)
    return str(size_in_kb) + "KB"