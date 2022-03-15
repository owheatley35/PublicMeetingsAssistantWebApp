class DBConfiguration:
    """
    Class to model all data needed to establish a connection to the MySQL Database.
    """

    def __init__(self, db_host: str, ssh_username: str, ssh_code_path: str, db_username: str, db_password: str,
                 db_port: str, ec2_host: str, ec2_dns: str, db_host_with_port: (str, int), ec2_connection_host: str):
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
