import os

# Get directory of all's files to organize
input_directory = os.getcwd() + '\\input'
output_directory = os.getcwd() + '\\output'

# All extensions of files in input directory and their respectives folders
file_ext = {
    "pdf": "PDFs",
    "png": "Images",
    "jpg": "Images",
    "jpeg": "Images",
    "gif": "Images",
    "doc": "Documents",
    "docx": "Documents",
    "txt": "Documents",
    "csv": "Data",
    "xlsx": "Data",
    "zip": "Archives",
    "rar": "Archives",
    "7z": "Archives",
    "exe": "Executables",
    "mp3": "Music",
    "wav": "Music",
    "mp4": "Videos",
    "avi": "Videos",
    "wmv": "Videos"
}



try:
    files = os.listdir(input_directory) # Get all files
    for file in files:
        # Get extension file for each file
        extension = file.split('.')[-1]
        
        # Get your folder
        folder = file_ext[extension]
        
        # Move archiver to correct folder
        os.replace(input_directory + f"\\{file}", output_directory + f"\\{folder}\\{file}")
except Exception as e:
    print(f"Error: {e}")
    exit()
    
print("Files Moved Successfully!")