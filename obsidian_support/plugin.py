import re

from mkdocs.plugins import BasePlugin


class ObsidianSupportPlugin(BasePlugin):

    def on_page_markdown(self, markdown, page, config, files):
        markdown = convert_callout_to_admonition(markdown)
        markdown = convert_wikilink_to_mdlink(markdown)

        return markdown


def convert_callout_to_admonition(markdown):
    obsidian_callout_regex = "> ?\\[!(?P<type>[a-z]+)\\](?P<title> .*)?(?P<lines>(\n>.*)*)"

    replaced_markdown = ""
    index = 0
    for callout in re.finditer(obsidian_callout_regex, markdown):
        start = callout.start()
        end = callout.end()

        ad_type = callout.group('type')
        title = callout.group('title')
        lines = callout.group('lines')

        lines = lines.replace("\n>", "\n    ")

        if title is None:
            title = ""
        else:
            title = ' \"' + title[1:] + '\"'

        admonition = "!!! " + ad_type + title + "\n" + lines + "\n"

        replaced_markdown += markdown[index:start]
        replaced_markdown += admonition
        index = end + 1

    replaced_markdown += markdown[index:len(markdown)]
    return replaced_markdown


def convert_wikilink_to_mdlink(markdown):
    wikilink_regex = "!\\[\\[(?P<image_path>.+)\\]\\]"

    replaced_markdown = ""
    index = 0
    for wikilink in re.finditer(wikilink_regex, markdown):
        start = wikilink.start()
        end = wikilink.end()

        image_path = wikilink.group('image_path')

        mdlink = '![' + image_path + '](' + image_path + ')'

        replaced_markdown += markdown[index:start]
        replaced_markdown += mdlink
        index = end + 1

    replaced_markdown += markdown[index:len(markdown)]
    return replaced_markdown
