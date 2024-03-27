from flask import Flask ,request ,jsonify ,send_from_directory
import json
import os

app = Flask(__name__)

@app.route('/api/v1/employees', methods=['GET'])
@app.route('/prodcuts/<int:product_id>', methods=['GET'])
def get_products(product_id=None):
    if product_id:
        with open('products.json') as f:
            data = json.load(f)
            for product in data:
                if product['id'] == product_id:
                    return jsonify(product)
            return jsonify({'message': 'product not found'}), 404
    else:
        with open('products.json') as f:
            data = json.load(f)
            return jsonify(data)