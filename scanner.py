import os
from hash_utils import get_hash


def scan_path(path):
    file_hashes = {}

    if os.path.isfile(path):
        try:
            file_path = os.path.normpath(path)
            file_hashes[file_path] = get_hash(file_path)
        except Exception as e:
            print(f"Error reading {path}: {e}")
        return file_hashes

    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                
                file_path = os.path.normpath(os.path.join(root, file))
                try:
                    file_hashes[file_path] = get_hash(file_path)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
        print(root,dirs,files)
        return file_hashes

    else:
        print("Invalid path!")
        return {}
    
