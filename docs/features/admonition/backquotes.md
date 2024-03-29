---
title: Admonition Backquotes
comments: true
---
> [!note]  feature - admonition backquotes
> convert `block-styled admonition` to `mkdocs-material admonition`
> 
> - block-styled admonition - [github>javalen>admonitions](https://github.com/javalent/admonitions)
> - [mkdocs-material admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)
>   
>  Requirement
>  - obsidian plugin - admonition

###  Admonition Backquotes


~~~tabs
---tab obsidian markdown
````
```ad-tip
title: This is a tip

This is the content of the admonition tip.
```
````
---tab obsidian rendered
![[images/backquotes_1.png]]
~~~





### mkdocs-material admonition

~~~tabs
---tab mkdocs-material markdown
```
!!!tip "This is a tip"

    This is the content of the admonition tip.
```

---tab mkdocs-material rendered
```ad-tip
title: This is a tip

This is the content of the admonition tip.
```
~~~
