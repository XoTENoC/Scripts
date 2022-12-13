import os
import shutil

# Set the path to the Downloads folder
downloads_path = "C:\\Users\\[username]\\Downloads"

# Set the path to the folder where you want to move the files
destination_path = "C:\\Users\\[username]\\SortedFiles"

# Set the file extensions and corresponding destination folders
file_extensions = {
    ".exe": "Installers",
    ".jpg": "Pictures",
    ".mp3": "Music"
}

# Loop through all files in the Downloads folder
for filename in os.listdir(downloads_path):
    # Get the file extension
    file_ext = os.path.splitext(filename)[1]

    # Check if the file extension is in the file_extensions dictionary
    if file_ext in file_extensions:
        # Get the destination folder for this file extension
        dest_folder = file_extensions[file_ext]

        # Create the destination folder if it doesn't exist
        if not os.path.exists(os.path.join(destination_path, dest_folder)):
            os.makedirs(os.path.join(destination_path, dest_folder))

        # Move the file to the destination folder
        shutil.move(os.path.join(downloads_path, filename), os.path.join(destination_path, dest_folder, filename))
