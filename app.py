from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def is_spam(email_content):
    spam_keywords = ['win', 'free', 'click', 'urgent', 'winner', 'cash', 'prize', 'buy now']
    # Basic checks for spam
    if any(keyword in email_content.lower() for keyword in spam_keywords):
        return True
    return False

@app.route('/check_spam', methods=['POST'])
def check_spam():
    data = request.json
    email_content = data.get('content', '')
    spam_result = is_spam(email_content)
    return jsonify({'is_spam': spam_result})

if __name__ == '__main__':
    app.run(debug=True)
