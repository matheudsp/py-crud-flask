# url base - localhost
# endpoints - 
    # /products    (GET)
    # /products/id (GET)
    # /products/id (PUT)
    # /products/id (POST)
    # /products/id (DELETE)

from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {
        'id': 1,
        'name': 'Echo Dot (4ª Geração): Smart Speaker com Alexa | Música, informação e Casa Inteligente - Cor Preta',
        'category': 'Electronics',
        'price': '379,05', 
        'url':'https://www.amazon.com.br/Novo-Echo-Dot-4%C2%AA-gera%C3%A7%C3%A3o/dp/B084DWCZY6/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2G6DFD401R1L9&keywords=alexa&qid=1675339627&sprefix=ale%2Caps%2C195&sr=8-1&ufe=app_do%3Aamzn1.fos.95de73c3-5dda-43a7-bd1f-63af03b14751&th=1'
    },
    {
        'id': 2,
        'name': 'Console PlayStation 5',
        'category': 'Games and Console',
        'price': '4.499,90', 
        'url':'https://www.amazon.com.br/PlayStation-CFI-1214A01X-Console-5/dp/B0BNSR3MW9/ref=sr_1_2?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3HTYEEUH02GRW&keywords=ps5&qid=1675339731&sprefix=p%2Caps%2C180&sr=8-2&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147'
    },
    {
        'id': 3,
        'name': 'HD SSD Kingston SA400S37 480GB',
        'category': 'Computers and IT',
        'price': '186,98',
        'url':'https://www.amazon.com.br/HD-SSD-KINGSTON-SA400S37-480GB/dp/B075BKXSCQ/ref=zg_bs_computers_sccl_1/138-9323391-1394721?psc=1' 
    },
    {
        'id': 4,
        'name': 'Suporte Articulado de Mesa com Pistão a Gás Para Monitores de 17 a 35 até 9kg - F80N ELG',
        'category': 'Computers and IT',
        'price': '199,99',
        'url':'https://www.amazon.com.br/Suporte-Monitor-Elg-F80N-Preto/dp/B0765KZ264/ref=zg_bs_computers_sccl_6/138-9323391-1394721?psc=1' 
    },
    
]

# /products    (GET) - view all
@app.route('/products', methods=['GET'])
def get_products():
    
    return jsonify(products)

# /products/id (GET) - view a specific product
@app.route('/products/<int:id>', methods=['GET'])
def get_product_per_id(id):
    for product in products:
        if product.get('id') == id:

            return jsonify(product)
        
# /products/id (PUT)
@app.route('/product/<int:id>', methods=['PUT'])
def modify_product_per_id(id):
    modify_product = request.get_json()

    for index, product in enumerate(products):
        if product.get('id') == id:
            products[index].update(modify_product)

            return jsonify(products[index])

# /products/id (POST)
@app.route('/product/<int:id>', methods=['POST'])
def include_new_product():
    new_product = request.get_json()
    products.append(new_product)

    return jsonify(products)

# /products/id (DELETE)
@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    for index, product in enumerate(products):
        if product.get('id') == id:
            del products[index]

            return jsonify(products)


app.run(port=5000, host='localhost',debug=True)