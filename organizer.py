import os
import shutil
import json

def load_config():
    if not os.path.exists('config.json'):
        print("Error: config.json not found.")
        return None
    with open('config.json', 'r') as f:
        return json.load(f)

def run_organizer():
    # Get desktop path
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    rules = load_config()
    
    if not rules:
        return

    # Files to stay on desktop
    exclude = ["organizer.py", "config.json", "README.md"]

    for file in os.listdir(desktop):
        file_path = os.path.join(desktop, file)

        if os.path.isdir(file_path) or file in exclude:
            continue

        # Get extension
        ext = os.path.splitext(file)[1].lower()
        
        # Find category
        target_folder = "Other"
        for folder, extensions in rules.items():
            if ext in extensions:
                target_folder = folder
                break

        dest_path = os.path.join(desktop, target_folder)
        
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

        try:
            shutil.move(file_path, os.path.join(dest_path, file))
            print(f"Moved: {file} -> {target_folder}")
        except Exception as e:
            print(f"Error moving {file}: {e}")

if __name__ == "__main__":
    print("Desktop Organizer is running...")
    run_organizer()
    print("Done.")