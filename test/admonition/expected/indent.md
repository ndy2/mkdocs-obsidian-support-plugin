### Obsidian Callout to Mkdocs-material Admonition Conversion Indent Tests

1. indent : 0,0
!!! note

>basic admonition conversion test

2. indent : 0,1
!!! note

    basic admonition conversion test

3. indent : 1,0
!!! note

 >basic admonition conversion test

4. indent : 1,1
!!! note

 > basic admonition conversion test

5. indent : 2,0 - do not convert
  >[!note]
  >basic admonition conversion test

6. indent : 2,1 - do not convert
  > [!note]
  > basic admonition conversion test

7. indent : 3,0 - do not convert
   >[!note]
   >basic admonition conversion test

8. indent : 3,1 - do not convert
   > [!note]
   > basic admonition conversion test

9. indent : 4,0 - do not convert
    >[!note]
    >basic admonition conversion test

10. indent : 4,1 - do not convert
    > [!note]
    > basic admonition conversion test
