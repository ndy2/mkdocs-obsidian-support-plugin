from contextlib import ExitStack

import pytest
from assertpy import assert_that

from obsidian_support.abstract_conversion import AbstractConversion
from obsidian_support.conversion.admonition import AdmonitionConversion
from obsidian_support.conversion.admonition_backquotes import AdmonitionBackquotesConversion
from obsidian_support.conversion.excalidraw import ExcalidrawConversion
from obsidian_support.conversion.image_link import ImageLinkConversion
from obsidian_support.conversion.tags import TagsConversion
from obsidian_support.markdown_convert import markdown_convert

"""
unit tests for `obsidian syntax` to `mkdocs-material syntax` conversion
"""


@pytest.mark.parametrize("test", ['indent', 'complex', 'edgecase', 'collapsible'])
def test_callout_to_admonition(test):
    assert_template("admonition", test, AdmonitionConversion())


@pytest.mark.parametrize("test", ['basic'])
def test_callout_to_admonition_backquotes(test):
    assert_template("admonition_backquotes", test, AdmonitionBackquotesConversion())


@pytest.mark.skip
@pytest.mark.parametrize("test", ['basic'])
def test_excalidraw_convert(test):
    assert_template("excalidraw", test, ExcalidrawConversion())


@pytest.mark.parametrize("test", ['basic', 'size', 'caption', 'size_caption'])
def test_wikilink_image_to_md_link_image(test):
    assert_template("image_link", test, ImageLinkConversion())


@pytest.mark.parametrize("test", ['basic'])
def test_tag_conversion(test):
    assert_template("tags", test, TagsConversion())


def assert_template(conversion_name: str, test: str, conversion: AbstractConversion):
    with ExitStack() as stack:
        src = stack.enter_context(open(f"{conversion_name}/given/{test}.md", 'r'))
        dest = stack.enter_context(open(f"{conversion_name}/expected/{test}.md", 'r'))
        given = src.read()
        expected = dest.read()

        # when
        actual = markdown_convert(given, None, conversion)

        # then
        assert_that(expected).is_equal_to(actual)
