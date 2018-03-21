from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
get_counter = 0
post_counter = 0
delete_counter = 0
put_counter = 0


@app.route('/')
def index():
    return render_template('index.html', counter=get_counter)


@app.route('/request-counter', methods=['GET', 'POST', 'DELETE', 'PUT'])
def request_counts():
    if request.method == 'GET':
        global get_counter
        get_counter += 1
    if request.method == 'POST':
        global post_counter
        post_counter += 1
    if request.method == 'DELETE':
        global delete_counter
        delete_counter += 1
    if request.method == 'PUT':
        global put_counter
        put_counter += 1
    return redirect('/')


@app.route('/statistics')
def statistics():
    stats = {'GET': get_counter, 'POST': post_counter, 'DELETE': delete_counter, 'PUT': put_counter}
    return render_template('statistics.html',
                           stats=stats)


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
