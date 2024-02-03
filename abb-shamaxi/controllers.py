import pytz
from app import app
from extensions import db
from models import *
from flask import render_template
from datetime import datetime
from sqlalchemy import desc
from currency import usd_value,eur_value,rub_value

#Sadiq
@app.route('/')
def home():
    baku_tz = pytz.timezone('Asia/Baku')
    today = datetime.now(baku_tz)
    formatted_date = today.strftime("%d.%m.%Y")
    return render_template('main.html', formatted_date=formatted_date, usd_value = usd_value,eur_value = eur_value,rub_value = rub_value)

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/company')
def company():
    datas = Company.query.order_by(desc(Company.id)).all()
    return render_template('company.html', datas=datas)

@app.route('/company/detail/<int:id>')
def company_detail(id):
    getData = Company.query.filter_by(id=id).first()
    if getData is None:
        return render_template('404.html')
    return render_template('company-detail.html', getData=getData)

#Zarifa
@app.route('/credits')
def credits():
    getCredits = Kreditler.query.order_by(desc(Kreditler.id)).limit(2).all()
    getCredits2 = Kreditler2.query.order_by(desc(Kreditler2.id)).limit(4).all()
    return render_template('credits.html', getCredits=getCredits, getCredits2=getCredits2)

@app.route('/credits/credits_detail/<int:id>')
def credits_detail(id):
    getCreditDetail = Kreditler.query.filter_by(id=id).first()
    if getCreditDetail is None:
        return render_template('404.html')
    return render_template("credits_detail.html", getCreditDetail = getCreditDetail)
@app.route('/credits/credits_detail_2/<int:id>')
def credits_detail_2(id):
    getCreditDetail = Kreditler2.query.filter_by(id=id).first()
    if getCreditDetail is None:
        return render_template('404.html')
    return render_template("credits_detail.html", getCreditDetail = getCreditDetail)
#Shahmar
@app.route('/cards')
def cards():
    _DebetKartlariLimit = DebetKartlari.query.order_by(desc(DebetKartlari.id)).limit(3).all()
    _DebetKartlari = DebetKartlari.query.order_by(desc(DebetKartlari.id)).all()
    _KreditKartlari = KreditKartlari.query.order_by(desc(KreditKartlari.id)).all()
    return render_template('cards.html', debet_kartlari_limit = _DebetKartlariLimit, debet_kartlari = _DebetKartlari, kredit_kartlari = _KreditKartlari)

@app.route('/cards/debet_cards_details/<int:id>')
def debet_cards_details(id):
    _DebetKarti = DebetKartlari.query.filter_by(id=id).first()
    if _DebetKarti is None:
        return render_template('404.html')
    return render_template('card_details.html', kart_detali = _DebetKarti)

@app.route('/cards/credit_cards_details/<int:id>')
def credit_cards_details(id):
    _KreditKarti = KreditKartlari.query.filter_by(id=id).first()
    if _KreditKarti is None:
        return render_template('404.html')
    return render_template('card_details.html', kart_detali = _KreditKarti)