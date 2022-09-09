import pymysql
import sys
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, session
from functools import wraps
import smtplib
from prettytable import PrettyTable

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hjshjhdjahkjshkjdhjs'


class Database():
    def __init__(self):
        host = "localhost"
        user = "root"
        password = "mysql-root-password"
        db = "learning"
        self.con = pymysql.Connect(host=host, user=user, password=password, db=db,
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def create_user(self, username, password, emailid, emailpassword):
        self.cur.execute(f"insert into user_table (username, password, emailid, emailpassword) "
                         f"values (%s,%s,%s,%s)",
                         (username, password, emailid, emailpassword))
        self.con.commit()

    def check_user(self, username):
        self.cur.execute(f"select username,password from user_table where username ='{username}'")
        res = self.cur.fetchall()
        return res

    def user_results(self, username):
        self.cur.execute(f"select * from result_table where user_name  = '{username}' order by date_of_exam desc")
        res = self.cur.fetchall()
        return res

    def list_of_subjects(self):
        self.cur.execute("select distinct added_date,subject_name from question_table")
        res = self.cur.fetchall()
        return res

    def list_of_question(self, sub):
        self.cur.execute(f"select * from question_table where subject_name='{sub}'")
        res = self.cur.fetchall()
        return res

    def get_user_mail(self, user):
        self.cur.execute(f"select emailid,emailpassword from user_table where username='{user}'")
        res = self.cur.fetchall()
        return res

    def get_user_result_status(self, username):
        self.cur.execute(
            f"select user_name,subject_name,substring(DATE_OF_EXAM,1,10) exam_date,count(user_name) no_of_exam_completed,"
            f" count(case when score >= 8 then 'PASS' end) passed_exams, count(case when score < 8 then 'FAIL' end) failed_exams, "
            f"(count(case when score >= 8 then 'PASS' end) / count(user_name)) * 100 percentage, avg(score) avg_score "
            f"from result_table "
            f"where user_name='{username}' "
            f"group by user_name,subject_name,substring(DATE_OF_EXAM,1,10) "
            f"order by substring(DATE_OF_EXAM,1,10) desc, subject_name")
        res = self.cur.fetchall()
        return res

    def get_all_user_result_status(self):
        self.cur.execute(
            f"select user_name,subject_name,substring(DATE_OF_EXAM,1,10) exam_date,count(user_name) no_of_exam_completed,"
            f" count(case when score >= 8 then 'PASS' end) passed_exams, count(case when score < 8 then 'FAIL' end) failed_exams, "
            f"(count(case when score >= 8 then 'PASS' end) / count(user_name)) * 100 percentage, avg(score) avg_score "
            f"from result_table "
            f"group by user_name,subject_name,substring(DATE_OF_EXAM,1,10) "
            f"order by substring(DATE_OF_EXAM,1,10) desc, subject_name")
        res = self.cur.fetchall()
        return res

    def submit_responses(self, username, sub_name, res1, res2, res3, res4, res5, res6, res7, res8, res9, res10):
        responses = [res1, res2, res3, res4, res5, res6, res7, res8, res9, res10]
        self.cur.execute(
            "INSERT INTO response_table"
            "(user_name,subject_name,date_of_exam,res1,res2,res3,res4,res5,res6,res7,res8,res9,res10)"
            " VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (username, sub_name, datetime.now(), res1, res2, res3, res4, res5, res6, res7, res8, res9, res10))
        self.con.commit()

        self.cur.execute(
            f"select  ans1, ans2,ans3,ans4,ans5,ans6,ans7,ans8,ans9,ans10 from answer_table where subject_name='{sub_name}'")
        output = self.cur.fetchall()[0]
        answers = [output['ans1'], output['ans2'], output['ans3'], output['ans4'], output['ans5'], output['ans6'],
                   output['ans7'], output['ans8'], output['ans9'], output['ans10']]
        sum_of_correct_ans = 0

        for i in range(10):
            if answers[i] == responses[i]:
                sum_of_correct_ans += 1
        total_questions = 10
        percentage = (sum_of_correct_ans / total_questions) * 100
        self.cur.execute(f"insert into result_table (user_name,subject_name,date_of_exam,score,total,percentage) "
                         f"values (%s,%s,%s,%s,%s,%s)",
                         (username, sub_name, datetime.now(), sum_of_correct_ans, total_questions, percentage))
        self.con.commit()

    def submit_questions(self, sub_name, question_list):

        option_and_answer = []
        answers = []
        self.cur.execute(f"select max(substr(subject_name,length(subject_name)-1, length(subject_name))) max_num from "
                         f"question_table where subject_name like '{sub_name}%';")
        max_sub_num = self.cur.fetchall()
        if max_sub_num[0]['max_num']:
            max_num = int(max_sub_num[0]['max_num']) + 1
        else:
            max_num = 1
        sub_name = sub_name.upper() + "_" + str(max_num)
        question_query = "INSERT INTO question_table " \
                         f"(subject_name, added_date, question_number,question,option1,option2,option3,option4,answer)" \
                         " VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        answer_query = "INSERT INTO answer_table " \
                       "(subject_name, added_date, ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10)" \
                       " VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        for i in range(1, 11):
            for j in range(2, 8):
                option_and_answer.append(question_list[f"r{i}c{j}"])
                if f"r{i}c{j}" == f"r{i}c{7}":
                    answers.append(question_list[f"r{i}c{j}"])
            self.cur.execute(question_query, (sub_name, datetime.now(), i, option_and_answer[0], option_and_answer[1],
                                              option_and_answer[2], option_and_answer[3], option_and_answer[4],
                                              option_and_answer[5]))
            option_and_answer.clear()
        self.cur.execute(answer_query,
                         (sub_name, datetime.now(), answers[0], answers[1], answers[2],
                          answers[3], answers[4], answers[5], answers[6], answers[7],
                          answers[8], answers[9]))
        self.con.commit()

    def learning_subjects(self, sub_name):
        self.cur.execute(f"select question,answer from question_table where subject_name = '{sub_name}' ")
        res = self.cur.fetchall()
        return res

    def get_all_users(self):
        self.cur.execute(f"select * from user_table")
        res = self.cur.fetchall()
        return res

    def get_all_subjects(self):
        res = self.list_of_subjects()
        return res

    def get_all_questions(self):
        self.cur.execute(
            f"select subject_name, question_number, question, answer from question_table order by subject_name,question_number")
        res = self.cur.fetchall()
        return res

    def get_all_responses(self):
        self.cur.execute(f"select * from response_table")
        res = self.cur.fetchall()
        return res

    def get_all_answers(self):
        self.cur.execute(f"select * from answer_table")
        res = self.cur.fetchall()
        return res

    def get_all_results(self):
        self.cur.execute(f"select * from result_table order by date_of_exam desc, user_name")
        res = self.cur.fetchall()
        return res

    def get_content_data(self):
        self.cur.execute(f"select "
                         f"(select count(*) from user_table) as user_count,"
                         f"(select count(distinct subject_name) from question_table) as subject_count, "
                         f"(select count(*) from result_table) as total_exam_conducted, "
                         f"(select count(*) from result_table where score >= 4) as exam_passed, "
                         f"(select count(*) from result_table where score < 4) as exam_failed "
                         f"from dual ")
        res = self.cur.fetchall()
        return res


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = Database().check_user(username)
        if user:
            user = user[0]
            if user['password'] == password:
                session['logged_in'] = True
                session['username'] = username
                flash('Logged in successfully!', category='success')
                if user['username'] == 'admin':
                    return redirect("/admin")
                else:
                    return redirect("/")
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('User does not exist.', category='error')

    return render_template("login.html")


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        emailid = request.form.get('emailid')
        emailpassword = request.form.get('emailpass')

        user = Database().check_user(username)
        if user:
            flash('User already exists.', category='error')
        elif len(username) < 4:
            flash('Username must be greater than 3 characters.', category='error')
        elif len(password) < 5:
            flash('Password must be at least 5 characters.', category='error')
        else:
            Database().create_user(username, password, emailid, emailpassword)
            flash('Account created!', category='success')
            return redirect("/login")

    return render_template("sign_up.html")


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, please login', 'danger')
            return redirect('/login')

    return wrap


@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('you are now logged out ', 'success')
    return redirect('/login')


@app.route("/", methods=['GET', 'POST'])
@is_logged_in
def home():
    if request.method == 'POST':
        pass
    else:
        username = session['username']
        status = Database().get_user_result_status(username)
        return render_template("home.html", status=status)


@app.route("/subject", methods=['GET', 'POST'])
@is_logged_in
def subject():
    sub = Database().list_of_subjects()
    return render_template("subject.html", subject=sub)


@app.route("/result", methods=['GET', 'POST'])
@is_logged_in
def result():
    if request.method == 'POST':
        return redirect("/subject")
    else:
        username = session['username']
        res = Database().user_results(username)
        return render_template("result.html", result=res)


@app.route("/question/<string:sub_name>")
@is_logged_in
def question_from_subject(sub_name):
    que = Database().list_of_question(sub_name)
    return render_template("question.html", question=que)


@app.route("/question", methods=['POST'])
@is_logged_in
def question_response():
    username = session['username']
    sub_name = request.form.get('sub_name')
    res1 = request.form.get('1')
    res2 = request.form.get('2')
    res3 = request.form.get('3')
    res4 = request.form.get('4')
    res5 = request.form.get('5')
    res6 = request.form.get('6')
    res7 = request.form.get('7')
    res8 = request.form.get('8')
    res9 = request.form.get('9')
    res10 = request.form.get('10')
    Database().submit_responses(username, sub_name, res1, res2, res3, res4, res5, res6, res7, res8, res9, res10)
    return redirect("/result")


@app.route("/all_questions", methods=['GET', 'POST'])
@is_logged_in
def all_quetions():
    res = Database().get_all_questions()
    return render_template("admin.html", question=res)


@app.route("/all_results", methods=['GET', 'POST'])
@is_logged_in
def all_results():
    res = Database().get_all_results()
    return render_template("admin.html", result=res)


@app.route("/all_subjects", methods=['GET', 'POST'])
@is_logged_in
def all_subjects():
    res = Database().get_all_subjects()
    return render_template("admin.html", subject=res)


@app.route("/all_users", methods=['GET', 'POST'])
@is_logged_in
def all_users():
    res = Database().get_all_users()
    return render_template("admin.html", user=res)


@app.route("/all_responses", methods=['GET', 'POST'])
@is_logged_in
def all_responses():
    res = Database().get_all_responses()
    return render_template("admin.html", response=res)


@app.route("/all_answers", methods=['GET', 'POST'])
@is_logged_in
def all_answers():
    res = Database().get_all_answers()
    return render_template("admin.html", answer=res)


@app.route("/admin", methods=['GET', 'POST'])
@is_logged_in
def admin_page():
    if request.method == 'POST':
        res = Database().get_content_data()
        res1 = Database().get_all_user_result_status()
        return render_template("admin.html", content=res, user_status=res1)
    else:
        username = session['username']
        if username == 'admin':
            res = Database().get_content_data()
            res1 = Database().get_all_user_result_status()
            return render_template("admin.html", content=res, user_status=res1)
        return render_template("login.html")


@app.route("/add_question", methods=['GET', 'POST'])
@is_logged_in
def add_question():
    if request.method == 'POST':
        sub_name = request.form.get('sub_name')
        question_list = {}
        for i in range(1, 11):
            for j in range(2, 8):
                question_list[f"r{i}c{j}"] = request.form.get(f"r{i}c{j}")
        Database().submit_questions(sub_name, question_list)
        return render_template("admin.html")
    else:
        return render_template("add_question.html")


@app.route("/learn/<string:sub_name1>")
@is_logged_in
def learn_sub(sub_name1):
    res = Database().learning_subjects(sub_name1)
    return render_template("learn.html", words=res)


@app.route("/learn", methods=['GET', 'POST'])
@is_logged_in
def learn():
    res = Database().list_of_subjects()
    return render_template("subject.html", learn=res)


@app.route("/mail", methods=['GET', 'POST'])
@is_logged_in
def send_reports_on_mail():
    if request.method == 'POST':
        receivers_mail = ["vinodkanojiya1694@gmail.com","pmpramod1992@gmail.com","manojkanojiya2006@gmail.com"]
        username = session['username']
        user_mail = Database().get_user_mail(username)
        sender_mail = user_mail[0]['emailid']
        sender_password = user_mail[0]['emailpassword']

        for dest in receivers_mail:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            s.login(sender_mail, sender_password)
            username = session['username']
            status = Database().get_user_result_status(username)
            message = PrettyTable(["user_name", "subject_name", "exam_date", "exam_completed", "passed_exams", "failed_exams",
                             "percentage", "avg_score"])
            for stat in status:
                message.add_row([stat["user_name"], stat["subject_name"],
                            stat["exam_date"], stat["no_of_exam_completed"],
                            stat["passed_exams"], stat["failed_exams"],
                            stat["percentage"], stat["avg_score"]])

            s.sendmail(sender_mail, dest, message.get_string())
            s.quit()
    status = Database().get_user_result_status(username)
    return render_template("home.html", status=status)


if __name__ == "__main__":
    app.run(port=5006, debug=True)

