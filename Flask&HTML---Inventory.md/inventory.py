## Python code:

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

inventory = []

@app.route('/')
def home():
    return render_template('index.html', inventory=inventory)

@app.route('/add', methods=['POST'])
def add_item():
 
    item_name = request.form['item_name']
    item_quantity = int(request.form['item_quantity'])

    inventory.append({'name': item_name, 'quantity': item_quantity})

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
