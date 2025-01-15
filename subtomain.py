import os
import shutil

# Main folder path
main_folder = r"C:\Users\PMLS\Downloads\Compressed\25_05_22\25_05_22\Ground_Multispectral_Photos\Healthy"

# Get list of all files in subfolders
for root, dirs, files in os.walk(main_folder):
    for file in files:
        # Get the full path of the file
        file_path = os.path.join(root, file)
        
        # Check if the file is not in the main folder
        if root != main_folder:
            # Check if the file already exists in the main folder
            if os.path.exists(os.path.join(main_folder, file)):
                # Replace existing file with new one
                shutil.move(file_path, os.path.join(main_folder, file))
                print(f"Replaced {file} in {main_folder}")
            else:
                # Move the file to the main folder
                shutil.move(file_path, main_folder)
                print(f"Moved {file} to {main_folder}")

# Remove empty subfolders
for root, dirs, files in os.walk(main_folder, topdown=False):
    for dir in dirs:
        folder_path = os.path.join(root, dir)
        # Remove the folder if it's empty
        if not os.listdir(folder_path):
            os.rmdir(folder_path)
            print(f"Removed empty folder: {folder_path}")
