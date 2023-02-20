# mkdocs-obsidian-support-plugin
---
Plugin for [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) to convert semantic in documentation from [obsidian](https://obsidian.md/) to mkdocs-material.

[![PyPI](https://img.shields.io/pypi/v/mkdocs-obsidian-support-plugin)](https://pypi.org/project/mkdocs-obsidian-support-plugin/)
[![GitHub](https://img.shields.io/github/license/ndy2/mkdocs-obsidian-support-plugin)](https://github.com/ndy2/mkdocs-obsidian-support-plugin/blob/main/LICENSE.md)


```text
pip install mkdocs-obsidian-support-plugin
```

## Usage
---
Activate the plugin in mkdocs.yml 
```yaml
plugins:
  - search
  - obsidian-support
```


## features 
---

### 1. `obsidian callout` -> `mkdocs admonition`
---

in obsidian,
```text
>[!note] haha
>I am obsidian callout!
>
>I became mkdocs admonition!
```
rendered as with [obsidian callout](https://help.obsidian.md/Editing+and+formatting/Callouts)

![img.png](images/obsidian-callout.png)

in mkdocs-material,
this is equivalent to [mkdocs-material admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#custom-admonitions)

```text
!!!note "haha"

    I am obsidian callout!
    
    I became mkdocs admonition!
```

this plugin convert `callout` to `admonition` based on regex.
finally it rendered as below in mkdocs-material

![img.png](images/mkdocs-admonition.png)

💡 common types that `obsidian callout` and `mkdocs-material admonition` support

- note
- abstract
- info
- tip
- success
- question
- warning
- failure
- danger
- bug
- example
- quote
