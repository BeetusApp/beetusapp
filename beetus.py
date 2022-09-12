"test"
from flask import Flask
import beetusapp.beetusapp_lib


DATABASE = "beetus.db"
connection = beetusapp.beetusapp_lib.create_connection(DATABASE)
date = beetusapp.beetusapp_lib.select_all_date(connection)
glucose = beetusapp.beetusapp_lib.select_all_glucose(connection)
beetusapp.beetusapp_lib.generate_graph(date, glucose)

# Write reading to HTML page

PATH_GRAPH = "./graph.html"
app = Flask(__name__)


@app.route("/")
def hello_world():
    "test"
    # return "<p>Hello, World!</p>"
    # return url_for('static', filename="graph.html")
    return app.send_static_file("graph.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
