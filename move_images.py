import os
import shutil

# Source folder (where images are now)
source_folder = "."

# Destination folder (where images will move)
destination_folder = "moved_images"

# Loop through all files
for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)
        print(f"Moved: {file}")

print("All JPG files moved successfully!")