from flask import Flask, render_template, request, redirect
app = Flask(__name__)

list = []

@app.route('/')
def hello_world():
    global list
    name = "Batsheva"
    day = "Monday"

    return render_template('list.html', name=name, day=day, list=list)

@app.route('/submit', methods = ['POST'])
def submit():
    global list
    email = request.form['email']

    task = request.form['task']
    priority = request.form["Priority"]
    to_do_item = {"email": email, "task": task, "level": priority}

    if "@" not in email:
        print("email is invalid")
        return redirect('/')

    if priority != "High" and priority != "Medium" and priority != "Low":
        print("priority is invalid")
        return redirect('/')

    list.append(to_do_item)


    return redirect('/')

@app.route('/clear', methods = ['POST'])
def clear():
    global list
    list = []

    return redirect('/')


if __name__ == "__main__":
    app.run()


