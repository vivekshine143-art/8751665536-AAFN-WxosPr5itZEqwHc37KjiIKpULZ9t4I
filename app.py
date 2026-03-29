from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8751665536:AAFN-WxosPr5itZEqwHc37KjiIKpULZ9t4I"
CHAT_ID = "1003861262690"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    entry = float(data["entry"])
    trade_type = data["type"]

    risk = entry * 0.02

    if trade_type == "BUY":
        sl = entry - risk
        t1 = entry + (risk * 1.5)
        t2 = entry + (risk * 2)
        t3 = entry + (risk * 3)
    else:
        sl = entry + risk
        t1 = entry - (risk * 1.5)
        t2 = entry - (risk * 2)
        t3 = entry - (risk * 3)

    message = f"""
🔥 {trade_type} SIGNAL 🔥

Entry: {entry}
SL: {round(sl,2)}

Target 1: {round(t1,2)}
Target 2: {round(t2,2)}
Target 3: {round(t3,2)}

🚀 Auto Bot
"""

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})

    return "ok"

app.run(port=5000)
