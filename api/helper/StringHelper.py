from typing import List

from api.Constants import STRING_SPLITTER


def break_string_into_list(list_string: str) -> List[str]:
    temp_list = list_string.split(STRING_SPLITTER)
    del temp_list[0]
    return temp_list


def convert_list_into_string(list_in: List[str]) -> str:
    return STRING_SPLITTER + STRING_SPLITTER.join(list_in)
