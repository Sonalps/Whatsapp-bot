from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from googlesearch import search  

app = Flask(__name__)

@app.route("/bot", methods=['POST'])
def bot():
    # user input
    user_msg = request.values.get('Body', '').lower()

    # creating object of MessagingResponse
    response = MessagingResponse()

    # User Query
    q = user_msg + " site:geeksforgeeks.org"

    # list to store urls
    search_results = []

    # searching and storing urls
    for i in search(q, tld='co.in', num=6, stop=6, pause=2):
        search_results.append(i)

    # displaying result
    msg = response.message(f"--- Results for '{user_msg}' ---")
    for result in search_results:
        msg.body(result)

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
