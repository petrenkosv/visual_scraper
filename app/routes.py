from flask import render_template, flash, redirect, url_for, request
from flask import send_from_directory
from app import app, db
from app.forms import LoginForm, ScraperForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Test
from werkzeug.urls import url_parse
from datetime import datetime
import os

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html',  title = 'Scraping Page')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember = form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title = 'Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)



#@app.route('/<path:path>')
#@login_required
#def send_file(path):
#    return send_from_directory(url_for('static'), path)

@app.route('/scraper/', methods=['GET', 'POST'])
@login_required
def scraper():
    curr_doc = Test.query.filter_by(scraped=False).first()
    form = ScraperForm()
    if form.validate_on_submit():
        curr_doc.test_date = form.test_date.data
        curr_doc.initial_pressure = form.initial_pressure.data
        curr_doc.final_pressure = form.final_pressure.data
        curr_doc.buildup_pressure = form.buildup_pressure.data
        curr_doc.water_flow = form.water_flow.data
        curr_doc.oil_flow = form.oil_flow.data
        curr_doc.scraped = True
        curr_doc.scraper_name = current_user.username
        curr_doc.comment = form.comment.data
        curr_doc.date_scraped = datetime.utcnow()
        db.session.commit()
        flash('Data Successfully Submitted!')
        return redirect(url_for('scraper'))

    return render_template('scraper.html', title='Scraper', curr_doc=curr_doc,
                          form = form)



