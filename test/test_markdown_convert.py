from typing import List

from assertpy import assert_that

from obsidian_support.markdown_convert import _get_excluded_indices


def test_get_code_indices():
    # given
    markdown = """## Hi there.
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
~~~"""

    # when
    code_indices: List[tuple] = _get_excluded_indices(markdown)

    # then
    assert_that(code_indices).is_length(5)

    # tilde_code_block_indices
    assert_that(code_indices[0]).is_equal_to((145, 168))  # indices of `~~~markdown\n somde tip\n~~~`
    assert_that(code_indices[1]).is_equal_to((182, 274))  # indices of `~~~markdown\n ```kotlin\n ... ~~~`

    # backtick_code_block_indices
    assert_that(code_indices[2]).is_equal_to((45, 100))  # indices of ````kotlin\n    fun ...````
    assert_that(code_indices[3]).is_equal_to((111, 132))  # indices of ````ad-tip\nsomde tip\n````

    # backtick_code_indices
    assert_that(code_indices[4]).is_equal_to((26, 31))  # indices of ``code``
