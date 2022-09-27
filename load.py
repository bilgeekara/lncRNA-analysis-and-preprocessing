def load_json(path):
    """
    Load json data as a distionary
    """

    with open(path) as f:
        file = f.read()
    file = json.loads(file)

    return file
