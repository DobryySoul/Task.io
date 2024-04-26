from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main_page():

    name = request.args.get('name')
    message = request.args.get('message')
    if name and message:
        return f"Hello {name}! {message}!"
    else:
        return ''

if __name__ == "__main__":
    app.run(debug=True)