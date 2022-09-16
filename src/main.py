from os.path import abspath

from getdata import get_all_by_lang, replace_lang
from project import replace_template
from about import replace_about
from titles import replace_titles

OUT_DIR = abspath("../")
TEMPLATE_README = "../template.md"
BASIC_NAME = "README"
LANGS = [ "", "EN", "ES" ]

data = get_all_by_lang()

with open(TEMPLATE_README) as template:
    raw_template_content = template.read()
    for lang in LANGS:
        raw_template = str(raw_template_content)
        raw_template = replace_lang(raw_template, LANGS)
        raw_template = replace_template(data, lang, raw_template)
        raw_template = replace_about(data, lang, raw_template)
        raw_template = replace_titles(data, lang, raw_template)
        # TODO: add more datas

        if len(lang) > 0:
            raw_template = raw_template.replace("@LANG", lang)
            lang = f"_{lang}"
        else:
            raw_template = raw_template.replace("@LANG", "EN")
        out_file = open(abspath(f"../{BASIC_NAME}{lang.upper()}.md"), "w")
        out_file.write(raw_template)


