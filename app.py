from flask import (
    Flask,
    jsonify,
    request,
    render_template,
    make_response,
)
import subprocess


app = Flask(__name__)


@app.route("/")
def home():
    resp = make_response(
        render_template(
            "index.html",
        )
    )
    return resp


@app.route("/ping", methods=["POST"])
def ping():
    data = request.json
    print(data.get("hostname"))
    if not data.get("hostname"):
        return jsonify({"error": "Missing hostname"})
    command = f"ping -c 1 {data.get('hostname')}"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()[0].decode("utf-8")
    print(output)

    result = {
        "result": output,
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
