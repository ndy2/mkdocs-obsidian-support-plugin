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



## Foldable/Collsapsible

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

common types that `obsidian callout` and `mkdocs-material admonition` support are

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

## Implementation details and Warning

It extracts obsidian call out from markdown using below regular expression 

```
\n ?> ?\\[!(?P<type>[a-z]+)\\](?P<title> .*)?(?P<lines>(\n ?>.*)*)
```

and create admonition using the groups (`type`, `title`, `lines`) of the match results.

Implementation code at [here](https://github.com/ndy2/mkdocs-obsidian-support-plugin/blob/main/obsidian_support/conversion/admonition.py)

As you might noticed that actual obsidian callout has more flexible rendering condition than above regex.  It allows some more spaces and so on.

For implementation convenience, above regex allows zero or one space before and after `>`'character. And it begins with a new line character `\n`. So, in case of your markdown begins with call out, it does not work as expected.

 > [!warning] implementation limitation
> 1. `type` must be written in lowercase : `info` , ~~`Info`~~
>    
> 2. It does not work if your markdown starts with the `callout` it self.  add dummy new link at the beginning of your markdown will fix it.
>    
> 3. Nested callout or admonition is not suppoerted
> 
> 4. Unlike actual obsidian callout, It requires more precise syntax. <br>
>    there sholud be only zero or one space before and after first  `>` character <br>
>    and no space before the rest of `>` characters and one space after it.
>    
>    recommended format is as below
> ```text
> > [!info]
> > copy me 
> ```


