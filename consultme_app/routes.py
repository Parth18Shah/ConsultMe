from flask import Flask  
from flask import render_template,url_for,flash,redirect,request,session
from flask_login import login_user,current_user,logout_user,login_required,LoginManager
# from db_op import insert_records, fetch_details
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
<<<<<<< HEAD
from consultme_app.models import Users
from consultme_app.forms import PatientRegistrationForm, DoctorRegistrationForm, LoginForm ,ChatForm
=======
from consultme_app.models import Users, Chat
from consultme_app.forms import PatientRegistrationForm, DoctorRegistrationForm, LoginForm, ChatForm
>>>>>>> 81c7d278cb67a12bc093632e5e71429c9ba8d3be
from consultme_app import app ,db ,bcrypt
from consultme_app.disease import get_diseaselist, get_symptomslist, get_specialization, predict_disease, get_description, get_cure

@app.errorhandler(404)
def not_found(e):
    return(render_template("error.html"))

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
    flash('Please select one options to proceed','warning')
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
            ispatient=0,
            experience=form.experience.data)
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
    flash('Please give the details in correct format','warning')
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
        if user and user.username == form.username.data and bcrypt.check_password_hash(user.pswd,form.password.data):
            login_user(user,remember=False)
            session['logged_in'] = True
            session['uid'] = user.id
            session['s_name'] = user.email
            session['ispatient'] = user.ispatient
            session['chatstatus'] = False
            session['rid'] = 0
            print(session)
            flash('You are successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            if not user:
                flash('Please enter the correct email', 'danger')
            elif user.username != form.username.data:
                flash('Please enter the correct username', 'danger')
            else:
                flash('Please enter the correct password', 'danger')
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

# @app.route('/account')
# @login_required
# def account():
#     return render_template('account.html',title='account')


@app.route('/predict', methods=['GET','POST'])
@login_required
def predict():
    symptomslist = get_symptomslist()
    if request.method == "POST":
        print(request.form)
        form_data = request.form
        form_values = []
        for i in form_data:
            form_values.append(form_data[i])
        print(form_values, len(symptomslist))
        if (form_values.count('0')== 5):
            flash(u"Please select few symptoms before clicking on the submit button",'warning')
            return render_template('predict.html', symptomslist = symptomslist)
        diseasename = predict_disease(form_values)
        diseasedesc = []
        diseasedesc = get_description(diseasename)
        treatment = get_cure(diseasename)
        specialization = get_specialization(diseasename)
        print("hey1234",diseasename,"\n\n",diseasedesc,"\n",treatment,specialization)
        return render_template('predict.html', symptomslist = symptomslist, diseasename = diseasename, treatment = treatment, diseasedesc = diseasedesc, specialization = specialization)
    return render_template('predict.html', symptomslist = symptomslist)


<<<<<<< HEAD
# @app.route('/consult')
# # @login_required
# def consult():
#     if current_user.is_authenticated:
#         redirect(url_for('home'))
#     return render_template('consult.html')

@app.route("/consult", methods=['GET', 'POST'])
# @login_required
def chat():
    if not current_user.is_authenticated:
        flash('Please login', 'danger')
        return redirect(url_for('login'))
    form=PatientRegistrationForm()
    user1 = Users.query.all()
    target_patient = form.ispatient.data['target'].ispatient
    print(target_patient)
    # print(user1[0])
    form=ChatForm()
    for i in user1:
        print(i['username'])
        for j in i:
            print(j)
            if(j=="False"):
                user = Users(request.form['username'], request.form['specialist'], request.form['experience'])
    return render_template("consult.html", username=current_user.username,form=form)
=======
@app.route('/consult', methods=['GET','POST'])
@login_required
def consult():
    form = ChatForm()
    uid = session['uid']
    if session['ispatient'] == True:
        doctors_list = Users.query.filter_by(ispatient=0).all()
        # print(doctors_list)
        if request.method == "POST":
            receiver_id = request.form['chat-btn']
            selected_user = Users.query.filter_by(id=receiver_id).first()
            session['rid'] = receiver_id
            session['chatstatus'] = True
            # session['details'] = selected_user
            print(selected_user)
            chats = Chat.query.filter((Chat.senderid==uid) | (Chat.receiverid==uid)).filter((Chat.senderid==receiver_id) | (Chat.receiverid==receiver_id)).all()
            [print(i.message) for i in chats]

            # [print(i.message) for i in user_chats]
        
            return render_template('consult.html', doctors_list = doctors_list, chats = chats, selected_user = selected_user, uid = uid, form = form )
        return render_template('consult.html', doctors_list = doctors_list)
    else:
        chat_list =  Chat.query.filter((Chat.senderid==uid) | (Chat.receiverid==uid)).all()
        users_list = []
        user_id = []
        for i in chat_list:
            if(i.senderid==uid):
                user = Users.query.filter_by(id=i.receiverid).first()
                if(user.id not in user_id):
                    users_list.append(user)
                    user_id.append(user.id)
            else:
                user = Users.query.filter_by(id=i.senderid).first()
                if(user.id not in user_id):
                    users_list.append(user)
                    user_id.append(user.id)
        # print(users_list)
        if request.method == "POST":
            receiver_id = request.form['chat-btn']
            selected_user = Users.query.filter_by(id=receiver_id).first()
            session['rid'] = receiver_id
            session['chatstatus'] = True
            # session['details'] = selected_user
            print(selected_user)
            chats = Chat.query.filter((Chat.senderid==uid) | (Chat.receiverid==uid)).filter((Chat.senderid==receiver_id) | (Chat.receiverid==receiver_id)).all()
            [print(i.message) for i in chats]

            # [print(i.message) for i in user_chats]
        
            return render_template('consult.html', users_list = users_list, chats = chats, selected_user = selected_user, uid = uid, form = form )
        return render_template('consult.html', users_list = users_list)
    

@app.route('/chat', methods=['POST'])
@login_required
def storechat():
    form = ChatForm()
    if request.method == 'POST':
        print(form.message.data)
        chat = Chat(
            senderid = session['uid'],
            receiverid = session['rid'],
            message = form.message.data
        )
        db.session.add(chat)
        db.session.commit()
        print("hyyy")
        return redirect(url_for('consult'))
    return redirect(url_for('home'))
>>>>>>> 81c7d278cb67a12bc093632e5e71429c9ba8d3be

if __name__=='__main__':
    app.secret_key = 'the random string'
    app.run(debug=True)
