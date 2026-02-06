from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    """Read products from JSON file"""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def read_csv():
    """Read products from CSV file"""
    try:
        products = []
        with open('products.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
        return products
    except FileNotFoundError:
        return None
    except (ValueError, KeyError):
        return None

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Validate source parameter
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    
    # Read data based on source
    if source == 'json':
        products_data = read_json()
    else:  # csv
        products_data = read_csv()
    
    # Handle file reading errors
    if products_data is None:
        return render_template('product_display.html', error="Error reading data")
    
    # Filter by ID if provided
    if product_id:
        try:
            product_id = int(product_id)
            products_data = [p for p in products_data if p['id'] == product_id]
            if not products_data:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Invalid product ID")
    
    return render_template('product_display.html', products=products_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
