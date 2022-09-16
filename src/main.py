from os.path import abspath

from getdata import get_all_by_lang
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
        # TODO: add more datas

        if len(lang) > 0:
            lang = f"_{lang}"
        out_file = open(abspath(f"../{BASIC_NAME}{lang}.md"), "w+")
        out_file.write(raw_template)


