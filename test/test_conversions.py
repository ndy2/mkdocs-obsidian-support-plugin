from contextlib import ExitStack

import pytest
from assertpy import assert_that

from obsidian_support.abstract_conversion import AbstractConversion
from obsidian_support.conversion.admonition import AdmonitionConversion
from obsidian_support.conversion.admonition_backquotes import AdmonitionBackquotesConversion
from obsidian_support.conversion.excalidraw import ExcalidrawConversion
from obsidian_support.conversion.image_internal_link import ImageInternalLinkConversion
from obsidian_support.conversion.image_web_link import ImageWebLinkConversion
from obsidian_support.conversion.tags import TagsConversion
from obsidian_support.markdown_convert import markdown_convert

"""
unit tests for `obsidian syntax` to `mkdocs-material syntax` conversion
"""


@pytest.mark.parametrize("test", ['indent', 'complex', 'edgecase', 'collapsible'])
def test_admonition_conversion(test):
    assert_template("admonition", test, AdmonitionConversion())


@pytest.mark.parametrize("test", ['basic'])
def test_admonition_backquotes_conversion(test):
    assert_template("admonition_backquotes", test, AdmonitionBackquotesConversion())


@pytest.mark.skip
@pytest.mark.parametrize("test", ['basic'])
def test_excalidraw_conversion(test):
    assert_template("excalidraw", test, ExcalidrawConversion())


@pytest.mark.parametrize("test", ['basic', 'size', 'caption', 'size_caption'])
def test_image_internal_link_conversion(test):
    assert_template("image_internal_link", test, ImageInternalLinkConversion())


@pytest.mark.parametrize("test", ['basic'])
def test_image_web_link_conversion(test):
    assert_template("image_web_link", test, ImageWebLinkConversion())


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
