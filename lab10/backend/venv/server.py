from flask import Flask ,request ,jsonify ,send_from_directory
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app, origins="http://localhost:3000")

@app.route('/api/v1/employees', methods=['GET'])
@app.route('/prodcuts/<int:product_id>', methods=['GET'])
def get_products(product_id=None):
    products = load_products()
    if product_id is None:
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
        
        
def load_products():
    with open('products.json','r') as f:
        return json.load(f)['products']   



@app.route('/products/add', methods=['POST'])
def add_product():
    new_product = request.json
    products = load_products()
    new_product['id'] = len(products) + 1
    products.append(new_product)
    with open ('products.json', 'w') as f:
        json.dump({"products": products},f)
    return jsonify(new_product), 201

@app.route('/products-images/<path:filename>')
def get_image(filename):
    return send_from_directory('products-images', filename)


if __name__ == '__main__':
    app.run(debug=True)
