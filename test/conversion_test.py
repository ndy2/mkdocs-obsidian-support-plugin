from unittest import TestCase

from parameterized import parameterized

from obsidian_support.abstract_conversion import AbstractConversion
from obsidian_support.conversion.admonition import AdmonitionConvert
from obsidian_support.conversion.image_link import ImageLinkConvert
from obsidian_support.markdown_convert import markdown_convert

"""
unit tests for `obsidian syntax` to `mkdocs-material syntax` conversion
"""


class ConversionTest(TestCase):

    @parameterized.expand(['indent', 'complex', 'edgecase','me'])
    def test_callout_to_admonition(self, test):
        self.assert_template("admonition", test, AdmonitionConvert())

    @parameterized.expand(['basic', 'size', 'caption', 'size_caption'])
    def test_wikilink_image_to_md_link_image(self, test):
        self.assert_template("image_link", test, ImageLinkConvert())

    def assert_template(self, conversion_name: str, test: str, conversion: AbstractConversion):
        ## given
        src = open(f"{conversion_name}/given/{test}.md", 'r')
        dest = open(f"{conversion_name}/expected/{test}.md", 'r')
        given = src.read()
        expected = dest.read()

        ## when
        actual = markdown_convert(given, conversion)

        ## then
        self.assertEqual(expected, actual)

        ## tear down
        src.close()
        dest.close()
