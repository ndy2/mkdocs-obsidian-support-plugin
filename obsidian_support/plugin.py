import re

from mkdocs.plugins import BasePlugin

OBSIDIAN_ADMONITION_REGEX = ">\\[!(?P<type>[a-z]+)\\](?P<title> .*)?(?P<lines>(\n>.*)*)"


def apply_admonition(markdown):
    replaced_markdown = ""
    index = 0
    count = 0

    for result in re.finditer(OBSIDIAN_ADMONITION_REGEX, markdown):
        start = result.start()
        end = result.end()
        count = count + 1

        ad_type = result.group('type')
        title = result.group('title')
        lines = result.group('lines')

        lines = lines.replace("\n>", "\n    ")

        if title is None:
            title = ""
        else:
            title = ' \"' + title[1:] + '\"'

        replacedTip = "!!! " + ad_type + title + "\n" + lines + "\n"

        replaced_markdown += markdown[index:start]
        replaced_markdown += replacedTip
        index = end + 1

    replaced_markdown += markdown[index:len(markdown)]
    return replaced_markdown


class ObsidianSupportPlugin(BasePlugin):

    def on_page_markdown(self, markdown, page, config, files):
        markdown = apply_admonition(markdown)
        return markdown
