"test"
from flask import Flask, request, jsonify, render_template
import beetusapp.beetusapp_lib


DATABASE = "beetus.db"
PATH_GRAPH = "./graph.html"

def generate_new_graph():
    "Generate new graph"
    connection = beetusapp.beetusapp_lib.create_connection(DATABASE)
    date = beetusapp.beetusapp_lib.select_all_date(connection)
    glucose = beetusapp.beetusapp_lib.select_all_glucose(connection)
    beetusapp.beetusapp_lib.generate_graph(date, glucose)
    connection.close()

# Write reading to HTML page

# Create graph on boot
generate_new_graph()

app = Flask(__name__)


@app.route("/graph", methods=['GET'])
def generate_graph():
    "Function to generate graph"
    generate_new_graph()
    return app.send_static_file("graph.html")


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
        # pylint: disable=E1101:no-member
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
        return render_template('entries.html', rows=rows)
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
        # pylint: disable=E1101:no-member
        beetusapp.beetusapp_lib.add_entry(
            connection, date, time, glucose_reading, notes
        )
        connection.close()
        return 'ENTRY SUBMITTED'
    return "TEST"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
