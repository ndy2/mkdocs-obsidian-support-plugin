# mkdocs-obsidian-support-plugin
---
Plugin for [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) to convert semantic in documentation
from [obsidian](https://obsidian.md/) to mkdocs-material.

[![\PyPI](https://img.shields.io/pypi/v/mkdocs-obsidian-support-plugin)](https://pypi.org/project/mkdocs-obsidian-support-plugin/)
[![\PyPi Downloads](https://img.shields.io/pypi/dm/mkdocs-obsidian-support-plugin.svg)](https://pypi.org/project/mkdocs-obsidian-support-plugin/)
[![\GitHub](https://img.shields.io/github/license/ndy2/mkdocs-obsidian-support-plugin)](https://github.com/ndy2/mkdocs-obsidian-support-plugin/blob/main/LICENSE)

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

- `obsidian callout/block styled admonition` -> `mkdocs-material admonition`
- `obsidian comment` -> `html comment`
- `obsidian wikilink image` -> `mkdocs-material mdlink image` & `image with md_in_html`
- `obsidian embed pdf` -> `html embed pdf`
- `obsidian tags` -> `mkdocs-material search`
- `obsidian html-tabs` -> `mkdocs-material content tabs`

> [!note]
>
> Some features **require setup** to activate it.
> If you interested in specific feature, see the documentation.

## github-pages

> [!tip]
>
> See https://ndy2.github.io/mkdocs-obsidian-support-plugin/ for more details

### Other plugins that helps mkdocs + obsidian

- https://github.com/sondregronas/mkdocs-callouts
- https://github.com/orbikm/mkdocs-ezlinks-plugin
