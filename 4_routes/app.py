from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static")

# Serve the AngularJS app
@app.route("/")
def serve_angular():
    return send_from_directory("static", "index.html")

@app.route("/<path:path>")
def serve_static_files(path):
    return send_from_directory("static", path)

@app.errorhandler(404)
def not_found(e):
    return send_from_directory("static", "index.html")

if __name__ == "__main__":
    app.run(debug=True)
