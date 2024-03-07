from inspect import cleandoc

from assertpy import assert_that

from obsidian_support.conversion.admonition.admonition_backquotes import AdmonitionBackquotesConversion


def test_admonition_backquotes_conversion():
    # given
    conversion = AdmonitionBackquotesConversion()
    markdown = cleandoc("""
    ```ad-tip
    title: some title
    
    Line 1: This is the content of the admonition tip.
    Line 2: This is the content of the admonition tip.
    Line 3: This is the content of the admonition tip.
    ```
    """)

    # when
    converted = conversion.markdown_convert(markdown, None)

    # then
    assert_that(converted).is_equal_to(cleandoc("""
    !!! tip "some title"
    
        Line 1: This is the content of the admonition tip.
        Line 2: This is the content of the admonition tip.
        Line 3: This is the content of the admonition tip.
    """))
