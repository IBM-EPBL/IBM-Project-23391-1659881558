from flask import Flask,render_template
app=Flask(_name_)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if _name=='main_':
    app.run(host='0.0.0.0', port=8081, debug=True)
