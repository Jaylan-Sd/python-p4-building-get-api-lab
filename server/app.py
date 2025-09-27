#!/usr/bin/env python3

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

# Import models
from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)


# ROUTES
@app.route('/')
def index():
    return '<h1>Bakery API</h1>'

# GET /bakeries
@app.route('/bakeries')
def bakeries():
    bakeries = Bakery.query.all()
    return make_response([b.to_dict() for b in bakeries], 200)

# GET /bakeries/<id>
@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.get_or_404(id)
    return make_response(bakery.to_dict(), 200)

# GET /baked_goods/by_price
@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    goods = BakedGood.query.order_by(desc(BakedGood.price)).all()
    return make_response([g.to_dict() for g in goods], 200)

# GET /baked_goods/most_expensive
@app.route('/baked_goods/most_expensive')
def most_expensive():
    good = BakedGood.query.order_by(desc(BakedGood.price)).first()
    return make_response(good.to_dict(), 200)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
