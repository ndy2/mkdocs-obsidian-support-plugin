from assertpy import assert_that

from obsidian_support.markdown_code_extract import get_code_indices, EXCLUDE_RANGES


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
```"""

    # when
    code_indices: EXCLUDE_RANGES = get_code_indices(markdown)

    # then
    assert_that(code_indices).is_length(7)

    # ## Hi there.
    assert_that(code_indices[0]).is_equal_to((26, 31))  # indices of `code`

    # ## Kotlin
    assert_that(code_indices[1]).is_equal_to((45, 46))  # indices of ``
    assert_that(code_indices[2]).is_equal_to((47, 98))  # indices of `kotlin\n    fun ...`
    assert_that(code_indices[3]).is_equal_to((99, 100))  # indices of ``

    # ## Tip
    assert_that(code_indices[4]).is_equal_to((111, 112))  # indices of ``
    assert_that(code_indices[5]).is_equal_to((113, 130))  # indices of `ad-tip\n    some tip`
    assert_that(code_indices[6]).is_equal_to((131, 132))  # indices of ``
