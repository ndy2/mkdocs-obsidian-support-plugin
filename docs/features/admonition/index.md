---
title: Admonition
---
  
> [!note]  feature - admonition
> convert `obsidian callout` to `mkdocs-material admonition`
> 
> - [obsidian callout](https://help.obsidian.md/Editing+and+formatting/Callouts)
> - [mkdocs-material admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)

See [Demo](demo) for more examples
## Basic Usage

###  obsidian callout

=== "obsidian markdown"

    ```
    > [!note] haha
    > I am obsidian callout!
    > 
    > I became mkdocs admonition!
    ```

=== "obsidian rendered"

     ![[images/1.png]]


### mkdocs-material admonition

=== "mkdocs-material markdown"

    ```
    !!!note "haha"
    
        I am obsidian callout!
        I became mkdocs admonition!
    ```

=== "mkdocs-material rendered"

    !!!note "haha"
    
        I am obsidian callout!
        
        I became mkdocs admonition!



## Foldable/Collapsible

###  obsidian callout

=== "obsidian markdown"

    ```
    > [!faq]- Are callouts foldable? 
    > Yes! In a foldable callout, the contents are hidden when the callout is collapsed.
    ```

=== "obsidian rendered"

     ![[images/2.png]]

### mkdocs-material admonition

=== "mkdocs-material markdown"

    ```
    ??? note "Are callouts foldable?"
    
        Yes! In a foldable callout, the contents are hidden when the callout is collapsed.
    ```

=== "mkdocs-material rendered"

    ??? note "Are callouts foldable?"
    
        Yes! In a foldable callout, the contents are hidden when the callout is collapsed.


## 💡 Notes

common types that `obsidian callout` and `mkdocs-material admonition` support are

-   note
-   abstract
-   info
-   tip
-   success
-   question
-   warning
-   failure
-   danger
-   bug
-   example
-   quote

common types that `obsidian callout`, `mkdocs-material admonition` and even `GitHub Docs alert` support are

- note
- tip
- warning

## Implementation details and Warning

> [!warning] implementation limitation
> 1. Nested callout or admonition is not suppoerted
> 
> 2. Unlike actual obsidian callout, It requires more precise syntax. <br>
>    there sholud be only zero or one space before and after first  `>` character <br>
>    and no space before the rest of `>` characters and one space after it.
> 
>   recommended format is as below
> ```text
> > [!info]
> > copy me 
> ```


