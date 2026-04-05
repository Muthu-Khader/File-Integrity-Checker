import json


def load_hashes():
    try:
        with open("database.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_hashes(data):
    with open("database.json", "w") as f:
        json.dump(data, f, indent=4)


def compare_hashes(old, new, is_file_scan):
    modified = []
    new_files = []
    deleted = []

    if is_file_scan:
        for file in new:
            if file not in old:
                new_files.append(file)
            elif old[file] != new[file]:
                modified.append(file)
        return modified, new_files, deleted

    # Folder scan
    for file in old:
        if file not in new:
            deleted.append(file)
        elif old[file] != new[file]:
            modified.append(file)

    for file in new:
        if file not in old:
            new_files.append(file)

    return modified, new_files, deleted