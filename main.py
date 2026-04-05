import os
import sys
from scanner import scan_path
from core import load_hashes, save_hashes, compare_hashes
from utils import clean_path, validate_path


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: python main.py scan <path>")
        sys.exit()

    command = sys.argv[1]

    if command != "scan":
        print("Invalid command. Use: scan")
        sys.exit()

    # 🔹 Clean path
    path = clean_path(sys.argv[2])

    if not validate_path(path):
        print("Invalid path! Path does not exist.")
        sys.exit()

    # 🔹 Determine scan type
    is_file_scan = os.path.isfile(path)

    if is_file_scan:
        tracking_key = os.path.dirname(path) or "."
    else:
        tracking_key = path

    # 🔹 Load database
    database = load_hashes()
    old_hashes = database.get(tracking_key, {})

    # 🔹 Scan
    new_hashes = scan_path(path)

    # 🟢 First scan → baseline
    if not old_hashes:
        database[tracking_key] = new_hashes
        save_hashes(database)
        print("Initial scan completed. Baseline created ✅")
        sys.exit()

    # 🔹 Compare
    modified, new_files, deleted = compare_hashes(old_hashes, new_hashes, is_file_scan)

    # 🔹 No changes
    if not (modified or new_files or deleted):
        print("No changes detected")
        sys.exit()

    # 🔹 Show grouped output
    if modified:
        print("\nModified files:")
        for f in modified:
            print(f" - {f}")

    if new_files:
        print("\nNew files:")
        for f in new_files:
            print(f" - {f}")

    if deleted:
        print("\nDeleted files:")
        for f in deleted:
            print(f" - {f}")

    # 🔹 Auto-add new files without prompt
    is_new_file = False
    if is_file_scan:
        for f in new_hashes:
            if f not in old_hashes:
                is_new_file = True

    if is_new_file:
        updated_hashes = old_hashes.copy()
        updated_hashes.update(new_hashes)

        database[tracking_key] = updated_hashes
        save_hashes(database)

        print("\nNew file added to baseline ✅")
        sys.exit()

    # 🔥 Ask user only for modifications
    choice = input("\nUpdate changes in database? (y/n): ").lower()

    if choice == "y":
        if is_file_scan:
            updated_hashes = old_hashes.copy()
            updated_hashes.update(new_hashes)
        else:
            updated_hashes = new_hashes

        database[tracking_key] = updated_hashes
        save_hashes(database)

        print("Database updated ✅")
    else:
        print("Changes ignored ❌")