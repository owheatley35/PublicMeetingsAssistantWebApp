from mysql.connector.cursor_cext import CMySQLCursor
from sshtunnel import SSHTunnelForwarder

from api.database.DBConfiguration import DBConfiguration
from mysql.connector import connect


class DatabaseConnectionHelper:
    """
    Class to create and manage the SSH Tunnel and MySLQ DB connection.
    """

    def __init__(self, configuration: DBConfiguration):
        """
        Creates an SSH Tunnel and establish a Db Connection

        :param configuration: DBConfiguration Details
        """
        self._configuration = configuration
        self._tunnel: SSHTunnelForwarder = self._create_tunnel()
        print("SSH Tunnel Established")
        self._connection = self._establish_connection()
        print("MySQL DB Connection Established")

    def get_connection_cursor(self) -> CMySQLCursor:
        """
        Retrieve the connection cursor

        :return: The connection cursor from the connection helper
        """
        return self._connection.cursor()

    def commit_connection(self) -> None:
        """
        Run the commit command on the ssh connection.
        Required when running insert or update SQL commands.

        :return: None
        """
        self._connection.commit()

    def close_connection(self) -> None:
        """
        Close the connection to the database and the EC2 instance if the connections and ssh tunnels are open.

        :return: None
        """

        if self._connection.is_connected():
            self._connection.close()
            print("DB Connection Closed Successfully")
        if self._tunnel.is_active:
            self._tunnel.close()
            print("SSH Tunnel Closed Successfully")

    def is_connection_open(self) -> bool:
        """
        Checks if a connection to the database exists and if a tunnel is active to the EC2 instance

        :return: boolean whether a connection is active
        """
        return self._connection.is_connected() and self._tunnel.is_active

    def _create_tunnel(self) -> SSHTunnelForwarder:
        """
        Creates an SSH tunnel using the details provided to the constructor.

        :return: an SSH Tunnel Configuration (Not open)
        """
        return SSHTunnelForwarder(
            self._configuration.get_ec2_dns(),
            ssh_username=self._configuration.get_ssh_username(),
            ssh_pkey=self._configuration.get_ssh_code_path(),
            remote_bind_address=self._configuration.get_db_host_with_port()
        )

    def _establish_connection(self):
        """
        Opens the SSH tunnel and uses it to establish a connection to the SQl database

        :return: Connection to MySQL database
        """
        self._tunnel.start()

        return connect(
            user=self._configuration.get_db_username(),
            password=self._configuration.get_db_password(),
            host=self._configuration.get_ec2_connection_host(),
            port=self._tunnel.local_bind_port
        )
