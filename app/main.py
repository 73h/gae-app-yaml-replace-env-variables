import os

if __name__ == "__main__":
    github_workspace = os.environ.get("GITHUB_WORKSPACE")
    app_yaml_path = os.environ.get("INPUT_APP_YAML_PATH")

    yaml_file_path = os.path.join(github_workspace, app_yaml_path)
    print(yaml_file_path)

    yaml_file = open(yaml_file_path, "r")
    print(yaml_file.read())
   