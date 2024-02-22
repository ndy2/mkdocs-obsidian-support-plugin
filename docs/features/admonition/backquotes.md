---
title: Admonition Backquotes
---
> [!note]  feature - admonition backquotes
> convert `block-styled admonition` to `mkdocs-material admonition`
> 
> - block-styled admonition - [github>javalen>admonitions](https://github.com/javalent/admonitions)
> - [mkdocs-material admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)
>   
>  Requires
>  - obsidian plugin - admonition

###  Admonition Backquotes

=== "obsidian markdown"

````
```ad-tip
title: This is a tip

This is the content of the admonition tip.
```
````

=== "obsidian rendered"

![[images/backquotes_1.png]]

### mkdocs-material admonition

=== "mkdocs-material markdown"

```
!!!tip "This is a tip"

    This is the content of the admonition tip.
```

=== "mkdocs-material rendered"

```ad-tip
title: This is a tip

This is the content of the admonition tip.
```