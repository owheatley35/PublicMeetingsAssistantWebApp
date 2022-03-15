
from sshtunnel import SSHTunnelForwarder

from api.database.DBConfiguration import DBConfiguration
from mysql.connector import connect


class DatabaseConnectionHelper:
    """
    Class to create and manage the SSH Tunnel and MySLQ DB connection.
    """

    def __init__(self, configuration: DBConfiguration):
        self._configuration = configuration
        self._tunnel: SSHTunnelForwarder = self._create_tunnel()
        print("SSH Tunnel Established")
        self._connection = self._establish_connection()
        print("MySQL DB Connection Established")

    def get_connection_cursor(self):
        return self._connection.cursor()

    def close_connection(self):
        if self._connection.is_connected():
            self._connection.close()
            print("DB Connection Closed Successfully")
        if self._tunnel.is_active:
            self._tunnel.close()
            print("SSH Tunnel Closed Successfully")

    def is_connection_open(self) -> bool:
        return self._connection.is_connected() and self._tunnel.is_active

    def _create_tunnel(self) -> SSHTunnelForwarder:
        return SSHTunnelForwarder(
            self._configuration.get_ec2_dns(),
            ssh_username=self._configuration.get_ssh_username(),
            ssh_pkey=self._configuration.get_ssh_code_path(),
            remote_bind_address=self._configuration.get_db_host_with_port()
        )

    def _establish_connection(self):
        self._tunnel.start()

        return connect(
            user=self._configuration.get_db_username(),
            password=self._configuration.get_db_password(),
            host=self._configuration.get_ec2_connection_host(),
            port=self._tunnel.local_bind_port
        )
