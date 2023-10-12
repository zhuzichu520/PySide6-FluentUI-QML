#!C:\Users\zhuzi\AppData\Local\Programs\Python\Python311\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'PySide6-Essentials==6.5.3','console_scripts','pyside6-rcc'
import os
import sys
import site
import subprocess


def exec():
    if len(sys.argv) < 2:
        print("error paramter")
        return
    arguments = sys.argv[1:]
    command_args = arguments[0]+' -o '+arguments[1]
    amin_script = os.path.join(sys.prefix, "Scripts", "pyside6-rcc.exe")
    print("admin_script = "+amin_script)
    if os.path.exists(amin_script):
        subprocess.run(f'{amin_script} {command_args}', shell=True)
        return
    user_script = os.path.join(os.path.dirname(
        site.USER_SITE), "Scripts", "pyside6-rcc.exe")
    print("user_script = "+user_script)
    if os.path.exists(user_script):
        subprocess.run(f'{user_script} {command_args}', shell=True)
        return
    print("error: not find pyside6-rcc")


if __name__ == '__main__':
    exec()
