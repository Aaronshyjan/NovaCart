@app.route('/cart')
def cart():
    if 'user' not in session:
        return redirect(url_for('login'))

    user_cart = mongo.db.carts.find_one({'user': session['user']})
    cart_items = []
    total_price = 0

    if user_cart:
        for item in user_cart['items']:
            product = mongo.db.products.find_one({'_id': item['product_id']})
            if product:
                total_price += product['price'] * item['quantity']
                cart_items.append({'name': product['name'], 'price': product['price'], 'quantity': item['quantity'], 'image_url': product['image_url']})

    return render_template('cart.html', cart_items=cart_items, total_price=total_price)
