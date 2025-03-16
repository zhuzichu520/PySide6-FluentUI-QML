import os

import py7zr


# noinspection PyPep8Naming
def zipFolder(folderPath: str, outputPath: str, password=None, excludeFolders=None, excludeFiles=None):
    if not excludeFolders:
        excludeFolders = []
    if not excludeFiles:
        excludeFiles = []
    with py7zr.SevenZipFile(outputPath, 'w', password=password) as zipf:
        for root, dirs, files in os.walk(folderPath):
            dirs[:] = [d for d in dirs if d not in excludeFolders]
            for file in files:
                if file not in excludeFiles:
                    filePath = os.path.join(root, file)
                    zipf.write(filePath)


if __name__ == "__main__":
    zipFolder("./FluentUI", "./source.zip", "zhuzichu988", ["__pycache__"], ["resource_rc.py"])
    zipFolder("./", "./source_all.zip", "zhuzichu988", [".git", "venv", "__pycache__", "dist", "build"], ["resource_rc.py", "source.zip", "source_all.zip"])
