import pyotp
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

admin_otp = 'QGHVTKVH3MJI34DC6XKFGOQMNHFJIB2I'  # change to you're own key

# create new key 
# print(pyotp.random_base32())

otp_obj = pyotp.TOTP(admin_otp)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_otp = request.form.get('otp-code')
        if not user_otp.isdigit():
            return jsonify({'error': 'please type number only!'})
        if otp_obj.verify(user_otp):
            return jsonify({'verify': 'true'})
        return jsonify({'verify': 'false'})
    return render_template('index.html')


app.run()
