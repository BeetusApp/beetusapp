"This is the main module for the beetus application"
# pylint: disable=E0401:import-error
import sqlite3
import plotly.express as px


DATABASE = "beetus.db"
def create_connection(data_base):
    'Function to connect to database'
    conn = None
    connection_error = None
    try:
        conn = sqlite3.connect(data_base)
    except connection_error as error:
        print(error)

    return conn

# print list of entries
def select_all_entries(conn):
    'test'

    cur = conn.cursor()
    cur.execute("SELECT * FROM entries")

    rows = cur.fetchall()

    for row in rows:
        print(row)

# print list of entries
def select_all_date(conn):
    'test'

    x = []
    cur = conn.cursor()
    cur.execute("SELECT date FROM entries")

    rows = cur.fetchall()

    for row in rows:
        x.append(row[0])
    return x

def select_all_glucose(conn):
    'test'

    y = []
    cur = conn.cursor()
    cur.execute("SELECT glucose FROM entries")

    rows = cur.fetchall()

    for row in rows:
        y.append(row[0])
    return y


# write entries to DB



#Graph and display readings
def generate_graph(date_reading, gluclose_reading):
    'test'
    fig = px.line(x=date_reading, y=gluclose_reading, template="plotly_dark",
                    labels={
                        "x": "Date and Time",
                        "y": "Blood Glucose Reading",
                    },
                    title="Blood Glucose Chart")
    fig.show()

connection = create_connection(DATABASE)

date = select_all_date(connection)
glucose = select_all_glucose(connection)

generate_graph(date, glucose)
# Write reading to HTML page
#fig.write_html("graph.html")
