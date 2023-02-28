---
title: Excalidraw
---
---
 
> [!warning]
> - This feature is not completed yet.
> - Currently, it does not work as intented in many situations, due to the [issue related to path resolution in mkdocs-kroki-plugin](https://github.com/AVATEAM-IT-SYSTEMHAUS/mkdocs-kroki-plugin/issues/29).
> - I found that some developers work hard on this issue. As soon as it resovles, I will proceed on this feature.


> [!note]  feature - excalidraw
> render `excalidraw.md` in `mkdocs` as in obsidian!

With this feature you can embed your `excalidraw.md` file as an image

---

### Prerequisites

- [obsidian-excalidraw-plugin](https://github.com/zsviczian/obsidian-excalidraw-plugin)
- [mkdocs-kroki-plugin](https://github.com/AVATEAM-IT-SYSTEMHAUS/mkdocs-kroki-plugin)

> [!success] plugin order
> * MkDocs plugin order is important for this feature
> * By default plugin applied in order as they appear in the config.
> * You should write `kroki` after `obsidian-support`
>  
>  ```yaml title="mkdocs.yml"
>  plugins:
>      ...
>      - obsidian-support
>      - kroki :
>          FencePrefix: 'kroki-'
>  ```

---

### Usage

#### Basic

=== "markdown"
    
    `![[my-draw.excalidraw]]`
    
=== "rendered"
        
    ![[my-draw.excalidraw]]
<br>

=== "markdown"
    `![[my-circles.excalidraw]]`
=== "rendered"
    ![[my-circles.excalidraw]]

#### TODO - With custom size & Captions

- `![[my-draw.excalidraw|200]]`
- `![[my-draw.excalidraw|caption]]`
- `![[my-draw.excalidraw|200|caption]]`

---

### Tips

I include `my-draw.excalidraw.md` as document to show `the directory structure` and `how the xxx.excalidraw.md file consists of` . In most case, you need only the rendered image, not `xxx.excalidraw.md` as document. You can use [`mkdocs-exclude-plugin` ](https://github.com/apenwarr/mkdocs-exclude) with blow config to exclude all excalidraw documents.

```yaml
plugins:
  - obsidian-support
  - exclude:
        glob:
            - "*/*.excalidraw.md"
```


### shoulders of giants...

#### excalidraw, obsidian-excalidraw-plugin

If you use `obsidian`, you might know about this plugin. This is one of the most popular obsidian plugin. It embeds the [excalidraw](https://excalidraw.com/) - a web based hand-drawn diagram editor to obsidian perfectly.

With below option enabled which is default,

![[1.png|`Filename>.excalidraw.md or .md` option]]

your new excalidraw file will get name `my-draw.excalidraw.md`. You can embed this file to your document in wikilink syntax - `![[my-draw.excalidraw]]`

But mkdocs does not know about `wikilink syntax` and `how to treat this file`.

#### kroki

> [!quote] kroki
> [`kroki`](https://kroki.io/) creates **diagrams** from **textual** descriptions!
> Kroki provides a unified API with support for BlockDiag (BlockDiag, SeqDiag, ActDiag, NwDiag, PacketDiag, RackDiag), BPMN, Bytefield, C4 (with PlantUML), D2, DBML, Ditaa, Erd, ==Excalidraw==, GraphViz, Mermaid, Nomnoml, Pikchr, PlantUML, Structurizr, SvgBob, UMLet, Vega, Vega-Lite, WaveDrom... and more to come!

> [!note]
> `kroki` provied a API with support fo `Excalidraw`

#### mkdocs-kroki-plugin

This plugin 
- uses `the code block syntax` for the textual descriptions for the kroki diagram. 
- process the API request to `https://kroki.io/` and get the processed image (link or image itself).
- use this image and serve as markdown image link
