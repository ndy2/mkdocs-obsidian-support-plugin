---
title: Demo
comments: true
---
## Examples

`1. basic`

- markdown

```
> [!note]
> basic admonition conversion test
```

- rendered

> [!note]
> basic admonition conversion test

`2. with external links`

- markdown

```
> [!note]
> github for this project - [link](https://github.com/ndy2/mkdocs-obsidian-support-plugin)

```

- rendered

> [!note]
> github for this project - [link](https://github.com/ndy2/mkdocs-obsidian-support-plugin)

`3. with title `

- markdown

```
> [!note] title
> haha
```

- rendered

> [!note] title
> haha

`4. with image (in Markdown link)`

- markdown

```
> [!note]
> ![images/book.png](images/book.png)
```

- rendered

> [!note]
> ![images/book.png](images/book.png)

`5. with image (in Wiki link)`

- markdown

```
> [!note]
> ![[images/book.png]]
```

- rendered

> [!note]
> ![[images/book.png]]

`6. with code block`

- markdown

```
> [!note] note with code block
> ```kotlin
> fun main() {
> 	println("hello world")
> ```

```

- rendered

> [!note] note with code block
> ```kotlin
> fun main() {
> 	println("hello world")
> ```

`7. note with content tab` - might be imporved

- markdown

```
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
```

- rendered

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

- markdown

```
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
```

- rendered

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
