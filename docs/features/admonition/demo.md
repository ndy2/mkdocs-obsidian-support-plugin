
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

`7. note with content tab` - might be imporved

 > [!note] code block with content tab and admonition
> === "C"
> 
>     ``` c
>     #include <stdio.h>
>     
>     in main(void) {
>         printf("Hello world!\n")
>         return 0;
>     }
>     ```
>    
> === "kotlin"
> 
>     ``` kotlin
>     fun main(){
>         println("Hello world!")
>     }
>     ```


 > [!example]
> === "Unordered List"
> 
>     ``` markdown
>     * Sed sagittis eleifend rutrum
>     * Donec vitae suscipic est
>     * Nulla tempor lobortis orci
>     ```
>    
> === "Ordered List"
> 
>     ``` markdown
>     1. Sed sagittis eleifend rutrum
>     2. Donec vitae suscipic est
>     3. Nullatempor loboritis orci
>     ```
