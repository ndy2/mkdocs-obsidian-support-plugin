from inspect import cleandoc

from assertpy import assert_that

from obsidian_support.conversion.admonition.admonition_callout import AdmonitionCalloutConversion


def test_admonition_backquotes_conversion_1():
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


def test_admonition_backquotes_conversion_2():
    # given
    conversion = AdmonitionCalloutConversion()
    markdown = cleandoc("""
    > [!note] some note
    > some content before nested notes
    > 
    > > [!note] nested note with no content
    >
    > > [!note] another nested note with some another content
    > > some another content
    >
    > some content after nested notes
    """)

    # when
    converted = conversion.markdown_convert(markdown, None)

    # then
    assert_that(converted).is_equal_to(cleandoc("""
    !!! note "some note"
    
        some content before nested notes
        
        !!! note "nested note with no content"
        
        
        !!! note "another nested note with some another content"
        
            some another content
        
        some content after nested notes
    """))
