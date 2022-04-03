class DBConfiguration:
    """
    Class to model all data needed to establish a connection to the MySQL Database.
    """

    def __init__(self, db_host: str, ssh_username: str, ssh_code_path: str, db_username: str, db_password: str,
                 db_port: str, ec2_host: str, ec2_dns: str, db_host_with_port: (str, int), ec2_connection_host: str):
        """
        :param db_host: string containing the host for the database
        :param ssh_username: username for the ssh tunnel
        :param ssh_code_path: Path to the file containing the key code for the ssh tunnel
        :param db_username: username for the database
        :param db_password: password for the database
        :param db_port: port number for the database connection
        :param ec2_host: ec2 host url string
        :param ec2_dns: ec2 dns url
        :param db_host_with_port: db host and port
        :param ec2_connection_host: Connection host to the ec2 instance
        """

        self._host = db_host
        self._ssh_username = ssh_username
        self._ssh_code_path = ssh_code_path
        self._db_username = db_username
        self._db_password = db_password
        self._port = db_port
        self._ec2_host = ec2_host
        self._ec2_dns = ec2_dns
        self._db_host_with_port = db_host_with_port
        self._ec2_connection_host = ec2_connection_host

    def get_db_host(self) -> str:
        return self._host

    def get_ssh_username(self) -> str:
        return self._ssh_username

    def get_ssh_code_path(self) -> str:
        return self._ssh_code_path

    def get_db_username(self) -> str:
        return self._db_username

    def get_db_password(self) -> str:
        return self._db_password

    def get_port(self) -> str:
        return self._port

    def get_ec2_host(self) -> str:
        return self._ec2_host

    def get_ec2_dns(self) -> str:
        return self._ec2_dns

    def get_db_host_with_port(self) -> (str, int):
        return self._db_host_with_port

    def get_ec2_connection_host(self) -> str:
        return self._ec2_connection_host
