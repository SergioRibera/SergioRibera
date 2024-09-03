from getdata import AUTHOR, PROJECT_NAME_FILE, REPO_SERVER

TEMPLATE_VARIABLE = "@PROJECTS"

class Project:
    name: str
    description: str
    author: str = AUTHOR

def proj_from_dict(o: dict) -> Project:
    p = Project()
    p.name = o['name']
    p.description = o['description']
    return p


def generate_table_data(p: Project) -> str:
    return f"""
<tr>
<td><a href="{REPO_SERVER}/{AUTHOR}/{p.name}" target="_blank" ><b>{p.name}</b></a>: {p.description}</td>
<td><img alt="Stars" src="https://img.shields.io/github/stars/{AUTHOR}/{p.name}?style=flat-square&labelColor=343b41"/></td>
<td><img alt="Forks" src="https://img.shields.io/github/forks/{AUTHOR}/{p.name}?style=flat-square&labelColor=343b41"/></td>
<td><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/{AUTHOR}/{p.name}?style=flat-square"/></td>
<td><img alt="Language" src="https://img.shields.io/github/languages/top/{AUTHOR}/{p.name}?style=flat-square"/></td>
</tr>"""

def generate_table(projects: list) -> str:
    generateds = [generate_table_data(proj_from_dict(p)) for p in projects]
    return "".join(generateds)

def replace_template(data, lang: str, raw_temp: str):
    d = data[PROJECT_NAME_FILE]
    if len(lang) == 0:
        lang = "en"
    if lang in d:
        d = d[lang]
    projects = generate_table(d)
    return raw_temp.replace(TEMPLATE_VARIABLE, projects)

