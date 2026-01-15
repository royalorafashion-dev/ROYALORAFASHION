# app.py - FOR FUTURE SERVER USE (Not GitHub Pages)
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Admin Info
OWNER_PHONE = "919662726807"
STUDENT_ID = "Jyot 24IC02IT012"

@app.route('/')
def home():
    # In a real Python app, you'd fetch these from a database
    products = [
        {"name": "240 GSM French Terry", "price": 450},
        {"name": "Boxy Fit Tee", "price": 300}
    ]
    return render_template('index.html', products=products)

@app.route('/order', methods=['POST'])
def order():
    item = request.form.get('product_name')
    customer_contact = request.form.get('contact')
    
    print(f"New Order from {customer_contact} for {item}")
    # Here you could save to SQL database
    
    return f"Order Received! We will call you at {customer_contact}"

if __name__ == '__main__':
    print(f"Starting Server... {STUDENT_ID}")
    app.run(debug=True)
