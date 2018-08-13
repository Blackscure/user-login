from flask import Flask,render_template,redirect, url_for,request
from db import users
from user import User

app =Flask(__name__)

@app.route('/')
def home():
    return render_template ('home.html')

@app.route('/register')
def register():
    return render_template ('register.html')

@app.route('/login')
def login():
    return render_template ('login.html')

@app.route('/auth/register',methods=['POST'])
def register_template():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        id = len(users) + 1
        for user in users:
            current_person = users[user]
            if name == current_person.name:
                print("name takken!!")

    

        new_user = User(name,password,id)
        
        return redirect(url_for('login'))
        

        users[id] = new_user
        print(users[id])

        return render_template ('register.html')

@app.route('/auth/login', methods=['POST'])
def login_template():
    if request.method == 'Post':
        name = request.form['name']
        password = request.form['password']


        for user in users:
            current_person = users[user]
            if name == current_person.name and password ==  current_person.password:
                return redirect(url_for('profile'))
                 
                 

if __name__ == '__main__':
    app.run(debug=True)
