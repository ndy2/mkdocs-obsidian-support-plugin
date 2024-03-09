from inspect import cleandoc

from assertpy import assert_that

from obsidian_support.conversion.tabs.tabs_backquotes import TabsBackquotesConversion


def test_tabs_conversion():
    # given
    conversion = TabsBackquotesConversion()
    markdown = cleandoc("""
    ```tabs
    ---tab first tab
    content-of-first-tab
    ---tab second tab
    content-of-second-tab
    ```
    """)

    # when
    converted = conversion.markdown_convert(markdown, None)

    # then
    assert_that(converted).is_equal_to(cleandoc("""
    === "first tab"
    
        content-of-first-tab
    === "second tab"
    
        content-of-second-tab
    """))
