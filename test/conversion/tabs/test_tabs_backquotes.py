from inspect import cleandoc

from conversion.tabs.tabs_backquotes import TabsBackquotesConversion
from obsidian_support.markdown_convert import markdown_convert


def test_tag_conversion():
    # given
    conversion = TabsBackquotesConversion()
    markdown = cleandoc("""
    ```tabs
    ---tab first tab
    ---tab second tab
    ```
    """)

    # when
    converted = markdown_convert(markdown, None, conversion)

    # then
    print(converted)
