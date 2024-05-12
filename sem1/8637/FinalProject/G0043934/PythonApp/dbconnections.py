import pymysql
import pandas as pd
from neo4j import GraphDatabase

def run_in_mysql(query):
    """
    Given a Query, the function connects to the Database and runs the Query, returning a dataframe of that output.
    """
    global conn
    conn = None

    def connect():
        global conn
        conn = pymysql.connect(host="localhost", user="root", password="root", db="appdbproj", cursorclass=pymysql.cursors.DictCursor)

    if not conn:
        connect()

    cursor = conn.cursor()
    cursor.execute(query)
    x = cursor.fetchall()

    cursor.close()
    conn.close()

    df = pd.DataFrame(x)

    return df

from neo4j import GraphDatabase

def run_in_neo4j(query):
    # Establish connection
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

    # Create a session to run the query
    with driver.session() as session:
        result = session.run(query)

        # Convert the result into a list of dictionaries
        records = [record for record in result]

    return records
