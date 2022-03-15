from os.path import exists

from mysql.connector import connect

from api.database.DBConfiguration import DBConfiguration
from sshtunnel import SSHTunnelForwarder

query = """SELECT * from exampleDatabase.users"""


def get_all_data():

    print("Does File Exist: " + str(exists("res/dbec2keypair.pem")))

    with SSHTunnelForwarder(
            DBConfiguration.ec2_dns,
            ssh_username=DBConfiguration.ssh_username,
            ssh_pkey="res/dbec2keypair.pem",
            remote_bind_address=DBConfiguration.db_host
    ) as tunnel:
        tunnel.start()
        print("****SSH Tunnel Established****")

        # db = pymysql.connect(
        #     host=DBConfiguration.ec2_host, user=DBConfiguration.db_username,
        #     password=DBConfiguration.db_password, port=tunnel.local_bind_port
        # )

        conn = connect(
            user=DBConfiguration.db_username,
            password=DBConfiguration.db_password,
            host="localhost",
            port=tunnel.local_bind_port,
        )

        result = []

        # Run sample query in the database to validate connection
        try:
            # Print all the databases
            with conn.cursor() as cur:
                cur.execute(query)
                for r in cur:
                    result.append(r)
                    print(r)
        finally:
            conn.close()
            tunnel.close()

        return result
