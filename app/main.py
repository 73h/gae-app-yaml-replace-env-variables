import os


def replace_env_variables_in_app_yaml_file():
    github_workspace = os.environ.get("GITHUB_WORKSPACE")
    app_yaml_path = os.environ.get("INPUT_APP_YAML_PATH")

    yaml_file_path = os.path.join(github_workspace, app_yaml_path)

    print(f"open {yaml_file_path}")
    yaml_file = open(yaml_file_path, "r+")
    yaml = yaml_file.read()

    print(os.environ.get("VAR_ONE"))

    # yaml_file.write(yaml)
    yaml_file.close()

    test = open(yaml_file_path, "r")
    # print(test.read())


if __name__ == "__main__":
    replace_env_variables_in_app_yaml_file()
