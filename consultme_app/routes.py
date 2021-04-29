from flask import Flask
from flask import render_template, url_for, flash, redirect, request, session
from flask_login import login_user, current_user, logout_user, login_required, LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy import desc
import itertools
from datetime import datetime
from consultme_app.models import Users, Chat, PredictDisease, ConsultRate, ConsultLog
from consultme_app.forms import PatientRegistrationForm, DoctorRegistrationForm, LoginForm, ChatForm, PredictForm, RateForm, LogForm
from consultme_app import app, db, bcrypt
from consultme_app.disease import get_diseaselist, get_symptomslist, get_specialization, predict_disease, get_description, get_cure
from consultme_app.verify import verify_doctor


@app.errorhandler(404)
def not_found(e):
    return(render_template("error.html"))


@app.route("/")
@app.route("/home")
def home():
    pred = PredictDisease.query.filter_by(feedback=True).all()
    p = len(pred)
    consult1 = ConsultRate.query.all()
    c = 0
    for i in consult1:
        if(i.rate > 50):
            c += 1
    return render_template('home.html', num=p, num1=c)


@app.route("/abc")
def abc():
    return render_template('chat.html')


@app.route("/register_choice", methods=['GET', 'POST'])
def register_choice():
    if request.method == "POST":
        choice = request.form["options"]

        if(choice == 'doctor'):
            form = DoctorRegistrationForm()
        else:
            form = PatientRegistrationForm()
        return render_template('register.html',  form=form, choice=choice)
    flash('Please select one options to proceed', 'warning')
    return render_template('register_choice.html')

# def save_picture(form_picture,id):
#     random_hex = secrets.token_hex(8)
#     _ ,f_ext = os.path.splitext(form_picture.filename)
#     picture_fn = random_hex + f_ext
#     picture_path = os.path.join(app.root_path,'static/profile_pics',picture_fn,id)
#     form_picture.save(picture_path)

#     return picture_fn


@app.route('/register/<choice>', methods=['GET', 'POST'])
def register(choice):
    if current_user.is_authenticated:
        redirect(url_for('home'))

    if(choice == 'doctor'):
        form = DoctorRegistrationForm()
        if form.validate_on_submit():
            hashed_pass = bcrypt.generate_password_hash(
                form.password.data).decode('utf-8')

            user = Users(username=form.username.data,
                         u_name=form.name.data,
                         gender=form.gender.data,
                         specialist=form.specialist.data,
                         reg_no=form.reg_no.data,
                         year_reg=form.year_reg.data,
                         email=form.email.data,
                         phone=form.phone.data,
                         pswd=hashed_pass,
                         ispatient=False,
                         # ispatient=0,
                         experience=form.experience.data
                         )
            result = verify_doctor(form.reg_no.data, form.name.data)
            print(result)
            if(result == 1):
                db.session.add(user)
                db.session.commit()
                flash(
                    f'Account created successfully for  { form.username.data }', 'success')
                return redirect(url_for('login'))
    else:
        form = PatientRegistrationForm()

        if form.validate_on_submit():
            hashed_pass = bcrypt.generate_password_hash(
                form.password.data).decode('utf-8')
            user = Users(username=form.username.data,
                         u_name=form.name.data,
                         gender=form.gender.data,
                         email=form.email.data,
                         phone=form.phone.data,
                         birthdate=form.birthdate.data,
                         age=form.age.data,
                         med_history=form.med_history.data,
                         pswd=hashed_pass,
                         ispatient=True,
                         # ispatient=1,
                         )
            db.session.add(user)
            db.session.commit()
            flash(
                f'Account created successfully for  { form.username.data }', 'success')
            return redirect(url_for('login'))

    flash('Please give the details in correct format', 'warning')
    return render_template('register.html',  form=form, choice=choice)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()

        if user and user.username == form.username.data and bcrypt.check_password_hash(user.pswd, form.password.data):
            login_user(user, remember=False)
            session['logged_in'] = True
            session['uid'] = user.id
            session['s_name'] = user.email
            session['ispatient'] = user.ispatient
            session['chatstatus'] = False
            session['rid'] = 0

            flash('You are successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            if not user:
                flash('Please enter the correct email', 'danger')
            elif user.username != form.username.data:
                flash('Please enter the correct username', 'danger')
            else:
                flash('Please enter the correct password', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    session['chatstatus'] = False
    session['rid'] = 0
    return redirect(url_for('home'))


@app.route('/predict', methods=['GET', 'POST'])
@login_required
def predict():
    form = PredictForm()
    symptomslist = get_symptomslist()
    form_data = request.form

    if request.method == "POST":
        if form.feedback.data == False:
            form_data = request.form
            form_values = []
            for i in form_data:
                form_values.append(form_data[i])
            if (form_values.count('0') == 5):
                flash(
                    u"Please select few symptoms before clicking on the submit button", 'warning')
                return render_template('predict.html', symptomslist=symptomslist)
            diseasename = predict_disease(form_values)

            diseasedesc = []
            # diseasedesc = get_description(diseasename)
            # treatment = get_cure(diseasename)
            # specialization = get_specialization(diseasename)
            # print(diseasedesc, "\n", treatment, "\n", specialization)

            for i in range(len(form_values)):
                new_value = form_values[i].replace("0", "")
                form_values[i] = new_value

            pred = PredictDisease(
                userid=current_user.id,
                disease_name=diseasename[0],
                symptom1=form_values[0],
                symptom2=form_values[1],
                symptom3=form_values[2],
                symptom4=form_values[3],
                symptom5=form_values[4]
            )
            print(pred)
            db.session.add(pred)
            db.session.commit()
            return render_template('predict.html', symptomslist=symptomslist, diseasename=diseasename, form=form)
            # ,treatment=treatment, diseasedesc=diseasedesc, specialization=specialization
        else:
            pred1 = db.session.query(PredictDisease).filter_by(
                userid=current_user.id).order_by(PredictDisease.id.desc()).first()
            if (form.feedback_input.data == "True"):
                pred1.feedback = True
            else:
                pred1.feedback = False
            db.session.flush()
            db.session.commit()

    return render_template('predict.html', symptomslist=symptomslist)


@app.route('/consult', methods=['GET', 'POST'])
@login_required
def consult():
    form = ChatForm()
    uid = session['uid']
    isenabled = False
    if session['ispatient'] == True:
        doctors_list = Users.query.filter_by(ispatient=False).all()
        # doctors_list = Users.query.filter_by(ispatient=0).all()

        if request.method == "POST":
            receiver_id = request.form['chat-btn']
            session['rid'] = receiver_id
            session['chatstatus'] = True

        if session['chatstatus'] == True:
            selected_user = Users.query.filter_by(id=session['rid']).first()
            chats = Chat.query.filter((Chat.senderid == uid) | (Chat.receiverid == uid)).filter(
                (Chat.senderid == session['rid']) | (Chat.receiverid == session['rid'])).all()
            consult_status = ConsultLog.query.filter(
                ConsultLog.doctorid == session['rid'], ConsultLog.patientid == uid).all()
            for i in range(len(consult_status)):
                if(consult_status[i].isenabled):
                    isenabled = True
                # print(val)
            return render_template('consult.html', doctors_list=doctors_list, chats=chats, selected_user=selected_user, uid=uid, form=form, isenabled=isenabled)
        return render_template('consult.html', doctors_list=doctors_list, form=form)
    else:
        chat_list = Chat.query.filter(
            (Chat.senderid == uid) | (Chat.receiverid == uid)).all()
        users_list = []
        user_id = []
        for i in chat_list:
            if(i.senderid == uid):
                user = Users.query.filter_by(id=i.receiverid).first()
                if(user.id not in user_id):
                    users_list.append(user)
                    user_id.append(user.id)
            else:
                user = Users.query.filter_by(id=i.senderid).first()
                if(user.id not in user_id):
                    users_list.append(user)
                    user_id.append(user.id)

        if request.method == "POST":
            receiver_id = request.form['chat-btn']
            session['rid'] = receiver_id
            session['chatstatus'] = True

        if session['chatstatus'] == True:
            selected_user = Users.query.filter_by(id=session['rid']).first()
            chats = Chat.query.filter((Chat.senderid == uid) | (Chat.receiverid == uid)).filter(
                (Chat.senderid == session['rid']) | (Chat.receiverid == session['rid'])).all()
            consult_status = ConsultLog.query.filter(
                ConsultLog.doctorid == uid, ConsultLog.patientid == session['rid']).all()
            for i in range(len(consult_status)):
                if(consult_status[i].isenabled):
                    isenabled = True
            return render_template('consult.html', users_list=users_list, chats=chats, selected_user=selected_user, uid=uid, form=form, isenabled=isenabled)
        return render_template('consult.html', users_list=users_list, form=form)


@app.route('/chat', methods=['POST'])
@login_required
def storechat():
    form = ChatForm()
    if request.method == 'POST':
        chat = Chat(
            senderid=session['uid'],
            receiverid=session['rid'],
            message=request.form['message']
        )
        db.session.add(chat)
        db.session.commit()
        return redirect(url_for('consult'))
    return redirect(url_for('home'))


@app.route('/getchats', methods=['GET', 'POST'])
@login_required
def getchats():
    rid = session['rid']
    uid = session['uid']
    selected_user = Users.query.filter_by(id=session['rid']).first()
    # print("rid",rid,uid)
    chats = Chat.query.filter((Chat.senderid == uid) | (Chat.receiverid == uid)).filter(
        (Chat.senderid == session['rid']) | (Chat.receiverid == session['rid'])).all()
    # print(chats)
    return render_template('chats.html', chats=chats, selected_user=selected_user, uid=uid)
    # return redirect(url_for('home'))


@app.route('/startchat', methods=['POST'])
@login_required
def startchat():
    form = LogForm()
    if request.method == 'POST':
        print(request.form)
        consult_details = ConsultLog(
            patientid=session['uid'],
            doctorid=session['rid'],
            isenabled=True,
            disease_name=request.form['disease_name'],
        )
        db.session.add(consult_details)
        db.session.commit()
        return redirect(url_for('consult'))
    return redirect(url_for('home'))


@app.route('/endchat', methods=['POST'])
@login_required
def endchat():
    consult_log = ConsultLog.query.filter(
        ConsultLog.doctorid == session['uid'], ConsultLog.patientid == session['rid'], ConsultLog.isenabled == True).first()
    # consult_log.end
    print(consult_log)
    if request.method == 'POST':
        consult_log.isenabled = False
        consult_log.ended_on = datetime.now()
        db.session.flush()
        db.session.commit()
        flash(f'Log Updated successfully', 'success')
        return redirect(url_for('consult'))
    return redirect(url_for('home'))


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    uid = session['uid']
    rid = session['rid']
    chat_list = Chat.query.filter(
        (Chat.senderid == uid) | (Chat.receiverid == uid)).all()
    users_list = []
    user_id = []
    for i in chat_list:
        if(i.senderid == uid):
            user = Users.query.filter_by(id=i.receiverid).first()
            if(user.id not in user_id):
                users_list.append(user)
                user_id.append(user.id)
        else:
            user = Users.query.filter_by(id=i.senderid).first()
            if(user.id not in user_id):
                users_list.append(user)
                user_id.append(user.id)
    if(current_user.ispatient == False):
        form = DoctorRegistrationForm()
        form1 = RateForm()
        userone = Users.query.filter_by(id=current_user.id).first_or_404()
        fn = "default.jpg"
        if request.method == "POST":
            if request.form['save-btn'] == 'save':
                userone.username = form.username.data
                userone.u_name = form.name.data
                userone.image_file = fn
                db.session.flush()
                db.session.commit()
                flash(f'Profile Updated successfully', 'success')
        ratelist = []
        loglist = []
        log = ConsultLog.query.filter_by(doctorid=current_user.id).all()
        for y in users_list:
            for z in log:
                if(z.patientid == y.id):
                    loglist.append(
                        [y.id, y.username, z.disease_name, z.initiated_on, z.ended_on])
        loglist = list(num for num, _ in itertools.groupby(loglist))
        rate2 = ConsultRate.query.filter_by(doctorid=current_user.id).all()
        for y in users_list:
            for z in rate2:
                if(z.patientid == y.id):
                    ratelist.append([y.id, y.username, z.disease_name, z.rate])
        ratelist = list(num for num, _ in itertools.groupby(ratelist))
        for i in ratelist:
            if len(i) == 4:
                if(i[3] > 50):
                    i.append(True)
                else:
                    i.append(False)
        pred = PredictDisease.query.all()
        labels = []
        values = []
        l1 = []
        for i in pred:
            l1.append(i.disease_name)
        freq = {}
        for item in l1:
            if (item in freq):
                freq[item] += 1
            else:
                freq[item] = 1
        for i, j in freq.items():
            labels.append(i)
            values.append(j)
        return render_template('account.html', users_list=users_list, form=form, userone=userone, image_file=fn, form1=form1, ratelist=ratelist, labels=labels, values=values, loglist=loglist)
    else:
        form = PatientRegistrationForm()
        userone = Users.query.filter_by(id=current_user.id).first_or_404()
        fn = "default.jpg"
        pred_list = PredictDisease.query.filter_by(
            userid=current_user.id).all()
        print(pred_list)
        if request.method == "POST":
            if request.form['save-btn'] == 'save':
                userone.username = form.username.data
                userone.u_name = form.name.data
                userone.image_file = fn
                userone.med_history = form.med_history.data
                db.session.flush()
                db.session.commit()
                flash(f'Profile Updated successfully', 'success')
        return render_template('account.html', users_list=users_list, form=form, userone=userone, image_file=fn, pred_list=pred_list)


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    uid = session['rid']
    form1 = RateForm()
    chat_list = Chat.query.filter(
        (Chat.senderid == uid) | (Chat.receiverid == uid)).all()
    users_list = []
    user_id = []
    for i in chat_list:
        if(i.senderid == uid):
            user = Users.query.filter_by(id=i.receiverid).first()
            if(user.id not in user_id):
                users_list.append(user)
                user_id.append(user.id)
        else:
            user = Users.query.filter_by(id=i.senderid).first()
            if(user.id not in user_id):
                users_list.append(user)
                user_id.append(user.id)
    pred_list = ConsultLog.query.filter_by(patientid=current_user.id).all()
    diseaselist = []
    for i in pred_list:
        diseaselist.append(i.disease_name)
    if(current_user.ispatient == False):
        form = PatientRegistrationForm()
        userone = Users.query.filter_by(id=uid).first_or_404()
        fn = "default.jpg"
        return render_template('profile.html', users_list=users_list, form=form, userone=userone, image_file=fn, pred_list=pred_list)
    else:
        form = DoctorRegistrationForm()
        fn = "default.jpg"
        userone = Users.query.filter_by(id=uid).first_or_404()
        if request.method == "POST":
            form_data = request.form
            form_values = []
            for i in form_data:
                form_values.append(form_data[i])
            if(form_values.count('0') > 0):
                flash(
                    u"Please select a disease before clicking on the submit button", 'warning')
                return render_template('profile.html', users_list=users_list, form=form, userone=userone, image_file=fn, form1=form1, diseaselist=diseaselist)
            rate1 = ConsultRate(
                patientid=current_user.id,
                doctorid=uid,
                disease_name=form_values[1],
                rate=form_values[2]
            )
            db.session.add(rate1)
            db.session.commit()
        ratelist = []
        for x in diseaselist:
            rate2 = ConsultRate.query.filter_by(
                patientid=current_user.id, disease_name=x).all()
            if len(rate2) > 0:
                sum1 = 0
                for i in range(len(rate2)):
                    sum1 = sum1 + rate2[i].rate
                avg = sum1//len(rate2)
                for i in users_list:
                    if i.id == current_user.id:
                        i.feedback = avg
                patient = Users.query.filter_by(
                    id=current_user.id).first_or_404()
                patient.feedback = avg
                db.session.flush()
                db.session.commit()
                for y in users_list:
                    for z in rate2:
                        if(z.patientid == y.id):
                            ratelist.append([y.id, y.username, x, avg])

                ratelist = list(num for num, _ in itertools.groupby(ratelist))
                for i in ratelist:
                    if len(i) == 4:
                        if(i[3] > 50):
                            i.append(True)
                        else:
                            i.append(False)
        rate3 = ConsultRate.query.all()
        l = []
        values = []
        for i in rate3:
            l.append([i.patientid, i.disease_name, i.rate])
        p = 0
        n = 0
        for i in l:
            if len(i) == 3:
                if(i[2] > 50):
                    i.append(True)
                    p += 1
                else:
                    i.append(False)
                    n += 1
        values.append(p)
        values.append(n)
        return render_template('profile.html', users_list=users_list, form=form, userone=userone, image_file=fn, form1=form1, diseaselist=diseaselist, ratelist=ratelist, values=values)


if __name__ == '__main__':
    app.secret_key = 'the random string'
    app.run(debug=True)


# last seen ka hai isme :-
#  https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vi-profile-page-and-avatars
