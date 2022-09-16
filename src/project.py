from getdata import PROJECT_NAME_FILE

REPO_SERVER = "https://github.com"
TEMPLATE_VARIABLE = "@PROJECTS"
AUTHOR = "SergioRibera"

class Project:
    name: str
    repo: str
    author: str = AUTHOR

def proj_from_dict(o: dict) -> Project:
    p = Project()
    p.name = o['name']
    p.repo = o['repo']
    return p


def generate_table_data(p: Project) -> str:
    return f"""
<tr>
<td><a href="{REPO_SERVER}/{AUTHOR}/{p.repo}" target="_blank" ><b>{p.name}</b></a></td>
<td><img alt="Stars" src="https://img.shields.io/github/stars/{AUTHOR}/{p.repo}?style=flat-square&labelColor=343b41"/></td>
<td><img alt="Forks" src="https://img.shields.io/github/forks/{AUTHOR}/{p.repo}?style=flat-square&labelColor=343b41"/></td>
<td><img alt="Issues" src="https://img.shields.io/github/issues/{AUTHOR}/{p.repo}?style=flat-square"/></td>
<td><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/{AUTHOR}/{p.repo}?style=flat-square"/></td>
<td><img alt="Language" src="https://img.shields.io/github/languages/top/{AUTHOR}/{p.repo}?style=flat-square"/></td>
</tr>"""

def generate_table(projects: list) -> str:
    generateds = [generate_table_data(proj_from_dict(p)) for p in projects]
    return "".join(generateds)

def replace_template(data, lang: str, raw_temp: str):
    data = data[PROJECT_NAME_FILE]
    if data is dict:
        data = data[lang]
    projects = generate_table(data)
    return raw_temp.replace(TEMPLATE_VARIABLE, projects)

