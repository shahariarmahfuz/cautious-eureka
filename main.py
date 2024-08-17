from flask import Flask, jsonify, request
import random
import string

app = Flask(__name__)

domains = [
    "1secmail.com",
    "1secmail.org",
    "1secmail.net",
    "wwjmp.com",
    "esiix.com",
    "xojxe.com",
    "yoggm.com"
]

def generate_unique_username(length=8):
    """ একটি র‍্যান্ডম ইউজারনেম তৈরি করে """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

@app.route('/v1', methods=['GET'])
def generate_temp_emails():
    if 'tempmail' in request.args:
        temp_emails = []
        for domain in domains:
            username = generate_unique_username()
            temp_emails.append(f"{username}@{domain}")
        return jsonify(temp_emails)
    else:
        return jsonify({"error": "Invalid request"}), 400

# Vercel-এর জন্য অ্যাপ্লিকেশন কনফিগারেশন
if __name__ == '__main__':
    from os import environ
    app.run(host='0.0.0.0', port=int(environ.get('PORT', 5000)))
