import os
import shutil
import time
from datetime import datetime

desktop_path = os.path.expanduser("~/Desktop")
organized_folder = os.path.join(desktop_path, "Organized")
folders_by_type = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".doc", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Others": []
}

def create_folders():
    """Create folders for organization."""
    if not os.path.exists(organized_folder):
        os.makedirs(organized_folder)
    for folder in folders_by_type.keys():
        folder_path = os.path.join(organized_folder, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def move_files():
    """Move files from desktop to appropriate folders."""
    files = [f for f in os.listdir(desktop_path) if os.path.isfile(os.path.join(desktop_path, f))]
    for file in files:
        file_path = os.path.join(desktop_path, file)
        file_ext = os.path.splitext(file)[1].lower()

      
        moved = False
        for folder, extensions in folders_by_type.items():
            if file_ext in extensions:
                shutil.move(file_path, os.path.join(organized_folder, folder, file))
                moved = True
                break

        if not moved:
            shutil.move(file_path, os.path.join(organized_folder, "Others", file))



if __name__ == "__main__":
    print("Organizing your desktop...")
    create_folders()
    move_files()
    print("Desktop organized successfully!")
