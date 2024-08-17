from flask import Flask, jsonify, request
import random
import string

app = Flask(__name__)

# ডোমেইনের তালিকা
domains = [
    "1secmail.com",
    "1secmail.org",
    "1secmail.net",
    "wwjmp.com",
    "esiix.com",
    "xojxe.com",
    "yoggm.com"
]

# র্যান্ডম ইউজারনেম তৈরি ফাংশন
def generate_username(length=8):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))

# মেইল তৈরি এবং JSON রেসপন্স প্রদান ফাংশন
@app.route('/v1', methods=['GET'])
def create_temp_mail():
    if request.args.get('tempmail') == 'create':
        username = generate_username()
        domain = random.choice(domains)
        temp_email = f"{username}@{domain}"
        
        # JSON আকারে রেসপন্স প্রদান
        return jsonify({"email": temp_email}), 200
    else:
        return jsonify({"error": "Invalid request"}), 400

if __name__ == '__main__':
    app.run(debug=True)
