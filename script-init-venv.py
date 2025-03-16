import subprocess
import sys

import env

if __name__ == "__main__":
    subprocess.run([sys.executable, "-m", "venv", "venv"])
    subprocess.run([env.pip(), "install", "PySide6==6.7.2"])
    subprocess.run([env.pip(), "install", "nuitka"])
    subprocess.run([env.pip(), "install", "PyInstaller"])
    subprocess.run([env.pip(), "install", "qasync"])
    subprocess.run([env.pip(), "install", "aiohttp"])
    subprocess.run([env.pip(), "install", "qrcode"])
    subprocess.run([env.pip(), "install", "Image"])
    subprocess.run([env.pip(), "install", "keyboard"])
    subprocess.run([env.pip(), "install", "PyOpenGL"])
    subprocess.run([env.pip(), "install", "py7zr"])
