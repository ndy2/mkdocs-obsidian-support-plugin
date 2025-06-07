from inspect import cleandoc
from typing import List

from assertpy import assert_that

from obsidian_support.conversion.util import get_exclude_indices


def test_get_exclude_indices_1():
    # given
    markdown = cleandoc("""
    `exclude me`
    """)

    # when
    exclude_indices = get_exclude_indices(markdown)

    # then
    assert_that(exclude_indices).is_length(1)
    assert_that(exclude_indices[0]).is_equal_to((0, 12))


def test_get_exclude_indices_2():
    # given
    markdown = cleandoc("""
    ```tabs
    ---tab obsidian markdown
    ~~~
    ![[features/pdf/a4-sample.pdf]]
    ~~~
    
    ~~~
    ![[features/pdf/a5-sample.pdf]]
    ~~~
    
    You can also specify the height in pixels for the embedded PDF viewer, by adding `#height=[number]` to the link. like this : `![[features/pdf/a4-sample.pdf#height=400]]`
    
    ---tab obsidian rendered
    ![[images/pdf_1.png]]
    ```
    """)

    # when
    exclude_indices = get_exclude_indices(markdown)

    # then
    assert_that(exclude_indices).is_length(4)
    assert_that(exclude_indices[0]).is_equal_to((33, 72))
    assert_that(exclude_indices[1]).is_equal_to((74, 113))
    assert_that(exclude_indices[2]).is_equal_to((196, 214))
    assert_that(exclude_indices[3]).is_equal_to((240, 284))


def test_get_exclude_indices_3():
    # given
    markdown = cleandoc("""
    ## Hi there.
    this is test `code`

    ### Kotlin
    ```kotlin
    fun main() {
        println("Hello world!")
    }
    ```

    ### Tip
    ```ad-tip
    some tip
    ```

    ### Tilde
    ~~~markdown
    some tip
    ~~~

    ### Nested
    ~~~markdown
    ```kotlin
    fun main() {
        println("Hello world!")
    }
    ```
    some tip
    `some code`
    ~~~
    """)

    # when
    code_indices: List[tuple] = get_exclude_indices(markdown)

    # then
    assert_that(code_indices).is_length(4)

    assert_that(code_indices[0]).is_equal_to((45, 101))  # indices of ````kotlin\n    fun ...````
    assert_that(code_indices[1]).is_equal_to((145, 169))  # indices of `~~~markdown\n somde tip\n~~~`
    assert_that(code_indices[2]).is_equal_to((182, 275))  # indices of `~~~markdown\n ```kotlin\n ... ~~~`
    assert_that(code_indices[3]).is_equal_to((26, 32))  # indices of ``code``


def test_get_exclude_indices_4():
    # given
    markdown = cleandoc("""
    ~~~~
    ```tabs
    ---tab First *tab*
    This is a *sample* **tab** with some markdown :
    ## Heading 2
    - [ ] Task 1
    - [ ] Task 2

    ### Heading 3
    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

    ---tab Second tab
    This tab has a code block:
    ~~~cpp
    include <iostream>
    using namespace std;

    int main() {
     char c;
     cout << "Enter a character: ";
     cin >> c;
     cout << "ASCII Value of " << c << " is " << int(c);
     return 0;
    }
    ~~~
    ---tab Last tab
    This tab contains callout
    > [!note] tab with callout!
    > callout content
    ```
    ~~~~
    """)

    # when
    code_indices: List[tuple] = get_exclude_indices(markdown)

    # then
    assert_that(code_indices).is_length(1)
    assert_that(code_indices[0]).is_equal_to((0, 546))  # indices of `~~~~\n...~~~~`


def test_get_exclude_indices_5():
    # given
    markdown = cleandoc("""
    `exclude me`
    
    ```
    exclude me
    ```

    `````
    exclude me
    `````
    
    ~~~
    exclude me
    ~~~
    
    ~~~~~
    exclude me
    ~~~~~
    
    `````
    ~~~ exclude me
    `````
    
    ```ad-tip
    include me
    ```
    
    ```kotlin
    exclude me
    ```
    
    ```tabs
    ---tab include me
    ```
    
    ~~~~
    ```tabs
    ---tab exclude me
    ~~~
    exclude me
    ~~~
    ```
    ~~~~
    
    ````
    ~~~tabs
    ---tab exclude me
    ```
    exclude me
    ```
    ~~~
    ````
    
    """)

    # when
    exclude_indices = get_exclude_indices(markdown)

    # then
    assert_that(exclude_indices).is_length(9)
    assert_that(exclude_indices[0]).is_equal_to((34, 56))
    assert_that(exclude_indices[1]).is_equal_to((78, 100))
    assert_that(exclude_indices[2]).is_equal_to((102, 128))
    assert_that(exclude_indices[3]).is_equal_to((213, 271))
    assert_that(exclude_indices[4]).is_equal_to((273, 331))
    assert_that(exclude_indices[5]).is_equal_to((14, 32))
    assert_that(exclude_indices[6]).is_equal_to((58, 76))
    assert_that(exclude_indices[7]).is_equal_to((156, 180))
    assert_that(exclude_indices[8]).is_equal_to((0, 12))


def test_get_exclude_indices_6():
    # given
    markdown = cleandoc("""
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
    exclude_indices = get_exclude_indices(markdown)

    # then
    assert_that(exclude_indices).is_length(1)
    assert_that(exclude_indices[0]).is_equal_to((33, 101))


def test_get_exclude_indices_7():
    # given
    markdown = cleandoc("""
    example <span style="background:#ff4d4f">highlighted</span> text
    """)

    # when
    exclude_indices = get_exclude_indices(markdown)

    # then
    assert_that(exclude_indices[0][0]).is_equal_to(markdown.index("<span "))
    assert_that(exclude_indices[0][1]).is_equal_to(markdown.index("</span>") + len("</span>"))
