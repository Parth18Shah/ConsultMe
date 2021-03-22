from flask import Flask  
from flask import render_template,url_for,flash,redirect,request
from flask_login import login_user,current_user,logout_user,login_required,LoginManager
# from db_op import insert_records, fetch_details
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from consultme_app.models import Users
from consultme_app.forms import PatientRegistrationForm, DoctorRegistrationForm, LoginForm
from consultme_app import app ,db ,bcrypt

@app.route("/")
@app.route("/home")
@login_required
def home():
    return render_template('home.html') 
    #in this we have passed variable named as posts in retuen statement i.e posts* =posts
    #therefore we can have access to this variablein home.html

@app.route("/register_choice", methods=['GET','POST'])
def register_choice():
    if request.method == "POST":
        choice = request.form["options"]
        print(choice)
        if(choice == 'doctor'):
            form = DoctorRegistrationForm()
        else:
            form = PatientRegistrationForm()
        return render_template('register.html',  form = form, choice = choice)
    return render_template('register_choice.html')  

@app.route('/register/<choice>',methods=['GET','POST'])
def register(choice):
    if current_user.is_authenticated:
        redirect(url_for('home'))
    print(choice)
    if(choice == 'doctor'):
        form = DoctorRegistrationForm()
        if form.validate_on_submit():
            hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = Users(username=form.username.data,
            u_name=form.name.data,
            gender=form.gender.data,
            specialist=form.specialist.data,
            reg_no=form.reg_no.data,
            year_reg=form.year_reg.data,
            email=form.email.data,
            phone=form.phone.data,
            pswd=hashed_pass,
            ispatient=0)
            print(request.form)
            db.session.add(user)
            db.session.commit()
            flash(f'Account created successfully for  { form.username.data }' ,'success')
            return redirect(url_for('login'))
    else:
        form = PatientRegistrationForm()
        print("hey")
        if form.validate_on_submit():
            print("hey3", form.validate_on_submit())
            hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = Users(username=form.username.data,
            u_name=form.name.data,
            gender=form.gender.data,
            email=form.email.data,
            phone=form.phone.data,
            birthdate=form.birthdate.data,
            age=form.age.data,
            med_history=form.med_history.data,
            pswd=hashed_pass,
            ispatient=1)
            print(request.form)
            db.session.add(user)
            db.session.commit()
            flash(f'Account created successfully for  { form.username.data }' ,'success')
            return redirect(url_for('login'))
    return render_template('register_choice.html',form=form)

    # if request.method == "POST":
    #     form_data = request.form
    #     print("form:",form_data)
    #     form_values = []
    #     for i in form_data:
    #         print(i)
    #         if(i == 'password1'):
    #             continue
    #         form_values.append(form_data[i])        
    #     if choice == "doctor":
    #         form_values.append(0)
    #     else:
    #         form_values.append(1)
    #     print(form_values)
    #     result = insert_records(choice,form_values)
    #     print(result)
    #     flash('Your account has been created! You are able to register','success')
    #     return redirect(url_for('login'))
    # return render_template('register_choice.html')

    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    # form=RegistrationForm()
    # if form.validate_on_submit():
    #     hashed_psw=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    #     user=User(username=form.username.data ,email=form.email.data,password=hashed_psw)
    #     db.session.add(user)
    #     db.session.commit()
    #     flash('Your account has been created! You are able to login','success')
    #     return redirect(url_for('login'))


@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        redirect(url_for('home'))
    
    form=LoginForm()
    # print("hey1",form.validate())
    if form.validate_on_submit():
        print("hey2")
        user = Users.query.filter_by(email=form.email.data).first()
        print(user)
        if user and bcrypt.check_password_hash(user.pswd,form.password.data):
            login_user(user,remember=False)
            flash('You are successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Check your email and password!')
    return render_template('login.html',form=form)
    # if request.method == "POST":
    #     username = request.form['username']
    #     email = request.form['email']
    #     pswd = request.form['password']
    #     print(username,email,pswd)
    #     records = fetch_details(username)
    #     print(records)
    #     if email == records[1] and pswd == records[2]:
    #         return redirect('/')
    #     else:
    #         flash('Login Unsuccessfull .please check email and password','danger')
    # return render_template('login.html')

    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    # form=LoginForm()
    # if form.validate_on_submit():
    #     user=User.query.filter_by(email=form.email.data).first()
    #     if user and bcrypt.check_password_hash(user.password,form.password.data):
    #         login_user(user,remember=form.remember.data)
    #         next_page=request.args.get('next')
    #         return redirect(next_page) if next_page else redirect(url_for('home'))
    #     else:
    #         flash('Login Unsuccessfull .please check email and password','danger')
    # return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html',title='account')

if __name__=='__main__':
    app.secret_key = 'the random string'
    app.run(debug=True)
