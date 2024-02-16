# mkdocs-obsidian-support-plugin
---
Plugin for [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) to convert semantic in documentation from [obsidian](https://obsidian.md/) to mkdocs-material.

[![PyPI](https://img.shields.io/pypi/v/mkdocs-obsidian-support-plugin)](https://pypi.org/project/mkdocs-obsidian-support-plugin/)
[![GitHub](https://img.shields.io/github/license/ndy2/mkdocs-obsidian-support-plugin)](https://github.com/ndy2/mkdocs-obsidian-support-plugin/blob/main/LICENSE.md)

```text
pip install mkdocs-obsidian-support-plugin
```

## Usage
Activate the plugin in mkdocs.yml 
```yaml
plugins:
  - obsidian-support
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

## features 
-  `obsidian callout` -> `mkdocs-material admonition`
-  `obsidian wikilink image` -> `mkdocs-material mdlink image` & `image with md_in_html`
-  `obsidian tags` -> `mkdocs-material search`

## github-pages

> [!info]
> 
> See https://ndy2.github.io/mkdocs-obsidian-support-plugin/ for more details
