import os
import subprocess

import env


def generateResource(_projectName):
    subprocess.run([env.pyside6_rcc(), os.path.join('.', _projectName, 'imports', 'resource.qrc'), "-o", os.path.join('.', _projectName, 'imports', 'resource_rc.py')])


if __name__ == "__main__":
    generateResource("FluentUI")
    generateResource(env.projectName)
