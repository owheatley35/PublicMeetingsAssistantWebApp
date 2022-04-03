import re
from datetime import datetime
from typing import List

from api.Constants import STRING_SPLITTER


def break_string_into_list(list_string: str) -> List[str]:
    temp_list = list_string.split(STRING_SPLITTER)
    del temp_list[0]
    return temp_list


def convert_list_into_string(list_in: List[str]) -> str:
    return STRING_SPLITTER + STRING_SPLITTER.join(list_in)


def convert_str_to_datetime(meeting_date: str, meeting_time: str) -> datetime:
    split_date = meeting_date.split('-')
    split_time = meeting_time.split(':')

    year: int = int(split_date[0])
    month: int = int(split_date[1])
    day: int = int(split_date[2])
    hour: int = int(split_time[0])
    mins: int = int(split_time[1])

    return datetime(year, month, day, hour, mins, 0, 0)


def convert_list_to_comma_seperated_string(str_list: List[str]) -> str:
    return ",".join(str_list)


def convert_comma_seperated_string_to_list(string: str) -> List[str]:
    string_list = string.split(',')

    if "" in string_list:
        string_list.remove("")

    if " " in string_list:
        string_list.remove(" ")

    return string_list
