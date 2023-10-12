import os
import subprocess
from mako.template import Template

def exec():
    result = subprocess.run(['git', 'tag'], cwd='./', stdout=subprocess.PIPE, text=True)
    output = result.stdout
    tags = output.splitlines()
    latest_tag = result.stdout.strip()
    print("last: tag", latest_tag)
    template_dir = './.template/InstallerScript.iss.in'
    context = {
        "GIT_SEMVER" : latest_tag,
    }
    template = Template(filename=template_dir)
    rendered_template = template.render(**context)
    folder_path = './action_cli/'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    with open('./action_cli/InstallerScript.iss', 'w') as file:
        file.write(rendered_template)

if __name__ == '__main__':
    exec()