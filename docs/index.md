---
title: README
---

Plugin for [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) to convert semantic in documentation
from [obsidian](https://obsidian.md/) to mkdocs-material.

[![\PyPI](https://img.shields.io/pypi/v/mkdocs-obsidian-support-plugin)](https://pypi.org/project/mkdocs-obsidian-support-plugin/)
[![\GitHub](https://img.shields.io/github/license/ndy2/mkdocs-obsidian-support-plugin)](https://github.com/ndy2/mkdocs-obsidian-support-plugin/blob/main/LICENSE.md)

```text
pip install mkdocs-obsidian-support-plugin
```

## Usage

Activate the plugin in mkdocs.yml

```yaml
plugins:
  - obsidian-support
```

## features

- `obsidian callout` -> `mkdocs-material admonition`
- `obsidian block styled callout` -> `mkdocs-material admonition`
- `obsidian wikilink image` -> `mkdocs-material mdlink image` & `image with md_in_html`
- `obsidian tags` -> `mkdocs-material search`

> [!note]
>
> Some features **require setup** to activate it.
> If you interested in specific feature, see the documentation.

### Other plugins that helps mkdocs + obsidian

- https://github.com/sondregronas/mkdocs-callouts
- https://github.com/orbikm/mkdocs-ezlinks-plugin