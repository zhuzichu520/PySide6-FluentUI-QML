import os
import sys
import subprocess

def find_cmd():
    base_cmd = "pyside6-rcc"
    if os.name == 'nt':  # Windows
        cmd = f"{base_cmd}.exe"
    else:
        cmd = base_cmd

    bin_paths = []

    # Unix global installation, Windows
    bin_paths.append(os.path.join(sys.prefix, 'bin'))
    # Also consider ~/.local/bin for Unix-like user installation
    # But this is a fallback so at the end of list
    if os.name != 'nt':
        bin_paths.append(os.path.expanduser('~/.local/bin'))

    for dir in bin_paths:
        path = os.path.join(dir, cmd)
        if os.path.exists(path):
            return path

    return None

def exec():
    if len(sys.argv) < 3:
        print("Parameter error: python qrc2py.py /path/to/qrc/file /path/to/output.py")
        return
    arguments = sys.argv[1:]
    command_args = arguments[0]+' -o '+arguments[1]
    script = find_cmd()
    if script is None:
        print("error: not find pyside6-rcc")
        exit(1)

    print("script = " + script)
    subprocess.run(f'{script} {command_args}', shell=True)

if __name__ == '__main__':
    exec()
