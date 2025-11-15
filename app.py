from flask import Flask, render_template, request
from kasir_logic import prices, hitung_total, hitung_diskon

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        qty = {key: int(request.form.get(key, 0) or 0) for key in prices}

        total, detail = hitung_total(qty)
        ultah = request.form.get('ultah', 'n').lower()
        diskon = hitung_diskon(total, ultah)
        subtotal = total - diskon

        return render_template(
            'bill.html',
            qty=qty,
            detail=detail,
            prices=prices,
            total=total,
            diskon=diskon,
            subtotal=subtotal,
            ultah=ultah
        )

    return render_template('index.html', prices=prices)

if __name__ == '__main__':
    app.run(debug=True)
