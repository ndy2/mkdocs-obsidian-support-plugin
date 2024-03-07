
> [!note]  feature - image-link
> Convert `obsidian embed pdf` to `html embed pdf`
> 
> - [obsidian embed pdf](https://help.obsidian.md/Linking+notes+and+files/Embed+files#Embed%20a%20PDF%20in%20a%20note)
> - [html embed pdf](https://www.w3docs.com/snippets/html/how-to-embed-pdf-in-html.html)

## Usage

### obsidian embed pdf

```tabs
---tab obsidian markdown
~~~
![[features/pdf/a4-sample.pdf]]
~~~

You can also specify the height in pixels for the embedded PDF viewer, by adding `#height=[number]` to the link. like this : `![[features/pdf/a4-sample.pdf#height=400]]`

---tab obsidian rendered
![[images/pdf_1.png]]
```


### html-embed pdf

```tabs
---tab html
~~~
<object data="/features/pdf/a4-sample.pdf" type="application/pdf" width="100%" height="800px" >
    <embed src="/features/pdf/a4-sample.pdf" type="application/pdf" width="100%" height="800px"/>
</object>
~~~
---tab html rendered
![[features/pdf/a4-sample.pdf]]
```


## HTML Template

```html
<object data="/{pdf_path}" type="application/pdf" width="100%" height="{height}px" >  
    <embed src="/{pdf_path}" type="application/pdf" width="100%" height="{height}px"/>  
</object>
```