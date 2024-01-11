---
title: Admonition-Collapsable
---
 
> [!note]  feature - admonition-collapsable
> convert `obsidian collapsable callout` to `mkdocs-material admonition`

### Foldable callouts

#### Collapsed

- raw text
```
> [!faq]- Are callouts foldable? 
> > Yes! In a foldable callout, the contents are hidden when the callout is collapsed.
```

- converted text
```
??? note "<title>"

    <lines>
```

- displayed

> [!faq]- Are callouts foldable? 
> Yes! In a foldable callout, the contents are hidden when the callout is collapsed.

#### Expanded

- raw text

```
> [!faq]+ Are callouts foldable? 
> > Yes! In a foldable callout, the contents are hidden when the callout is collapsed.
```

- converted to
```
??? note "<title>"

    <lines>
```

- displayed

> [!faq]+ Are callouts foldable? 
> Yes! In a foldable callout, the contents are hidden when the callout is collapsed.


