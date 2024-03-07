---
title: Comment
comments: true
---

> [!note]  feature - comment
> Convert `obsidian comments` to `HTML Comment Tag`
>
> - [obsidian comments](https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax#Comments)
> - [HTML Comment Tag](https://www.w3schools.com/tags/tag_comment.asp)

## Usage

### obsidian comment

=== "obsidian markdown"

```
This is an %%inline%% comment.

%% 
This is a block comment. 
Block comments can span multiple lines. 
%%
```

=== "obsidian reading view"

![[images/comment_1.png]]

### mkdocs-material comment

=== "mkdocs-material markdown"

```
This is an <!--inline--> comment.

<!--
This is a block comment. 
Block comments can span multiple lines. 
-->
```

=== "mkdocs-material rendered"

This is an %%inline%% comment.

%% 
This is a block comment. 
Block comments can span multiple lines. 
%%

