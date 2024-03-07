from contextlib import ExitStack

import pytest
from assertpy import assert_that
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import File
from mkdocs.structure.pages import Page

from obsidian_support.conversion.abstract_conversion import AbstractConversion
from obsidian_support.conversion.admonition.admonition_backquotes import AdmonitionBackquotesConversion
from obsidian_support.conversion.admonition.admonition_callout import AdmonitionCalloutConversion
from obsidian_support.conversion.comment.comment import CommentConversion
from obsidian_support.conversion.image_link.image_internal_link import ImageInternalLinkConversion
from obsidian_support.conversion.image_link.image_web_link import ImageWebLinkConversion
from obsidian_support.conversion.pdf.pdf import PdfConversion
from obsidian_support.conversion.tabs.tabs_backquotes import TabsBackquotesConversion
from obsidian_support.conversion.tabs.tabs_tilde_block import TabsTildeBlockConversion
from obsidian_support.conversion.tags.tags import TagsConversion

"""
unit tests for `obsidian syntax` to `mkdocs-material syntax` conversion
"""


@pytest.mark.parametrize("test", ['indent', 'complex', 'edgecase', 'collapsible'])
def test_admonition_callout_conversion(test):
    assert_template("admonition/admonition_callout", test, AdmonitionCalloutConversion())


@pytest.mark.parametrize("test", ['basic'])
def test_admonition_backquotes_conversion(test):
    assert_template("admonition/admonition_backquotes", test, AdmonitionBackquotesConversion())


@pytest.mark.parametrize("test", ['basic'])
def test_comment_conversion(test):
    assert_template("comment", test, CommentConversion())


@pytest.mark.parametrize("test", ['basic', 'size', 'caption', 'size_caption'])
def test_image_internal_link_conversion(test):
    assert_template("image_link/image_internal_link", test, ImageInternalLinkConversion())


@pytest.mark.parametrize("test", ['basic', 'escape'])
def test_image_web_link_conversion(test):
    assert_template("image_link/image_web_link", test, ImageWebLinkConversion())


@pytest.mark.parametrize("test", ['basic'])
def test_pdf_conversion(test):
    assert_template("pdf", test, PdfConversion())


@pytest.mark.parametrize("test", ['basic'])
def test_tabs_backquotes_conversion(test):
    assert_template("tabs/tabs_backquotes", test, TabsBackquotesConversion())


@pytest.mark.parametrize("test", ['basic'])
def test_tabs_tilde_block_conversion(test):
    assert_template("tabs/tabs_tilde_block", test, TabsTildeBlockConversion())


@pytest.mark.parametrize("test", ['basic'])
def test_tag_conversion(test):
    assert_template("tags", test, TagsConversion())


def assert_template(conversion_name: str, test: str, conversion: AbstractConversion):
    with ExitStack() as stack:
        src = stack.enter_context(open(f"markdowns/{conversion_name}/given/{test}.md", 'r'))
        dest = stack.enter_context(open(f"markdowns/{conversion_name}/expected/{test}.md", 'r'))
        given = src.read()
        expected = dest.read()

        file = File(path="path", src_dir="src_dir", dest_dir="dest_dir", use_directory_urls=False)
        config = MkDocsConfig()
        config.site_name = "mkdocs-obsidian-support-plugin"
        config.site_url = "https://ndy2.github.io"
        config.site_dir = "mkdocs-obsidian-support-plugin"
        page = Page(title="test_page", file=file, config=config)

        # when
        actual = conversion.markdown_convert(given, page)

        # then
        assert_that(expected).is_equal_to(actual)
