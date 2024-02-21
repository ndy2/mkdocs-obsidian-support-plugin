---
title: Image-Link
---

> [!note]  feature - image-link
> convert `obsidian wikilink for images` to `mkdocs-material md-link for images`

obsidian support [`wikilink`](https://help.obsidian.md/Linking+notes+and+files/Internal+links)
with [embbe an image in a note](https://help.obsidian.md/Linking+notes+and+files/Embedding+files#Embed+an+image+in+a+note)
which is also known as `internal link`. However markdown and mkdocs-material does not support `wikilink`. It uses
traditional [`markdown links`](https://squidfunk.github.io/mkdocs-material/reference/images/).

```text
wikilink :  ![[images/hello.png]] 
mdlink   :  [images/hello.png](images/hello.png)
```

## Features

**Internal Links**

| type           | wikilink               | converted link                          |
|----------------|------------------------|-----------------------------------------|
| basic          | `![[hello.png]]`       | `![hello.png](hello.png)`               |
| path           | `![[image/hello.png]]` | `![images/hello.png](images/hello.png)` |
| size           | `![[hello.png          | 200x300]]`                              | see below content tab                    |
| caption        | `![[hello.png          | caption]]`                              | see below content tab                    |
| size & caption | `![[im/hello.png       | my-caption                              |200]]` | see below content tab                    |

**Web Links**

| type           | wikilink                                | converted link                       |
|----------------|-----------------------------------------|--------------------------------------|
| basic          | `![](https://path.to.image.png)`        | see below demo                       |
| size           | `![100x100](https://path.to.image.png)` | see below demo                       |
| caption        | `![caption](https://path.to.image.png)` | see below demo                       |
| size & caption | `![caption                              | 100x100](https://path.to.image.png)` | see below demo        |

**Converted links in `md_in_html` form**

=== "custom size"

	```html
	<figure markdown>
	  ![hello.png](hello.png){ width="200" height="300" }
	  
	</figure markdown>
	```

=== "caption"

	```html
	<figure markdown>
	  ![hello.png](hello.png)
	  <figcaption>my-caption</figcaption>
	</figure markdown>
	```

=== "custom size and caption"

	```html
	<figure markdown>
	  ![hello.png](hello.png){ width="200" height="300" }
	  <figcaption>caption</figcaption>
	</figure markdown>
	```

## Demo

**Internal Links**

> [!tip]
> Compare this page with it's original markdown. See the top right link

- `![[hello.png]]`

![[hello.png]]

- `![[hello.png|200x200]]`

![[hello.png|200x200]]

- `![[hello.png|hello-caption|200x200]]`

![[hello.png|hello-caption|200x200]]

**Web Links**

- `![](https://history-computer.com/ModernComputer/Basis/images/Engelbart.jpg)`

![](https://history-computer.com/ModernComputer/Basis/images/Engelbart.jpg)

- `![Engelbart](https://history-computer.com/ModernComputer/Basis/images/Engelbart.jpg)`

![Engelbart](https://history-computer.com/ModernComputer/Basis/images/Engelbart.jpg)

- `![100x100](https://history-computer.com/ModernComputer/Basis/images/Engelbart.jpg)`

![100x100](https://history-computer.com/ModernComputer/Basis/images/Engelbart.jpg)

- `![Engelbart|100x100](https://history-computer.com/ModernComputer/Basis/images/Engelbart.jpg)`

![Engelbart|100x100](https://history-computer.com/ModernComputer/Basis/images/Engelbart.jpg)

- `[![\PyPi](https://img.shields.io/pypi/v/mkdocs-obsidian-support-plugin)](https://pypi.org/project/mkdocs-obsidian-support-plugin/)`

result (web link image with hyperlink) : [![\\](https://img.shields.io/pypi/v/mkdocs-obsidian-support-plugin)](https://pypi.org/project/mkdocs-obsidian-support-plugin/)

You can escape web link conversion by adding `backslash - \` on prior to tag(replacement part)