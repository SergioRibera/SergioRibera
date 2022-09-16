from os.path import abspath

from getdata import get_all_by_lang, replace_lang
from project import replace_template

OUT_DIR = abspath("../")
TEMPLATE_README = "../template.md"
BASIC_NAME = "README"
LANGS = [ "", "EN", "ES" ]

data = get_all_by_lang()

with open(TEMPLATE_README) as template:
    raw_template = template.read()
    for lang in LANGS:
        raw_template = replace_template(data, lang, raw_template)
        raw_template = replace_lang(raw_template, LANGS)
        if len(lang) > 0:
            raw_template = raw_template.replace("@LANG", lang)
        else:
            # Default language
            raw_template = raw_template.replace("@LANG", "EN")
        # TODO: add more datas

        if len(lang) > 0:
            lang = f"_{lang}"
        out_file = open(abspath(f"../{BASIC_NAME}{lang}.md"), "w+")
        out_file.write(raw_template)


