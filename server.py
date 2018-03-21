from flask import Flask, render_template, request, session, redirect, url_for


app = Flask(__name__)


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )