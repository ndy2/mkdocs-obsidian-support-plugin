from inspect import cleandoc

from assertpy import assert_that

from obsidian_support.conversion.admonition.admonition_callout import AdmonitionCalloutConversion


def test_admonition_backquotes_conversion():
    # given
    conversion = AdmonitionCalloutConversion()
    markdown = cleandoc("""
    > [!note] some note
    > some content
    """)

    # when
    converted = conversion.markdown_convert(markdown, None)

    # then
    assert_that(converted).is_equal_to(cleandoc("""
    !!! note "some note"
    
        some content
    """))
