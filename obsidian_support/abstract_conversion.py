import re
from abc import *

from typing import List
from mkdocs.structure.pages import Page

# a list of string that implies the syntax groups in regex
SyntaxGroup = List[str]

"""
An abstract class that implies a conversion from `obsidian syntax` to `mkdocs-material syntax`

It contains
 - self.obsidian_regex : an regex that implies `obsidian syntax`
 - @abstractmethod convert : an abstract method that convert `obsidian syntax` to `mkdocs-material syntax`

Every conversion should extends this class
"""


class AbstractConversion(metaclass=ABCMeta):

    def __init__(self, regex, regex_groups):
        self.obsidian_regex_pattern = re.compile(regex)
        self.obsidian_regex_groups = regex_groups

    @abstractmethod
    def convert(self, syntax_groups: SyntaxGroup, page: Page) -> str:
        pass
