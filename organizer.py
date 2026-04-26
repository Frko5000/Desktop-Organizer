import os
import shutil
import json

def load_config():
    if not os.path.exists('config.json'):
        print("Error: config.json not found!")
        return None
    with open('config.json', 'r') as f:
        return json.load(f)

def run_organizer():
    user_home = os.path.expanduser("~")
    desktop_path = os.path.join(user_home, "Desktop")
    onedrive_path = os.path.join(user_home, "OneDrive", "Desktop")
    
    if os.path.exists(onedrive_path):
        desktop_path = onedrive_path

    print(f"Target path: {desktop_path}")
    
    config = load_config()
    if not config:
        return

    exclude = ["organizer.py", "config.json", "README.md", "desktop.ini"]
    counter = 0

    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)

        if os.path.isdir(item_path) or item in exclude:
            continue

        extension = os.path.splitext(item)[1].lower()
        
        target_folder = "Other"
        for folder, extensions in config.items():
            if extension in extensions:
                target_folder = folder
                break

        dest_dir = os.path.join(desktop_path, target_folder)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        try:
            shutil.move(item_path, os.path.join(dest_dir, item))
            print(f"Moved: {item} -> {target_folder}")
            counter += 1
        except Exception as e:
            print(f"Could not move {item}: {e}")

    print(f"\nDone! {counter} files organized.")

if __name__ == "__main__":
    run_organizer()
