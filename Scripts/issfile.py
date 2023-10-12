import os
import subprocess
from mako.template import Template


def exec():
    latest_tag = latest_tag = subprocess.check_output(
        ['git', 'describe', '--tags', '--abbrev=0'], cwd='./', universal_newlines=True).strip()
    print("last: tag", latest_tag)
    template_dir = './.template/InstallerScript.iss.in'
    context = {
        "GIT_SEMVER": latest_tag
    }
    template = Template(filename=template_dir, preprocessor=[
                        lambda x: x.replace("\r\n", "\n")])
    rendered_template = template.render(**context)
    folder_path = './action-cli/'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    with open('./action-cli/InstallerScript.iss', 'w') as file:
        file.write(rendered_template)


if __name__ == '__main__':
    exec()
