---
title: Tabs
comments: true
---
> [!note]  feature - tags
> Convert `obsidian html-tabs` to `mkdocs-material content tab`
>
> - [obsidian html-tabs](https://github.com/ptournet/obsidian-html-tabs)
> - [mkdocs-material Content tabs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/)

## Usage

### obsidian html-tabs

=== "obsidian html-tabs"

~~~~
```tabs
---tab First *tab*
This is a *sample* **tab** with some markdown :
## Heading 2
- [ ] Task 1
- [ ] Task 2

### Heading 3
* Sed sagittis eleifend rutrum
* Donec vitae suscipit est
* Nulla tempor lobortis orci

---tab Second tab
This tab has a code block:
~~~cpp
include <iostream>
using namespace std;

int main() {
 char c;
 cout << "Enter a character: ";
 cin >> c;
 cout << "ASCII Value of " << c << " is " << int(c);
 return 0;
}
~~~
---tab Last tab
This tab contains callout
> [!note] tab with callout!
> callout content
```
~~~~

=== "obsidian rendered"

![[obsidian-html-tabs.gif]]

### mkdocs-material content tabs

**mkdocs markdown**

~~~~
=== "First *tab*"
    
    This is a *sample* **tab** with some markdown :
    ## Heading 2
    - [ ] Task 1
    - [ ] Task 2
    
    ### Heading 3
    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci
    
=== "Second tab"
    
    This tab has a code block:
    ~~~cpp
    include <iostream>
    using namespace std;
    
    int main() {
     char c;
     cout << "Enter a character: ";
     cin >> c;
     cout << "ASCII Value of " << c << " is " << int(c);
     return 0;
    }
    ~~~
    
=== "Last tab"

    This tab contains callout
    !!! note "tab with callout!"
    
        callout content
~~~~


**rendered**

```tabs
---tab First *tab*
This is a *sample* **tab** with some markdown :
## Heading 2
- [ ] Task 1
- [ ] Task 2

### Heading 3
* Sed sagittis eleifend rutrum
* Donec vitae suscipit est
* Nulla tempor lobortis orci

---tab Second tab
This tab has a code block:
~~~cpp
include <iostream>
using namespace std;

int main() {
 char c;
 cout << "Enter a character: ";
 cin >> c;
 cout << "ASCII Value of " << c << " is " << int(c);
 return 0;
}
~~~
---tab Last tab
This tab contains callout
> [!note] tab with callout!
> callout content
```
