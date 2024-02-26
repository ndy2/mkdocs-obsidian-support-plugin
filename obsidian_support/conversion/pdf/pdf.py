import re
from inspect import cleandoc

from mkdocs.structure.pages import Page
from overrides import override

from obsidian_support.conversion.abstract_conversion import AbstractConversion, SyntaxGroup

"""
a strategy that convert obsidian #embed pdf (refer https://help.obsidian.md/Linking+notes+and+files/Embed+files#Embed%20a%20PDF%20in%20a%20note)
to embed pdf (refer https://www.w3docs.com/snippets/html/how-to-embed-pdf-in-html.html) in html
"""


class PdfConversion(AbstractConversion):

    @property
    @override
    def obsidian_regex_pattern(self):
        # OBSIDIAN_EMBED_PDF_REGEX
        return re.compile(r"!\[\[(?P<pdf_path>[^|^\]]+\.pdf)(?P<tags>#height=\d+)?]]")

    @override
    def convert(self, syntax_groups: SyntaxGroup, page: Page) -> str:
        base_path = page.canonical_url[:-len(page.url)]
        return self._convert_tags(page, base_path, *syntax_groups)

    def _convert_tags(self, page,  base_path: str, pdf_path: str, tags: str) -> str:
        if tags is None:
            height = 800
        else:
            height = int(tags[8:])

        return cleandoc(f"""
        page.url = {page.url} <br>
        page.abs_url = {page.abs_url} <br>
        page.canonical_url = {page.canonical_url} <br>
        page.edit_url = {page.edit_url} <br>
        <br>
        page.file.url = {page.file.url} <br>
        page.file.src_path = {page.file.src_path} <br>
        page.file.abs_src_path = {page.file.abs_src_path} <br>
        page.file.dest_path = {page.file.dest_path} <br>
        page.file.abs_dest_path = {page.file.abs_dest_path} <br>
        <br>
        
        <object data="{base_path}{pdf_path}" type="application/pdf" width="100%" height="{height}px" >
            <embed src="{base_path}{pdf_path}" type="application/pdf" width="100%" height="{height}px"/>
        </object>
        """)
