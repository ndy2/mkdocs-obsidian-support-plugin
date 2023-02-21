
## Admonition

> [!note]  feature - admonition
> convert `obsidian callout' to `mkdocs-material admonition`

###  [obsidian callout](https://help.obsidian.md/Editing+and+formatting/Callouts)

=== "obsidian markdown"

    ```
    > [!note] haha
    > I am obsidian callout!
    > 
    > I became mkdocs admonition!
    ```
    this is a none bug it convert call out even if it is in a codeblock.
    will be fixed

=== "obsidian rendered"

    ![[images/1.png]]


### [mkdocs-material admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions)

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

> [!info] haha

> [!info]

