from flask import Flask, render_template, request
import json
import csv
import sqlite3

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

def read_sql():
    """Read products from SQLite database"""
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        conn.close()
        
        products = []
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        return products
    except sqlite3.Error:
        return None

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Validate source parameter
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")
    
    # Read data based on source
    if source == 'json':
        products_data = read_json()
    elif source == 'csv':
        products_data = read_csv()
    else:  # sql
        products_data = read_sql()
    
    # Handle file/database reading errors
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
