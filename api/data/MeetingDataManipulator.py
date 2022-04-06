from api.data.DatabaseConnector import DatabaseConnector


class MeetingDataManipulator(DatabaseConnector):

    def __init__(self, user_id: str, meeting_id: int):
        super().__init__()
        self._user_id = user_id
        self._meeting_id = meeting_id
