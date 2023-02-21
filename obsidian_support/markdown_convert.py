import re

from obsidian_support.abstract_conversion import AbstractConversion

"""
A template method that applies conversion for every regex matches 
"""


def markdown_convert(markdown: str, conversion: AbstractConversion) -> str:
    converted_markdown = ""
    index = 0
    for obsidian_syntax in re.finditer(conversion.obsidian_regex, markdown):
        start = obsidian_syntax.start()
        end = obsidian_syntax.end()

        syntax_groups = list(map(lambda group: obsidian_syntax.group(group), conversion.obsidian_regex_groups))

        mkdocs_syntax = conversion.convert(syntax_groups)
        converted_markdown += markdown[index:start]
        converted_markdown += mkdocs_syntax
        index = end + 1

    converted_markdown += markdown[index:len(markdown)]
    return converted_markdown
