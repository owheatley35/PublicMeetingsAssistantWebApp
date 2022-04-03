
from api.database.DBConfiguration import DBConfiguration
from security.credentials import host, ssh_username, ssh_code_path, db_username, db_password, port, ec2_host, ec2_dns, \
    db_host, ec2_connection_host


class DBConfigurationProvider:
    """
    Retrieves Database configuration details for access from AWS services and provides that data.
    """

    def get_configuration_from_local(self) -> DBConfiguration:
        """
        :return: DBConfiguration object containing all the information required to create a connection to a database.
        """
        return DBConfiguration(host, ssh_username, ssh_code_path, db_username, db_password, port, ec2_host, ec2_dns,
                               db_host, ec2_connection_host)
