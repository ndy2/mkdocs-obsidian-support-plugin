import re
from inspect import cleandoc

from obsidian_support.abstract_conversion import AbstractConversion, SyntaxGroup
from mkdocs.structure.pages import Page

"""
a strategy that convert [excalidraw link] to [excalidraw kroki code block]
"""

EXCALIDRAW_LINK_REGEX = "!\\[\\[(?P<excalidraw_path>[^\\|^\\]]+.excalidraw)\\]\\]"
EXCALIDRAW_LINK_REGEX_GROUPS = ['excalidraw_path']
EXCALIDRAW_JSON_PATTERN = re.compile("```json\n(?P<json>[\\s\\S]+)\n```")


class ExcalidrawConvert(AbstractConversion):
    def __init__(self):
        super().__init__(EXCALIDRAW_LINK_REGEX, EXCALIDRAW_LINK_REGEX_GROUPS)

    def convert(self, syntax_groups: SyntaxGroup, page: Page) -> str:
        return convert_excalidraw(*syntax_groups, page)


def convert_excalidraw(excalidraw_path: str, page:Page) -> str:
    src_uri = page.file.src_uri
    src_dir_index = src_uri[:len(src_uri)-1].rfind('/')
    src_dir_path = src_uri[:src_dir_index] + "/"
    excalidraw_file_path = "docs/" + src_dir_path + excalidraw_path+'.md'

    f = open(excalidraw_file_path, 'r')
    excalidraw_markdown = f.read()
    excalidraw_json_match = EXCALIDRAW_JSON_PATTERN.search(excalidraw_markdown)
    excalidraw_json = excalidraw_json_match.group('json')
    f.close()

    return f"```kroki-excalidraw\n{excalidraw_json}\n```"
