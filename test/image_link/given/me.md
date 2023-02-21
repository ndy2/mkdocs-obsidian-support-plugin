### Examples

> [!tip]
> Compare this page with it's original markdown. See the top right link


`1. basic`

> [!note]
> basic admonition conversion test

`2. with external links`

> [!note]
> github for this project - [link](https://github.com/ndy2/mkdocs-obsidian-support-plugin)

`3. with title `

> [!note] title
> haha

`4. with image (in Markdown link)`

> [!note]
> ![images/img.png](images/img.png)

`5. with image (in Wiki link)`

> [!note]
> ![[images/img.png]]

`6. with code block`

> [!note] note with code block
> ```kotlin
> fun main() {
> 	println("hello world")
> ```

`7. note with content tab` - should be imporved

>[!note] note with content tab
>=== "C"
>    ``` c
>    #include <stdio.h>
>    
>    int main(void) {
>          printf("Hello world!\n");
>         return 0;
>    }
>    ```
> 
>=== "Kotlin"
>     ```kotlin
>     fun main(){
>     	println("Hello world!")
>     }
>     ```


### 2. ⚠️ Warning

1. within codeblock - `should be fixed`
```
> [!note] this should not be converted
> because it is in code block
```

 2. It does not work if your markdown starts with the call out it self.
	 - add dummy new link at the beginning of your markdown will fix it.

3. Unlike actual obsidian callout, It allows only zero or one space before and after `>`'character