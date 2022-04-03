import re

from api.Constants import STRING_SPLITTER

USER_ID_PATTERN = re.compile("^([a-z0-9]*)$")
SCRIPT_TAG_PATTERN = re.compile("<script>.*</script>")


# Meetings validation
def validate_user_id(user_id: str) -> bool:
    return isinstance(user_id, str) and USER_ID_PATTERN.match(user_id) and (len(user_id) <= 255)


def validate_meeting_id(meeting_id) -> bool:
    return isinstance(meeting_id, int) and meeting_id > 0


def validate_input_string(meeting_note: str) -> bool:
    return isinstance(meeting_note, str) and (len(SCRIPT_TAG_PATTERN.findall(meeting_note)) == 0)


def validate_meeting_note(meeting_note: str) -> bool:
    return validate_sql_longtext(meeting_note) and (STRING_SPLITTER not in meeting_note)


def validate_sql_text(text: str) -> bool:
    return validate_input_string(text) and (len(text.encode('utf-8')) < 65535)


def validate_sql_longtext(long_text: str) -> bool:
    return validate_input_string(long_text) and (len(long_text.encode('utf-8')) < 4294967295)
