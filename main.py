from flask import Flask, jsonify, request
import random
import string

app = Flask(__name__)

# ডোমেইন লিস্ট
domains = [
    "1secmail.com",
    "1secmail.org",
    "1secmail.net",
    "wwjmp.com",
    "esiix.com",
    "xojxe.com",
    "yoggm.com"
]

# র‍্যান্ডম স্ট্রিং তৈরি করার ফাংশন
def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# মেইল তৈরি করার রুট
@app.route('/v1', methods=['GET'])
def create_temp_mail():
    if request.args.get('tempmail') == 'create':
        emails = [f"{generate_random_string()}@{domain}" for domain in domains]
        return jsonify(emails)
    else:
        return jsonify({"error": "Invalid query parameter"}), 400

if __name__ == '__main__':
    app.run(debug=True)
