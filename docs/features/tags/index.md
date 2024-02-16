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


### How to use

```
TLDR - apply https://github.com/ndy2/mkdocs-obsidian-support-plugin/pull/8/files in your project
```

By default `obsidian tags` are just shown as bold text. Obsidian style can be activated by using the following css file, that has to be activated inside the mkdocs.yml.
```
.hash {
  background-color: #f3eefd;
  border-radius: 20px;
  padding: 5px;
  font-weight: normal;
}
```

Activating this inside the mkdocs.yml
```
extra_css:
  - assets/css/obsidian_tags.css
```

By using the following javascript, the search menu will be opened by clicking the tags.
```
$('.hash').each(function() {
  var link = $(this).html();
  $(this).contents().wrap('<a href="?q='+link+'">#</a>');
});
```

This have to be activated inside the mkdocs.yml.
```
extra_javascript:
  - https://code.jquery.com/jquery-3.7.1.min.js
  - assets/javascript/obsidian_tags.js
```

### Escape tag

You may escape conversion by adding backslash in front of the hashtag
`\` work as escape create tagging in both obsidian & mkdocs-material by default

=== "obsidian markdown"

    ```
    This is not an \#obsidian tag.
    ```

=== "mkdocs-material rendered"

    This is not an \#obsidian tag.
