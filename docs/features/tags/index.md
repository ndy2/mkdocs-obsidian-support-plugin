---
title: Tags
---
 
> [!note]  feature - tags
> convert `obsidian tags` to `mkdocs-material search`
> 
> - [obsidian tags](https://help.obsidian.md/Editing+and+formatting/Tags)
> - [mkdocs-material search](https://squidfunk.github.io/mkdocs-material/plugins/search/)
>  
> Requirements
> - mkdocs-material plugin `search`  
### obsidian tags

=== "obsidian markdown"

    ```
    This is just an #obsidian tag.
    ```

=== "mkdocs-material rendered"

    This is just an **obsidian**{: .hash} tag.

### Escape tag

You may escape conversion by adding backslash in front of the hashtag
`\` work as escape create tagging in both obsidian & mkdocs-material by default

=== "obsidian markdown"

    ```
    This is not an \#obsidian tag.
    ```

=== "mkdocs-material rendered"

    This is not an \#obsidian tag.
