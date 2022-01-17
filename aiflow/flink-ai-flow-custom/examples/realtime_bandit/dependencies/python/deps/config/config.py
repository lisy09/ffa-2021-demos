import os
from typing import Dict
import yaml

def load_project_config() -> Dict:
    config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
    with open(config_path) as f:
        yaml_config = yaml.load(f, Loader=yaml.FullLoader)
    return yaml_config