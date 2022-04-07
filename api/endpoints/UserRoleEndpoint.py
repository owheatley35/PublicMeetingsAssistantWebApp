import logging

from api.data.model.Response import Response
from api.data.provider.UserRoleProvider import UserRoleProvider


class UserRoleEndpoint:

    def __init__(self, user_id: str):
        logging.info("UserRoleEndpoint: Starting Endpoint")

        self._user_id = user_id
        self._role_provider = UserRoleProvider(self._user_id)
        self._endpoint_status = True

    def get_user_role(self) -> Response:
        if self._endpoint_status:
            return Response(True, self._role_provider.get_user_role())
        else:
            logging.warning("Endpoint: UserRoleEndpoint - Closed")
            Response(False)

    def close_endpoint(self) -> None:
        """
        Close the endpoint

        :return: None
        """
        self._role_provider.finish()
        self._endpoint_status = False
        logging.info("UserRoleEndpoint: Endpoint Closed")
