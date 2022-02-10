"""
All logic related to the module's main application
Mostly only this file requires changes
"""

from app.config import APPLICATION
from hdbcli import dbapi

def parseColumnHeaders():
    if APPLICATION['HDB_HEADERS']:
        headers = [header.strip() for header in APPLICATION['HDB_HEADERS'].split(',')]
    else:
        headers = None
    return headers

def parseDataLabels():
    if APPLICATION['LABELS']:
        labels = [label.strip() for label in APPLICATION['LABELS'].split(',')]
    else:
        labels = None
    return labels

def connectToSAPHANA():
    try:
        conn = dbapi.connect(
            address=APPLICATION['HDB_ADDRESS'],
            port=APPLICATION['HDB_PORT'],
            user=APPLICATION['HDB_USER'],
            password=APPLICATION['HDB_PASSWORD']
        )
        return conn
    except Exception:
        return None

SCHEMA = APPLICATION['HDB_SCHEMA']
TABLE = APPLICATION['HDB_TABLE']
HEADERS = parseColumnHeaders()
LABELS = parseDataLabels()
# open the database connection
CONN = connectToSAPHANA()
if CONN:
    # prepare a cursor object
    CURSOR = CONN.cursor()
else:
    CURSOR = None

def module_main(data):
    """
    Implement module logic here. Although this function returns data, remember to implement
    egressing method to external database or another API.

    Args:
        data ([JSON Object]): [Data received by the module and validated by data_validation function]

    Returns:
        [string, string]: [data, error]
    """

    # https://blogs.sap.com/2021/07/20/connecting-hana-db-using-python-language/
    # https://www.youtube.com/watch?v=lnhlegJDT2Q

    try:
        global HEADERS
        global LABELS
        global CURSOR

        if not HEADERS:
            return None, "Database column headers not provided"
        if not LABELS:
            return None, "Data labels not provided"
        if len(HEADERS) != len(LABELS):
            return None, "Number of provided database column headers in not matchin a number of provided data labels"
        if not CURSOR:
            return None, "Cannot connect to SAP HANA, check provided API details and authentication credentials"
        
        if isinstance(data, dict):
            insertData(data)
        elif isinstance(data, list):
            for d in data:
                insertData(d)        

        return data, None
    except Exception:
        return None, "Unable to perform the module logic"

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