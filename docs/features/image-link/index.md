## Image-Link

> [!note]  feature - image-link
> convert `obsidian wikilink for images` to `mkdocs-material md-link for images`


obsidian support [`wikilink`](https://help.obsidian.md/Linking+notes+and+files/Internal+links) with [embbe an image in a note](https://help.obsidian.md/Linking+notes+and+files/Embedding+files#Embed+an+image+in+a+note) which is also known as `internal link`. However markdown and mkdocs-material does not support `wikilink`. It uses traditional [`markdown links`](https://squidfunk.github.io/mkdocs-material/reference/images/).

```text
wikilink :  ![[images/hello.png]] 
mdlink   :  [images/hello.png](images/hello.png)
```



## Features

| type           | wikilink                            | converted link                          | implemented |
| -------------- | ----------------------------------- | --------------------------------------- | --------- |
| basic          | `![[hello.png]]`                    | `![hello.png](hello.png)`               | o         |
| path           | `![[image/hello.png]]`              | `![images/hello.png](images/hello.png)` | o         |
| size           | `![[hello.png|200x300]]`            | will be html                            | x         |
| caption        | `![[hello.png|caption]]`            | will be html                            | x         |
| size & caption | `![[im/hello.png|my-caption|200]]` | will be html                            | x         |

### Demo

> [!tip]
> Compare this page with it's original markdown. See the top right link

`![[hello.png]]`


![[hello.png]]

`![[hello.png|200x200]]`

![[hello.png|200x200]]


`![[hello.png|hello-caption|200x200]]`

![[hello.png|hello-caption|200x200]]
