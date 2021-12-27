import os

import yaml


def replace_env_variables_in_app_yaml_file():
    github_workspace = os.environ.get("GITHUB_WORKSPACE")
    app_yaml_path = os.environ.get("INPUT_APP_YAML_PATH")

    yaml_file_path = os.path.join(github_workspace, app_yaml_path)

    print(f"open and read {yaml_file_path}")
    yaml_file = open(yaml_file_path, "r")
    content = yaml.full_load(yaml_file.read())
    yaml_file.close()

    if "env_variables" in content:
        env_variables = content["env_variables"]
    else:
        raise Exception("cannot find the \"env_variables\" section in yaml-file")

    for key in env_variables:
        env_var = env_variables[key]
        if env_var.startswith("$"):
            repl_env_var = os.environ.get(env_var[1:])
            if repl_env_var is not None:
                content["env_variables"][key] = repl_env_var
            else:
                raise Exception(f"cannot find the env-variable {key} in \"env\" section in github action workflow")
        pass

    yaml_file = open(yaml_file_path, "w")
    yaml.dump(content, yaml_file)
    yaml_file.close()

    test = open(yaml_file_path, "r")
    print(test.read())
    yaml_file.close()


if __name__ == "__main__":
    replace_env_variables_in_app_yaml_file()
