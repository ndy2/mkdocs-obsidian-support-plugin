---
title: Tags
---
> [!note]  feature - tags
> convert `obsidian tags` to `mkdocs-material search`
>
> - [obsidian tags](https://help.obsidian.md/Editing+and+formatting/Tags)
> - [mkdocs-material search](https://squidfunk.github.io/mkdocs-material/setup/setting-up-site-search/)

## Usage

=== "obsidian markdown"

    ```
    This is just an #obsidian tag. Click to go to the search bar
    ```

=== "mkdocs-material rendered"

    This is just an **obsidian**{: .hash} tag. Click to go to the search bar

## How to activate

**TLDR**

see [this PR](https://github.com/ndy2/mkdocs-obsidian-support-plugin/pull/8/files) and apply to your project

By default `obsidian tags` are just shown as bold text. Obsidian style can be activated by using the following css file,
that has to be activated inside the mkdocs.yml.

```css
.hash {
  background-color: #f3eefd;
  border-radius: 20px;
  padding: 5px;
  font-weight: normal;
}

[data-md-color-scheme="slate"] .hash {
  background-color: #292433;
}
```

Activating this inside the mkdocs.yml

```yaml
extra_css:
  - assets/css/obsidian_tags.css
```

By using the following javascript, the search menu will be opened by clicking the tags.

```javascript
$('.hash').each(function() {
  var link = $(this).html();
  $(this).contents().wrap('<a href="?q='+link+'">#</a>');
});
```

This have to be activated inside the mkdocs.yml.

```yaml
extra_javascript:
  - https://code.jquery.com/jquery-3.7.1.min.js
  - assets/javascript/obsidian_tags.js
```
