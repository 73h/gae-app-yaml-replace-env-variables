import os

if __name__ == "__main__":

    print("start")

    files = os.listdir('/github/workspace')
    for f in files:
        print(str(f))

    print("##########")

    # yaml_file_path = "/github/workspace/" + os.environ.get("app_yaml_path")
    # print(yaml_file_path)

    """
    yaml_file = open(os.environ.get("app_yaml_path"), "r")
    print(yaml_file.read())
    """
