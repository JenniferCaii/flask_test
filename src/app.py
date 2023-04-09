from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/duration=<duration>')
def main():
    return 

@app.route('/about/durati=<username>')
def about(username):
    username = username.upper()
    return f'this is flask turoial of {username}'

@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == 'POST':
        user = request.form["nm"]
    else:
        return render_template('login.html')

@app.route("/<usr>")
def user(usr):
    return f'{usr}'

if __name__ == '__main__':
    app.run(debug=True) 