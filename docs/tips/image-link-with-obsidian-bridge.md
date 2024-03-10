---
title: image-link with obsidian-bridge
comments: true
---


Feature [[image-link/index|Image-link]] can work with [obsidian-bridge](https://github.com/GooRoo/mkdocs-obsidian-bridge).

1. add mkdocs-obsidian-bridge plugin below mkdocs-obsidian-support-plugin.

```yaml
plugins:  
  - obsidian-support  
  - obsidian-bridge
```

2. you can use `obsidian bridge` with `obsidian support - image-link` as in below

**obsidian style `wikilink` with image size**

```
![[book.png|200]]
```

**mkdocs-material rendered**

![[book.png|200]]






