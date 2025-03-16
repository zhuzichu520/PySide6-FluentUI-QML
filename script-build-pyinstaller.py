import shutil
import os
import subprocess

import env

if __name__ == "__main__":
    buildDir = os.path.join('.', 'build')
    distDir = os.path.join('.', 'dist')
    try:
        shutil.rmtree(buildDir)
        shutil.rmtree(distDir)
    except FileNotFoundError:
        pass
    subprocess.run([env.python(), os.path.join('.', 'script-zip-source.py')])
    subprocess.run([env.python(), os.path.join('.', 'script-update-translations.py')])
    subprocess.run([env.python(), os.path.join('.', 'script-update-resource.py')])
    subprocess.run([env.pyinstaller(), "-y", os.path.join('.', 'main.spec')], env=env.environment())
