"This is the main module for the beetus application"
# pylint: disable=E0401:import-error
import sqlite3
import plotly.express as px


def add_numbers(num_one, num_two):
    "test"
    return num_one + num_two


def create_connection(data_base):
    "Function to connect to database"
    conn = None
    connection_error = None
    try:
        conn = sqlite3.connect(data_base)
    except connection_error as error:
        print(error)

    return conn


# print list of entries
def select_all_entries(conn):
    "test"

    cur = conn.cursor()
    cur.execute("SELECT * FROM entries")

    rows = cur.fetchall()

    for row in rows:
        print(row)


# Print list of all date readings and return list
def select_all_date(conn):
    "test"

    date_list = []
    cur = conn.cursor()
    cur.execute("SELECT date FROM entries")

    rows = cur.fetchall()

    for row in rows:
        date_list.append(row[0])
    return date_list


# Print list of all glucose readings and return list
def select_all_glucose(conn):
    "test"

    glucose_list = []
    cur = conn.cursor()
    cur.execute("SELECT glucose FROM entries")

    rows = cur.fetchall()

    for row in rows:
        glucose_list.append(row[0])
    return glucose_list


# write entries to DB


# Graph and display readings
def generate_graph(date_reading, gluclose_reading):
    "test"
    fig = px.line(
        x=date_reading,
        y=gluclose_reading,
        template="plotly_dark",
        labels={
            "x": "Date and Time",
            "y": "Blood Glucose Reading",
        },
        title="Blood Glucose Chart",
    )
    fig.show()
    fig.write_html("./static/graph.html")
