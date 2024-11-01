from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from db import init_app, db
from models import User, Data, Metric, Fault

# 初始化 Flask 应用
app = init_app()


@app.route('/')
def index():
    if 'user_id' in session:
        return render_template('dashboard.html', username=session['username'], isAdmin=session['is_admin'])
    return redirect(url_for('login'))


#
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.userid
            session['username'] = user.username
            session['is_admin'] = user.role == 'admin'
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')


# @app.route('/login')
# def login():
#     return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('is_admin'):
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        email = request.form['email']
        user = User(username=username, password=generate_password_hash(password, method='pbkdf2'), role=role, email=email)
        db.session.add(user)
        db.session.commit()
        flash('User added successfully.')
    users = User.query.all()
    return render_template('admin.html', users=users, username=session['username'], isAdmin=session['is_admin'])


@app.route('/faults')
def faults():
    fault_list = Fault.query.all()
    return render_template('faults.html', faults=fault_list, username=session['username'], isAdmin=session['is_admin'])


@app.route('/toggle_fault/<int:fault_id>')
def toggle_fault(fault_id):
    fault = Fault.query.get_or_404(fault_id)
    fault.solve = 1 if fault.solve == 0 else 0
    db.session.commit()
    return redirect(url_for('faults'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
