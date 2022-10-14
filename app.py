from flask import Flask, render_template, request

from counter import *
from read_csv import *

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
counter = Counter(read_item_list())

counter.clear_cart()
counter.set_discount(0.1)
counter.set_tax(0.15)

@app.route('/', methods=["GET", "POST"])
def index():
    output = []
    if 'item' in request.form:
        new_item = request.form['item']
        new_num = request.form['num']

        if request.form.get('Reset') == 'Reset':
            counter.clear_cart()

        if request.form.get('Checkout') == 'Checkout':
            output = counter.print_invoice()

        if new_num.isdigit() and new_item.isdigit():
            if 0 < int(new_num) and 0 < int(new_item) < 7:
                if request.form.get('Add') == 'Add':
                    counter.add_cart(int(new_item), int(new_num))
                elif request.form.get('Remove') == 'Remove':
                    counter.remove_cart(int(new_item), int(new_num))

    return render_template("index.html", cart=counter.show_cart(), invoice=output)

app.run()