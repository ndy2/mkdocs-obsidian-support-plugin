from abc import *
from typing import List

from mkdocs.structure.pages import Page
from overrides import final

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

    @property
    @abstractmethod
    def obsidian_regex_pattern(self):
        pass

    @property
    @final
    def obsidian_regex_groups(self):
        return list(self.obsidian_regex_pattern.groupindex.keys())

    @abstractmethod
    def convert(self, syntax_groups: SyntaxGroup, page: Page) -> str:
        pass
