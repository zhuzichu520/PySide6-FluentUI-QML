import subprocess
import sys

import env

if __name__ == "__main__":
    subprocess.run([sys.executable, "-m", "venv", "venv"])
    subprocess.run([env.pip(), "install", "PySide6==6.7.2"])
    subprocess.run([env.pip(), "install", "nuitka==2.3.2"])
    subprocess.run([env.pip(), "install", "PyInstaller==6.8.0"])
    subprocess.run([env.pip(), "install", "qasync==0.27.1"])
    subprocess.run([env.pip(), "install", "aiohttp==3.11.8"])
    subprocess.run([env.pip(), "install", "qrcode==7.4.2"])
    subprocess.run([env.pip(), "install", "pillow==10.4.0"])
    subprocess.run([env.pip(), "install", "keyboard==0.13.5"])
    subprocess.run([env.pip(), "install", "PyOpenGL==3.1.7"])
    subprocess.run([env.pip(), "install", "py7zr==0.22.0"])
