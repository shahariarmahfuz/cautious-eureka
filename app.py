from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

# ডোমেইনগুলোর তালিকা
domains = [
    "1secmail.com",
    "1secmail.org",
    "1secmail.net",
    "wwjmp.com",
    "esiix.com",
    "xojxe.com",
    "yoggm.com"
]

# র্যান্ডম মেইল নাম তৈরি করার ফাংশন
def generate_random_mail_name():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

# /v1?tempmail রুট
@app.route('/v1', methods=['GET'])
def generate_temp_mails():
    mail_addresses = [f"{generate_random_mail_name()}@{domain}" for domain in domains]
    return jsonify(mail_addresses)

# অ্যাপ রান করানোর জন্য
if __name__ == '__main__':
    app.run(debug=True)
