import os
import shutil

# Specify the directory where the files are located
downloads_dir = "C:\\Users\\<username>\\Downloads"

# Create a list of file types to classify
file_types = {
    "installers": [".exe", ".msi"],
    "pictures": [".jpg", ".jpeg", ".png", ".gif"],
    "documents": [".pdf", ".doc", ".docx", ".txt"]
}

# Loop through all the files in the downloads directory
for filename in os.listdir(downloads_dir):
    # Get the file extension of the current file
    file_ext = os.path.splitext(filename)[1]
    
    # Loop through the file types to find a match
    for file_type, extensions in file_types.items():
        # If the file extension matches one of the extensions for this file type
        if file_ext in extensions:
            # Create the directory for this file type if it doesn't already exist
            if not os.path.exists(os.path.join(downloads_dir, file_type)):
                os.makedirs(os.path.join(downloads_dir, file_type))
            
            # Move the file to the correct directory
            shutil.move(os.path.join(downloads_dir, filename), os.path.join(downloads_dir, file_type, filename))
            break
