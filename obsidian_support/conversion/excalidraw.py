import re

from mkdocs.structure.pages import Page
from overrides import override

from obsidian_support.abstract_conversion import AbstractConversion, SyntaxGroup

"""
a strategy that convert [excalidraw link] to [excalidraw kroki code block]
"""


class ExcalidrawConversion(AbstractConversion):
    excalidraw_json_pattern = re.compile(r"```json\n(?P<json>[\\s\\S]+)\n```")

    @property
    @override
    def obsidian_regex_pattern(self):
        # OBSIDIAN_EXCALIDRAW_PATH_REGEX
        return re.compile(r"!\[\[(?P<excalidraw_path>[^|^\]]+.excalidraw)]]")

    @override
    def convert(self, syntax_groups: SyntaxGroup, page: Page) -> str:
        return self._convert_excalidraw(*syntax_groups, page)

    def _convert_excalidraw(self, excalidraw_path: str, page: Page) -> str:
        src_uri = page.file.src_uri
        src_dir_index = src_uri[:len(src_uri) - 1].rfind('/')
        src_dir_path = src_uri[:src_dir_index] + "/"
        excalidraw_file_path = "docs/" + src_dir_path + excalidraw_path + '.md'

        f = open(excalidraw_file_path, 'r')
        excalidraw_markdown = f.read()
        excalidraw_json_match = self.excalidraw_json_pattern.search(excalidraw_markdown)
        excalidraw_json = excalidraw_json_match.group('json')
        f.close()

        return f"```kroki-excalidraw\n{excalidraw_json}\n```"
