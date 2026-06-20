import os
import shutil

# Source and destination folders
source_folder = "SourceFolder"
destination_folder = "DestinationFolder"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Move all JPG files
for file_name in os.listdir(source_folder):
    if file_name.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        shutil.move(source_path, destination_path)
        print("Moved:", file_name)

print("All JPG files moved successfully!")