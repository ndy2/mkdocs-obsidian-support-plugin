import dataclasses
import re
from typing import Tuple, List

CODE_BLOCK_PATTERN = re.compile(r'(?P<code_block>^[`~]{3,})(?P<language>[a-zA-Z\-]*)?', re.MULTILINE)
BACKQUOTES_CODE_PATTERN = re.compile(r"`[^\n`]+`")


@dataclasses.dataclass
class CodeBlockSyntax:
    start: int
    end: int
    code_block_type: str
    language: str


def get_exclude_indices(markdown: str) -> List[Tuple[int, int]]:
    # setup
    exclude_indices = []
    code_block_matches = {}

    # step 1
    # get all lines stars with more than three of ` or ~
    # and group it by its size
    for code_block_match in CODE_BLOCK_PATTERN.finditer(markdown):
        code_block_syntax = code_block_match.group("code_block")
        size = len(code_block_syntax)
        code_block_type = code_block_syntax[0]
        start = code_block_match.start()
        end = code_block_match.end()
        language = code_block_match.group("language")

        if size not in code_block_matches:
            code_block_matches[size] = []
        code_block_matches[size].append(CodeBlockSyntax(start, end, code_block_type, language))

    # step 2
    # loop the code_block_matches in desc sorted by its size
    for code_block_size in sorted(code_block_matches.keys(), reverse=True):
        code_block_matches_with_same_size = code_block_matches[code_block_size]
        current_syntax = None
        nested_code_block_syntax = None

        # filter already excluded code_block_matches
        code_block_matches_with_same_size = [it for it in code_block_matches_with_same_size if
                                             not is_overlapped(it.start, it.end, exclude_indices)]
        for code_block_syntax in code_block_matches_with_same_size:
            if current_syntax is None:
                current_syntax = code_block_syntax
            elif current_syntax.code_block_type == code_block_syntax.code_block_type and \
                    not is_overlapped(current_syntax.start, code_block_syntax.end, exclude_indices):
                # do not exclude if its ad or tabs block
                if not current_syntax.language.startswith("ad-") and not current_syntax.language == "tabs":
                    exclude_indices.append((current_syntax.start, code_block_syntax.end))
                current_syntax = None
            elif (current_syntax.language.startswith("ad-") or current_syntax.language == "tabs") and \
                    current_syntax.code_block_type != code_block_syntax.code_block_type and \
                    nested_code_block_syntax is None:
                nested_code_block_syntax = code_block_syntax
            elif nested_code_block_syntax is not None and \
                    code_block_syntax.code_block_type == nested_code_block_syntax.code_block_type:
                if not nested_code_block_syntax.language.startswith("ad-") and \
                        not nested_code_block_syntax.language == "tabs":
                    exclude_indices.append((nested_code_block_syntax.start, code_block_syntax.end))
                nested_code_block_syntax = None

    # step 3
    # exclude backquotes_codes (``)
    for code_match in re.finditer(BACKQUOTES_CODE_PATTERN, markdown):
        if not is_overlapped(code_match.start(), code_match.end(), exclude_indices):
            exclude_indices.append((code_match.start(), code_match.end()))

    return exclude_indices


def is_overlapped(start: int, end: int, exclude_indices_pairs: List[tuple]) -> bool:
    for exclude_indices_pair in exclude_indices_pairs:
        if exclude_indices_pair[0] <= start and end <= exclude_indices_pair[1]:
            return True
    return False
