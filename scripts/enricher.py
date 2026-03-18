from flask import Flask, request, jsonify
import requests
import re
import os

app = Flask(__name__)

VT_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

def simple_sentiment(text):
    text_lower = text.lower()
    if any(word in text_lower for word in ['critical', 'breach', 'malicious', 'attack', 'threat']):
        return "CRITICAL"
    elif any(word in text_lower for word in ['warning', 'suspicious']):
        return "MEDIUM"
    return "LOW"

@app.post("/enrich")
def enrich_alert():
    data = request.get_json()
    alert_text = data.get("alert_text", "")
    ioc_value = data.get("ioc_value")
    
    # Auto-extract IP if missing
    if not ioc_value:
        match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', alert_text)
        ioc_value = match.group(0) if match else None
    
    # VirusTotal lookup
    vt_data = {}
    if ioc_value:
        try:
            resp = requests.get(
                f"https://www.virustotal.com/api/v3/ip_addresses/{ioc_value}",
                headers={"x-apikey": VT_API_KEY},
                timeout=10
            )
            resp.raise_for_status()
            vt_data = resp.json()
        except Exception as e:
            vt_data = {"error": str(e)}
    
    sentiment = simple_sentiment(alert_text)
    malicious = vt_data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {}).get("malicious", 0)
    
    return jsonify({
        "sentiment": sentiment,
        "ioc_value": ioc_value,
        "vt_malicious": malicious,
        "vt_link": f"https://www.virustotal.com/gui/ip-address/{ioc_value}" if ioc_value else None,
        "enriched_text": f"{alert_text}\nSentiment: {sentiment} | VT Malicious: {malicious}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))