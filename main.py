from flask import Flask, jsonify, request
import random
import string
import requests

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
def handle_request():
    if 'tempmail' in request.args:
        temp_emails = []
        for domain in domains:
            username = generate_unique_username()
            temp_emails.append(f"{username}@{domain}")
        return jsonify(temp_emails)
    
    elif 'inbox' in request.args:
        inbox_email = request.args.get('inbox')
        if '@' not in inbox_email:
            return jsonify({"error": "Invalid email format"}), 400
        
        username, domain = inbox_email.split('@')
        if domain not in domains:
            return jsonify({"error": "Invalid domain"}), 400
        
        # Get messages
        get_messages_url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain}"
        response = requests.get(get_messages_url)
        messages = response.json()
        
        if not messages:
            return jsonify({"error": "No messages found"}), 404
        
        # Get the first message id
        message_id = messages[0]['id']
        
        # Get the message details
        read_message_url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain}&id={message_id}"
        response = requests.get(read_message_url)
        message_details = response.json()
        
        # Extract the required fields
        result = {
            "date": message_details.get("date"),
            "from": message_details.get("from"),
            "subject": message_details.get("subject"),
            "body": message_details.get("textBody")
        }
        
        return jsonify(result)
    
    else:
        return jsonify({"error": "Invalid request"}), 400

# Vercel-এর জন্য অ্যাপ্লিকেশন কনফিগারেশন
if __name__ == '__main__':
    from os import environ
    app.run(host='0.0.0.0', port=int(environ.get('PORT', 5000)))
