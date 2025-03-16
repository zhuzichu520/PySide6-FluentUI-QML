import os
import shutil
import subprocess

import env


def generateTranslations(projectName: str, localeDatas, files=None):
    if not files:
        files = []
    targetFolder = f"{os.path.join('.', projectName, 'imports', projectName, 'i18n')}"
    for locale in localeDatas:
        tsFileName = f"{projectName}_{locale}.ts"
        qmFileName = f"{projectName}_{locale}.qm"
        tsFilePath = f"{os.path.join('.', projectName, tsFileName)}"
        qmFilePath = f"{os.path.join('.', projectName, qmFileName)}"
        commands = [env.pyside6_lupdate(), os.path.join('.', projectName, 'imports', "resource.qrc")]
        for file in files:
            commands.append(file)
        commands.append("-ts")
        commands.append(tsFilePath)
        subprocess.run(commands)
        subprocess.run([env.pyside6_lrelease(), tsFilePath])
        os.makedirs(targetFolder, exist_ok=True)
        shutil.copy(qmFilePath, os.path.join(targetFolder, qmFileName))


if __name__ == "__main__":
    generateTranslations("FluentUI", ["en_US", "zh_CN"])
    generateTranslations(env.projectName, ["en_US", "zh_CN"])
