# Setup Guide

## Zapier Path (Recommended for beginners)
1. Create a new Zap
2. Trigger: Webhooks by Zapier → Catch Hook
3. Code by Zapier → Run Python (paste the sentiment code from earlier messages)
4. API Request → GET VirusTotal
5. GitHub → Create Issue
6. Turn on and test

## Standalone Script Path
1. Deploy `enricher.py` to Render.com (free)
2. Set VIRUSTOTAL_API_KEY as environment variable
3. Use the deployed URL as webhook in Zapier or directly with curl

Test command:
curl -X POST https://your-app.onrender.com/enrich -H "Content-Type: application/json" -d '{"alert_text": "Critical login from 8.8.8.8"}'