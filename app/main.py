
import os

import ruamel.yaml

yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True


def replace_env_variables_in_app_yaml_file():
    github_workspace = os.environ.get("GITHUB_WORKSPACE")
    app_yaml_path = os.environ.get("INPUT_APP_YAML_PATH")

    yaml_file = os.path.join(github_workspace, app_yaml_path)

    with open(yaml_file, "r") as stream:
        yaml_data = yaml.safe_load(stream)

    if "env_variables" not in yaml_data:
        raise Exception("cannot find the \"env_variables\" section in yaml-file")

    for key in yaml_data["env_variables"]:
        env_var = yaml_data["env_variables"][key]
        if env_var.startswith("$"):
            repl_env_var = os.environ.get(env_var[1:])
            if repl_env_var is not None:
                yaml_data["env_variables"][key] = repl_env_var
            else:
                raise Exception(f"cannot find the env-variable {env_var[1:]} in \"env\" section in github workflow")

    with open(yaml_file, "w") as stream:
        yaml.dump(yaml_data, stream, width=float("inf"))


if __name__ == "__main__":
    replace_env_variables_in_app_yaml_file()