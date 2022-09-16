
TITLE_NAME_FILE = "titles"
TT_VISITORS_TEMPLATE_VARIABLE = "@TITLE_VISITORS"
TT_LIVE_TEMPLATE_VARIABLE = "@TITLE_LIVE"
TT_ABOUT_TEMPLATE_VARIABLE = "@TITLE_ABOUT"
TT_PROJECT_TEMPLATE_VARIABLE = "@TITLE_PROJECT"
REGARDS_TEMPLATE_VARIABLE = "@TITLE_REGARDS"
CC_TEMPLATE_VARIABLE = "@TITLE_CC"
TABLE_NAME_TEMPLATE_VARIABLE = "@TITLE_PROJECT_NAME"
TABLE_STARS_TEMPLATE_VARIABLE = "@TITLE_PROJECT_STARS"
TABLE_FORKS_TEMPLATE_VARIABLE = "@TITLE_PROJECT_FORKS"
TABLE_ISSUES_TEMPLATE_VARIABLE = "@TITLE_PROJECT_ISSUES"
TABLE_PR_TEMPLATE_VARIABLE = "@TITLE_PROJECT_PR"
TABLE_LANG_TEMPLATE_VARIABLE = "@TITLE_PROJECT_LANG"


def replace_titles(data, lang: str, raw_temp: str) -> str:
    d = data[TITLE_NAME_FILE]
    if len(lang) == 0:
        lang = "EN"
    if lang in d:
        d = d[lang]
    s = raw_temp.replace(TABLE_NAME_TEMPLATE_VARIABLE, d['proj_title_name'])
    s = s.replace(TT_VISITORS_TEMPLATE_VARIABLE, d['visitors'])
    s = s.replace(TT_LIVE_TEMPLATE_VARIABLE, d['live'])
    s = s.replace(TABLE_STARS_TEMPLATE_VARIABLE, d['proj_title_stars'])
    s = s.replace(TABLE_FORKS_TEMPLATE_VARIABLE, d['proj_title_forks'])
    s = s.replace(TABLE_ISSUES_TEMPLATE_VARIABLE, d['proj_title_issues'])
    s = s.replace(TABLE_PR_TEMPLATE_VARIABLE, d['proj_title_pr'])
    s = s.replace(TABLE_LANG_TEMPLATE_VARIABLE, d['proj_title_lang'])
    s = s.replace(TT_ABOUT_TEMPLATE_VARIABLE, d['about_title'])
    s = s.replace(TT_PROJECT_TEMPLATE_VARIABLE, d['proj_title'])
    s = s.replace(REGARDS_TEMPLATE_VARIABLE, d['regards'])
    s = s.replace(CC_TEMPLATE_VARIABLE, d['cc'])
    return s

