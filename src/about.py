ABOUT_NAME_FILE = "about"
SO_TEMPLATE_VARIABLE = "@ABOUT_SO"
WM_TEMPLATE_VARIABLE = "@ABOUT_WM"
TERM_TEMPLATE_VARIABLE = "@ABOUT_TERM"
SHELL_TEMPLATE_VARIABLE = "@ABOUT_SHELL"
CODE_TEMPLATE_VARIABLE = "@ABOUT_CODE"
NOTE_TEMPLATE_VARIABLE = "@ABOUT_NOTE"
EXTRA_TEMPLATE_VARIABLE = "@ABOUT_EXTRA"
TECH_TITLE_TEMPLATE_VARIABLE = "@ABOUT_TECH_TITLE"
FAVORITE_TECH_TEMPLATE_VARIABLE = "@ABOUT_FAVORITE_TECH"


def replace_about(data, lang: str, raw_temp: str) -> str:
    d = data[ABOUT_NAME_FILE]
    if len(lang) == 0:
        lang = "EN"
    if lang in d:
        d = d[lang]
    s = raw_temp.replace(SO_TEMPLATE_VARIABLE, d['so'])
    s = s.replace(WM_TEMPLATE_VARIABLE, d['wm'])
    s = s.replace(TERM_TEMPLATE_VARIABLE, d['terminal'])
    s = s.replace(SHELL_TEMPLATE_VARIABLE, d['shell'])
    s = s.replace(CODE_TEMPLATE_VARIABLE, d['code_editor'])
    s = s.replace(NOTE_TEMPLATE_VARIABLE, d['note'])
    s = s.replace(EXTRA_TEMPLATE_VARIABLE, d['extra'])
    s = s.replace(TECH_TITLE_TEMPLATE_VARIABLE, d['tech_title'])
    s = s.replace(FAVORITE_TECH_TEMPLATE_VARIABLE, d['favorite_tech'])
    return s

