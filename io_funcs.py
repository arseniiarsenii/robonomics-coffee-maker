from hashlib import sha256
import yaml
import typing as tp


# load up the configuration file
def read_config() -> tp.Dict[str:str]:
    with open("config.yaml", "r") as file:
        try:
            return yaml.safe_load(file)["config"]
        except Exception as E:
            print(f"Error loading config.yaml: {E}")
            return {}


# load up the allow list
def read_allow_list() -> tp.List[str]:
    with open("allow_list.yaml", "r") as file:
        try:
            return yaml.safe_load(file)["allowed_ids"]
        except Exception as E:
            print(f"Error loading allow_list.yaml: {E}")
            return []


# get an sha256 checksum of the allow_list.yaml file
def allow_list_hash() -> str:
    with open("allow_list.yaml", "r") as file:
        allow_list_bytes = file.read()
        check_sum = sha256(allow_list_bytes).hexdigest()
        return check_sum


# todo
# gets the latest hash for an allow list from robonomics network
def get_robonomics_hash() -> str:
    pass