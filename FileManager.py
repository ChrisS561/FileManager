import os
import shutil
from pathlib import Path

os.chdir('/Users/chris/Downloads')

# Finds all duplicate files in a folder
def find_duplicates(folder):
    seen = {}
    duplicates = []

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            if file_size in seen:
                if file_path not in duplicates:
                    duplicates.append(file_path)
            else:
                seen[file_size] = file_path

    return duplicates

# Finds all duplicate files in a folder and removes them
download_folder = ["/Users/chris/Downloads/PDF", "/Users/chris/Downloads/Images", "/Users/chris/Downloads/Videos", "/Users/chris/Downloads/Documents",
                   "/Users/chris/Downloads/Compressed", "/Users/chris/Downloads/Audio", "/Users/chris/Downloads/Applications", "/Users/chris/Downloads/Text", "/Users/chris/Downloads/Code"]
# download_folder = ["/Users/chris/Downloads"]
for folder in download_folder:
    duplicate_files = find_duplicates(folder)
    if len(duplicate_files) > 0:
        # for file in duplicate_files:
        #     os.remove(file)
        # print(f"Duplicate files removed from {folder}:")
        print(f"Duplicate files found in {folder}:")
        for file in duplicate_files:
            print(file)
    else:
        print(f"No duplicate files found in {folder}.")



print("------------------------------------------------------------------------------------------------------------------------")
# # Moves all PDF files to a folder called PDF
# for file in os.listdir():
#     if file.endswith('.pdf'):
#         shutil.move(file, "PDF")

#     # Moves all JPG, PNG, JPEG, and GIF files to a folder called Images
#     if file.endswith(('.jpg', '.png', '.jpeg', '.JPG', '.PNG', '.JPEG', '.gif', '.GIF', 'heic', 'HEIC', 'heif', 'HEIF')):
#         shutil.move(file, "Images")

#     # Moves all MP4, MOV, and M4V files to a folder called Videos
#     if file.endswith(('.mp4', '.mov', '.m4v', '.MP4', '.MOV', '.M4V', '.avi', '.AVI', '.mkv', '.MKV', '.wmv', '.WMV')):
#         shutil.move(file, "Videos")

#     # Moves all DOC, DOCX, PPT, PPTX, XLS, XLSX, and PAGES files to a folder called Documents
#     if file.endswith(('.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.pages', '.DOC', '.DOCX', '.PPT', '.PPTX', '.XLS', '.XLSX', '.PAGES')):
#         shutil.move(file, "Document")

#     # Moves all ZIP, RAR, and 7Z files to a folder called Compressed
#     if file.endswith(('.zip', '.rar', '.7z', '.ZIP', '.RAR', '.7Z')):
#         shutil.move(file, "Compressed")

#     # Moves all MP3, M4A, WAV, and FLAC files to a folder called Audio
#     if file.endswith(('.mp3', '.m4a', '.wav', '.flac', '.MP3', '.M4A', '.WAV', '.FLAC')):
#         shutil.move(file, "Audio")

#     # Moves all EXE, DMG, and APP files to a folder called Applications
#     if file.endswith(('.exe', '.dmg', '.app', '.EXE', '.DMG', '.APP')):
#         shutil.move(file, "Applications")

#     # Moves all TXT, RTF, and HTML files to a folder called Text
#     if file.endswith(('.txt', '.rtf', '.html', '.TXT', '.RTF', '.HTML')):
#         shutil.move(file, "Text")

#     # Moves all Java, Bash, Python, C and C++ files to a folder called Code
#     if file.endswith(('.java', '.bash', '.py', '.c', '.cpp', '.JAVA', '.BASH', '.PY', '.C', '.CPP')):
#         shutil.move(file, "Code")
