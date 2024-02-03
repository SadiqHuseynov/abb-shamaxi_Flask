from extensions import *
from app import admin
from flask_admin.contrib.sqla import ModelView


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    poster = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    button_name = db.Column(db.String(50), default=False)
    button_link = db.Column(db.String(50))
    
# Zarifa
class Kreditler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sekil = db.Column(db.String(255), nullable=False)
    ad = db.Column(db.String(255), nullable=False)
    kicik_aciqlama = db.Column(db.String(255), nullable=False)
    aciqlama = db.Column(db.Text, nullable=False)
    max_mebleg = db.Column(db.String(255), nullable=False)
    muddet = db.Column(db.String(255), nullable=False)
    faiz_derecesi = db.Column(db.String(255), nullable=False)
    
class Kreditler2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sekil = db.Column(db.String(255), nullable=False)
    ad = db.Column(db.String(255), nullable=False)
    kicik_aciqlama = db.Column(db.String(255), nullable=False)
    aciqlama = db.Column(db.Text, nullable=False)
    
# Shahmar    
class DebetKartlari(db.Model):   
    id = db.Column(db.Integer, primary_key=True)
    sekil = db.Column(db.String(255), nullable=False)
    ad = db.Column(db.String(255), nullable=False)
    aciqlama = db.Column(db.Text, nullable=False)
    nece_il = db.Column(db.Integer, nullable=False)
    qiymet = db.Column(db.Integer, nullable=False)

    imkan1 = db.Column(db.String(255), nullable=False)
    imkan2 = db.Column(db.String(255), nullable=False)
    imkan3 = db.Column(db.String(255), nullable=False)
    imkan4 = db.Column(db.String(255), nullable=False)
    imkan5 = db.Column(db.String(255), nullable=False)
    imkan6 = db.Column(db.String(255), nullable=False)

class KreditKartlari(db.Model):   
    id = db.Column(db.Integer, primary_key=True)
    sekil = db.Column(db.String(255), nullable=False)
    ad = db.Column(db.String(255), nullable=False)
    aciqlama = db.Column(db.Text, nullable=False)
    nece_il = db.Column(db.Integer, nullable=False)
    qiymet = db.Column(db.Integer, nullable=False)    
    
    imkan1 = db.Column(db.String(255), nullable=False)
    imkan2 = db.Column(db.String(255), nullable=False)
    imkan3 = db.Column(db.String(255), nullable=False)
    imkan4 = db.Column(db.String(255), nullable=False)
    imkan5 = db.Column(db.String(255), nullable=False)
    imkan6 = db.Column(db.String(255), nullable=False)
    
    
#ModelView    
admin.add_view(ModelView(Company, db.session))
admin.add_view(ModelView(Kreditler, db.session))         
admin.add_view(ModelView(Kreditler2, db.session))         
admin.add_view(ModelView(DebetKartlari, db.session))
admin.add_view(ModelView(KreditKartlari, db.session))
