from flask import Flask, redirect, render_template, request, url_for

# Creating the Flask class object: An object of the Flask class is considered as the WSGI application.
# We need to pass the name of the current module, i.e. __name__ as the argument into the Flask constructor.
app = Flask(__name__)


# The route(rule, options) function of the Flask class defines the URL mapping of the associated function.
# rule: It represents the URL binding with the function.
# options: It represents the list of parameters to be associated with the rule object
@app.route('/')
def home():
    return "hello, this is our first flask website"


# ---------------------------------------------------------------------------------------------------------------------
def about():
    return "This is about page"


# ---------------------------------------------------------------------------------------------------------------------
@app.route('/admin')
def admin():
    return 'admin'


@app.route('/librarion')
def librarion():
    return 'librarion'


@app.route('/student')
def student():
    return 'student'


@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    if name == 'librarion':
        return redirect(url_for('librarion'))
    if name == 'student':
        return redirect(url_for('student'))


# ---------------------------------------------------------------------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['uname']
        password = request.form['pass']
        if uname == "Rohit" and password == "google":
            return "Welcome %s" % uname

    if request.method == 'GET':
        # In the GET request we can check the URL which also contains the data sent with the request to the server.
        # This is an important difference between the GET requests and the POST requests as the data sent to the server
        # is not shown in the URL on the browser in the POST requests.
        uname = request.args.get('uname')
        password = request.args.get('pass')
        if uname == "Rohit" and password == "google":
            return "Welcome %s" % uname


# ---------------------------------------------------------------------------------------------------------------------
# @motor_insurance.route('/')
# def message():
#     return render_template('message.html')
@app.route('/user/<uname>')
def message(uname):
    return render_template('message.html', name=uname)


# ---------------------------------------------------------------------------------------------------------------------
@app.route('/table/<int:num>')
def table(num):
    return render_template('print-table.html', n=num)


if __name__ == '__main__':
    """
    The "run" method of the Flask class is used to run the flask application on the local development server.
    motor_insurance.run(host, port, debug, options)  
    1. host: The default hostname is 127.0.0.1, i.e. localhost.
    2. port: The port number to which the server is listening to. The default port number is 5000.
    3. debug: The default is false. It provides debug information if it is set to true.
    4. options: It contains the information to be forwarded to the server.
    """
    app.run(debug=True)

    # add_url_rule(<url rule>, <endpoint>, <view function>):   This function is mainly used in the case if the view
    # function is not given and we need to connect a view function to an endpoint externally by using this function.
    app.add_url_rule("/about", "about", about)
