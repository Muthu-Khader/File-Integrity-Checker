import os


def clean_path(path):
    path = path.strip('"')
    path = os.path.normpath(path)
    path = path.rstrip("\\/")
    return path


def validate_path(path):
    return os.path.exists(path)

