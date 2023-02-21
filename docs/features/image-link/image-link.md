## Image-Link

> [!note]  feature - image-link
> convert `obsidian wikilink for images` to `mkdocs-material md-link for images`


bsidian support [`wikilink`](https://help.obsidian.md/Linking+notes+and+files/Internal+links) with [embbe an image in a note](https://help.obsidian.md/Linking+notes+and+files/Embedding+files#Embed+an+image+in+a+note) which is also known as `internal link`. However markdown and mkdocs-material does not support `wikilink`. It uses traditional [`markdown links`](https://squidfunk.github.io/mkdocs-material/reference/images/).

```text
wikilink :  ![[images/hello.png]] 
mdlink   :  [images/hello.png](images/hello.png)
```



## Features

| type                        | wikilink                 | converted link                          | supported |
| --------------------------- | ------------------------ | --------------------------------------- | ------- |
| basic                       | `![[hello.png]]`        | `![hello.png](hello.png)`               | o       |
| path                   | `![[image/hello.png]]`   | ``![images/hello.png](images/hello.png)`` | o       |
| custom size            | `![[hello.png|200x300]]` |                                         | x       |
| caption                | `![[hello.png|caption]]` |                                      bye   | x       |
| custom size & caption | `![[images/hello.png|caption|200]]`                        |   hi                                      |  x       |


`| hi`

`![[heelo|hi]]``