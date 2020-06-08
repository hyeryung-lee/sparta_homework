from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def write_order():
    name_receive = request.form['name_give']
    amount_receive = request.form['amount_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']
    order = {
       'name': name_receive,
       'amount': amount_receive,
       'address': address_receive,
       'phone': phone_receive
    }
    db.orders.insert_one(order)
    return jsonify({'result': 'success'})


@app.route('/order', methods=['GET'])
def list_orders():
    orders = list(db.orders.find({},{'_id': False }))
    return jsonify({'result':'success', 'msg': '주문을 받아왔습니다.', 'orders' : orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)