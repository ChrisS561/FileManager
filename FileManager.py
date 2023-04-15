import os
import shutil
from pathlib import Path

os.chdir('/Users/chris/Downloads')


# Moves all PDF files to a folder called PDF
for file in os.listdir():
    if file.endswith('.pdf'):
        shutil.move(file, "PDF")

    # Moves all JPG, PNG, JPEG, and GIF files to a folder called Images
    if file.endswith(('.jpg', '.png', '.jpeg', '.JPG', '.PNG', '.JPEG', '.gif', '.GIF', 'heic', 'HEIC', 'heif', 'HEIF')):
        shutil.move(file, "Images")
    
    # Moves all MP4, MOV, and M4V files to a folder called Videos
    if file.endswith(('.mp4', '.mov', '.m4v', '.MP4', '.MOV', '.M4V', '.avi', '.AVI', '.mkv', '.MKV', '.wmv', '.WMV')):
        shutil.move(file, "Videos")
    
    # Moves all DOC, DOCX, PPT, PPTX, XLS, XLSX, and PAGES files to a folder called Documents
    if file.endswith(('.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.pages', '.DOC', '.DOCX', '.PPT', '.PPTX', '.XLS', '.XLSX', '.PAGES')):
        shutil.move(file, "Document")
    
    # Moves all ZIP, RAR, and 7Z files to a folder called Compressed
    if file.endswith(('.zip', '.rar', '.7z', '.ZIP', '.RAR', '.7Z')):
        shutil.move(file, "Compressed")
    
    # Moves all MP3, M4A, WAV, and FLAC files to a folder called Audio
    if file.endswith(('.mp3', '.m4a', '.wav', '.flac', '.MP3', '.M4A', '.WAV', '.FLAC')):
        shutil.move(file, "Audio")
        
    # Moves all EXE, DMG, and APP files to a folder called Applications
    if file.endswith(('.exe', '.dmg', '.app', '.EXE', '.DMG', '.APP')):
        shutil.move(file, "Applications")
    
    # Moves all TXT, RTF, and HTML files to a folder called Text
    if file.endswith(('.txt', '.rtf', '.html', '.TXT', '.RTF', '.HTML')):
        shutil.move(file, "Text")
    
    # Moves all Java, Bash, Python, C and C++ files to a folder called Code
    if file.endswith(('.java', '.bash', '.py', '.c', '.cpp', '.JAVA', '.BASH', '.PY', '.C', '.CPP')):
        shutil.move(file, "Code")

