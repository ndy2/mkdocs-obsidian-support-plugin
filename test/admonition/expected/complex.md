### Obsidian Callout to Mkdocs-material Admonition Conversion Complex Tests

1. basic

!!! note

    basic admonition conversion test

2. with external links

!!! note

    github for this project - [link](https://github.com/ndy2/mkdocs-obsidian-support-plugin)

3. with title 

!!! note "title"

    haha

4. with image (in Markdown link)

!!! note

    [img.png](../../images/img.png)

5. with code block

!!! note "note with code block"

    ```kotlin
    fun main() {
    	println("hello world")
    ```

6. note with content tab

!!! note "note with content tab"

    === "C"
    
    ``` c
    #include <stdio.h>
    
    int main(void) {
         printf("Hello world!\n");
         return 0;
    }
    ```
    
    === "Kotlin"
    
    ```kotlin
    fun main(){
    	println("Hello world!")
    }
    ```

7. within codeblock

```
> [!note] this should not be converted
> because it is in code block
```