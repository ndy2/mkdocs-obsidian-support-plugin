from inspect import cleandoc

from assertpy import assert_that

from obsidian_support.conversion.tags.tags import TagsConversion


def test_tags_conversion_1():
    # given
    conversion = TagsConversion()
    markdown = "#tag"

    # when
    converted = conversion.markdown_convert(markdown, None)

    # then
    assert_that(converted).is_equal_to("**tag**{: .hash}")


def test_tags_conversion_2():
    # given
    conversion = TagsConversion()
    markdown = cleandoc("""
    #tag
    ```tabs
    ---tab obsidian markdown
    ~~~
    This is just an #obsidian tag. Click to go to the search bar
    ~~~
    ---tab mkdocs-material rendered
    This is just an #obsidian tag. Click to go to the search bar
    ```
    """)

    # when
    converted = conversion.markdown_convert(markdown, None)

    # then
    assert_that(converted).is_equal_to(cleandoc("""
    **tag**{: .hash}
    ```tabs
    ---tab obsidian markdown
    ~~~
    This is just an #obsidian tag. Click to go to the search bar
    ~~~
    ---tab mkdocs-material rendered
    This is just an **obsidian**{: .hash} tag. Click to go to the search bar
    ```
    """))
