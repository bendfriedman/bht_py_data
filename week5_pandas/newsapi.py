from flask import Flask, jsonify

app = Flask(__name__)
news = {"zeit": ["Schlagzeile 1", "Schlagzeile 2"],
        "taz": ["Schlagzeile 1", "Schlagzeile 2"]}


@app.route("/newsapi/<newspaper_id>")
def get_news(newspaper_id):
    if newspaper_id not in news:
        return jsonify({"error": "unbekannte Zeitung"}), 404
    return jsonify({"headlines": news[newspaper_id]})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)
