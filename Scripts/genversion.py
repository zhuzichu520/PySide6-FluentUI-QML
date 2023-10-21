import os
import subprocess
from mako.template import Template


def get_commit_count(repo_path):
    git_cmd = f"git --git-dir={repo_path}/.git rev-list HEAD --count"
    result = subprocess.run(git_cmd, shell=True, check=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output = result.stdout.strip()
    if output:
        commit_count = output
        return commit_count
    return "0"


def get_latest_tab(repo_path):
    result = subprocess.check_output(
        ['git', 'describe', '--tags', '--abbrev=0'], cwd='./', universal_newlines=True)
    output = result.strip()
    if (output):
        latest_tag = output
        return latest_tag
    return "1.0.0"


def generalTemplate(template_path, out_path, context):
    out_dir = os.path.dirname(out_path)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    template = Template(filename=template_path, preprocessor=[
        lambda x: x.replace("\r\n", "\n")])
    rendered = template.render(**context)
    with open(out_path, 'w') as file:
        file.write(rendered)


def exportIssFile():
    git_latest_tag = get_latest_tab("./")
    context = {
        "GIT_SEMVER": git_latest_tag
    }
    generalTemplate('./.template/InstallerScript.iss.in',
                    './action-cli/InstallerScript.iss', context)


def exportVersionPy():
    git_latest_tag = get_latest_tab("./")
    context = {
        "GIT_SEMVER": git_latest_tag
    }
    generalTemplate('./.template/version.py.in',
                    './example/version.py', context)


def exportFileVersionInfo():
    git_latest_tag = get_latest_tab("./")
    git_commit_count = get_commit_count('./')
    split_version_arr = git_latest_tag.split('.')
    ver_major = split_version_arr[0]
    ver_minor = split_version_arr[1]
    ver_patch = split_version_arr[2]
    ver_build = git_commit_count
    context = {
        "VER_MAJOR": ver_major,
        "VER_MINOR": ver_minor,
        "VER_PATCH": ver_patch,
        "VER_BUILD": ver_build,
    }
    generalTemplate('./.template/file_version_info.txt.in',
                    './action-cli/file_version_info.txt', context)


def exec():
    exportIssFile()
    exportFileVersionInfo()
    exportVersionPy()


if __name__ == '__main__':
    exec()
