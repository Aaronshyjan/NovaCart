@app.route('/add_to_cart/<product_id>')
def add_to_cart(product_id):
    if 'user' not in session:
        return redirect(url_for('login'))

    user_cart = mongo.db.carts.find_one({'user': session['user']})

    if user_cart:
        for item in user_cart['items']:
            if str(item['product_id']) == product_id:
                item['quantity'] += 1
                break
        else:
            user_cart['items'].append({'product_id': ObjectId(product_id), 'quantity': 1})
        mongo.db.carts.update_one({'user': session['user']}, {'$set': {'items': user_cart['items']}})
    else:
        mongo.db.carts.insert_one({'user': session['user'], 'items': [{'product_id': ObjectId(product_id), 'quantity': 1}]})

    return redirect(url_for('cart'))
