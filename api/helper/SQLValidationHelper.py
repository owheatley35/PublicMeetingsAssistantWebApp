import re

USER_ID_PATTERN = re.compile("^([a-z0-9]*)$")


# Meetings validation
def validate_user_id(user_id: str) -> bool:
    return isinstance(user_id, str) and USER_ID_PATTERN.match(user_id)


def validate_meeting_id(meeting_id) -> bool:
    return isinstance(meeting_id, int) and meeting_id > 0
