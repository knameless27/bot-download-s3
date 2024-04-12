import json
import os

def load_env(data):
    # print(data)
    env_path = "./env.json"
    env = {}

    if os.path.exists(env_path) and data == {}:
        with open(env_path, "r") as file:
            env = json.load(file)
    else:
        # print("entra")
        with open(env_path, "w") as env_file:
            json.dump(data, env_file)

        with open(env_path, "r") as env_file:
            env = json.load(env_file)

    return env
