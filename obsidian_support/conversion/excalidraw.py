import re
from inspect import cleandoc

from obsidian_support.abstract_conversion import AbstractConversion, SyntaxGroup

"""
a strategy that convert [excalidraw link] to [excalidraw kroki code block] 
"""

EXCALIDRAW_LINK_REGEX = "!\\[\\[(?P<excalidraw_path>[^\\|^\\]]+.excalidraw)\\]\\]"
EXCALIDRAW_LINK_REGEX_GROUPS = ['excalidraw_path']
EXCALIDRAW_JSON_PATTERN = re.compile("```json\n(?P<json>[\\s\\S]+)\n```")


class ExcalidrawConvert(AbstractConversion):
    def __init__(self):
        super().__init__(EXCALIDRAW_LINK_REGEX, EXCALIDRAW_LINK_REGEX_GROUPS)

    def convert(self, syntax_groups: SyntaxGroup) -> str:
        return convert_excalidraw(*syntax_groups)


def convert_excalidraw(excalidraw_path: str) -> str:
    f = open(excalidraw_path + ".md", 'r')
    excalidraw_markdown = f.read()
    print(excalidraw_markdown)

    excalidraw_json_match = EXCALIDRAW_JSON_PATTERN.search(excalidraw_markdown)
    excalidraw_json = excalidraw_json_match.group('json')
    f.close()

    return f"```kroki-excalidraw\n{excalidraw_json}\n```"
