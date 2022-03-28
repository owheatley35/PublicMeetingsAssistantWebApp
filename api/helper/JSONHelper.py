import json
from typing import List


def convert_custom_object_list_to_dict(input_list: List[any]) -> List[dict]:
    new_list = []

    for item in input_list:
        new_list.append(item.__dict__)

    return new_list


def convert_custom_object_to_dict(input_object: any) -> dict:
    return input_object.__dict__
