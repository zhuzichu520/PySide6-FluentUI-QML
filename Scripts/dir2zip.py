import zipfile
import sys
import os

def exec():
    if len(sys.argv) < 2:
        print("error paramter")
        return
    arguments = sys.argv[1:]
    folder_to_compress = arguments[0]
    zip_filename = arguments[1]
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_to_compress):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_to_compress))
        print(f'{zip_filename} is created')

if __name__ == '__main__':
    exec()