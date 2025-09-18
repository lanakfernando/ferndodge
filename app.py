from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return "ok", 200

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    r = MessagingResponse()
    r.message("It works! 🌟 Your webhook is connected.")
    return str(r)

# Optional: lets you run locally too, but Render will use gunicorn (below)
if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
