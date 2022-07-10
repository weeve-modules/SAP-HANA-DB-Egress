"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
from .params import PARAMS
from hdbcli import dbapi

log = getLogger("module")

def parseColumnHeaders():
    if PARAMS['HDB_HEADERS']:
        headers = [header.strip() for header in PARAMS['HDB_HEADERS'].split(',')]
    else:
        headers = None
    return headers

def parseDataLabels():
    if PARAMS['LABELS']:
        labels = [label.strip() for label in PARAMS['LABELS'].split(',')]
    else:
        labels = None
    return labels

def connectToSAPHANA():
    try:
        conn = dbapi.connect(
            address=PARAMS['HDB_ADDRESS'],
            port=PARAMS['HDB_PORT'],
            user=PARAMS['HDB_USER'],
            password=PARAMS['HDB_PASSWORD']
        )
        return conn
    except Exception:
        return None

SCHEMA = PARAMS['HDB_SCHEMA']
TABLE = PARAMS['HDB_TABLE']
HEADERS = parseColumnHeaders()
LABELS = parseDataLabels()
# open the database connection
CONN = connectToSAPHANA()
if CONN:
    # prepare a cursor object
    CURSOR = CONN.cursor()
else:
    CURSOR = None


def module_main(received_data: any) -> str:
    """
    Send received data to the next module by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        str: Error message if error occurred, otherwise None.

    """

    # https://blogs.sap.com/2021/07/20/connecting-hana-db-using-python-language/
    # https://www.youtube.com/watch?v=lnhlegJDT2Q

    log.debug("Outputting ...")

    try:
        # YOUR CODE HERE
        global HEADERS
        global LABELS
        global CURSOR

        if not HEADERS:
            return "Database column headers not provided."
        if not LABELS:
            return "Data labels not provided."
        if len(HEADERS) != len(LABELS):
            return "Number of provided database column headers in not matching a number of provided data labels."
        if not CURSOR:
            return "Cannot connect to SAP HANA, check provided API details and authentication credentials."

        if isinstance(received_data, dict):
            insertData(received_data)
        elif isinstance(received_data, list):
            for d in received_data:
                insertData(d)

        return None

    except Exception as e:
        return f"Exception in the module business logic: {e}"

def insertData(data):
    global HEADERS
    global LABELS
    global SCHEMA
    global TABLE
    global CURSOR

    # build column artefact
    columns = ''
    for h in HEADERS:
        columns += f'"{h}",'
    columns = '(' + columns[:-1] + ')'

    # build values
    values = ''
    for l in LABELS:
        if isinstance(data[l], str):
            values += f"\'{data[l]}\',"
        else:
            values += f"{data[l]},"
    values = '(' + values[:-1] + ')'

    # build SQL Query
    sql_insert = f'INSERT INTO {SCHEMA}.{TABLE} {columns} VALUES {values}'
    CURSOR.execute(sql_insert)
