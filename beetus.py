"test"
from flask import Flask, request, jsonify
import beetusapp.beetusapp_lib


DATABASE = "beetus.db"
connection = beetusapp.beetusapp_lib.create_connection(DATABASE)
date = beetusapp.beetusapp_lib.select_all_date(connection)
glucose = beetusapp.beetusapp_lib.select_all_glucose(connection)
beetusapp.beetusapp_lib.generate_graph(date, glucose)
connection.close()

# Write reading to HTML page

PATH_GRAPH = "./graph.html"
app = Flask(__name__)


@app.route("/noob")
def hello_world():
    "test"
    # return "<p>Hello, World!</p>"
    # return url_for('static', filename="graph.html")
    return app.send_static_file("graph.html")

@app.route("/entry", methods = ['POST'])
def post_entry():
    "test"
    content = request.json
    connection = beetusapp.beetusapp_lib.create_connection(DATABASE)
    date = content['date']
    time = content['time']
    glucose_reading = content['glucose_reading']
    notes = content['notes']
    beetusapp.beetusapp_lib.add_entry(connection, date, time, glucose_reading, notes)
    connection.close()
    #return jsonify({"Date":date},{"Time":time},{"Glucose_Reading":glucose_reading}, {"Notes":notes})
    return jsonify(content)

@app.route('/')
def test_root():
    "Root route"
    return 'This is the root page'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
