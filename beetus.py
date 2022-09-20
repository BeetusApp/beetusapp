"test"
from flask import Flask, request, jsonify, render_template
import beetusapp.beetusapp_lib


DATABASE = "beetus.db"
PATH_GRAPH = "./graph.html"

# Write reading to HTML page


app = Flask(__name__)


@app.route("/graph", methods=['GET', 'POST'])
def generate_graph():
    "Function to generate graph"
    if request.method == 'POST':
        connection = beetusapp.beetusapp_lib.create_connection(DATABASE)
        date = beetusapp.beetusapp_lib.select_all_date(connection)
        glucose = beetusapp.beetusapp_lib.select_all_glucose(connection)
        beetusapp.beetusapp_lib.generate_graph(date, glucose)
        connection.close()
        return "Graph Generated"
    if request.method == 'GET':
        return app.send_static_file("graph.html")
    return "TEST"


@app.route("/entry", methods=['GET', 'POST'])
def post_entry():
    "POST to create entry, GET to view entries"
    if request.method == 'POST':
        content = request.json
        connection = beetusapp.beetusapp_lib.create_connection(DATABASE)
        date = content['date']
        time = content['time']
        glucose_reading = content['glucose_reading']
        notes = content['notes']
        beetusapp.beetusapp_lib.add_entry(
            connection, date, time, glucose_reading, notes
        )
        connection.close()
        return jsonify(content)
    if request.method == 'GET':
        connection = beetusapp.beetusapp_lib.create_connection(DATABASE)
        cur = connection.cursor()
        cur.execute("SELECT * FROM entries")

        rows = cur.fetchall()
        return rows
    return "TEST"


@app.route('/')
def test():
    "Root route"
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def entry_form():
    "Root route"
    if request.method == 'GET':
        return render_template('entry_form.html')
    if request.method == 'POST':
        date = request.form.get('date')
        time = request.form.get('time')
        glucose_reading = request.form.get('glucose_reading')
        notes = request.form.get('notes')
        connection = beetusapp.beetusapp_lib.create_connection(DATABASE)
        beetusapp.beetusapp_lib.add_entry(
            connection, date, time, glucose_reading, notes
        )
        connection.close()
        return 'ENTRY SUBMITTED'
    return "TEST"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
