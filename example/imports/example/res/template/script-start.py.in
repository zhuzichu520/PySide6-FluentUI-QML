import subprocess
import sys
import os

import env

if __name__ == "__main__":
    isFast = False
    args = sys.argv
    if len(args) >= 2:
        if "fast" in args[1:]:
            isFast = True
    if not isFast:
        subprocess.run([env.python(), os.path.join('.', 'script-update-translations.py')])
        subprocess.run([env.python(), os.path.join('.', 'script-update-resource.py')])
    subprocess.run([env.python(), os.path.join('.', env.projectName, 'main.py')], env=env.environment())
