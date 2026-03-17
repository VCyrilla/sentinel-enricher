# Sentinel Enricher

> Automated security alert triage and enrichment pipeline.

Sentinel Enricher ingests security alerts from multiple sources (email, Datadog, Intruder, or any webhook), enriches them with threat intelligence via VirusTotal, and automatically creates a GitHub Issue or posts a structured Slack summary

---

## How It Works

1. **Ingest** — Receives alerts from email, Datadog monitors, Intruder scans, or generic webhooks via Zapier
2. **Analyze** — Applies lightweight NLP sentiment scoring to classify alert urgency
3. **Enrich** — Queries the VirusTotal API for contextual threat intelligence on IPs, domains, or hashes found in the alert
4. **Deliver** — Creates a structured GitHub Issue or posts a formatted Slack summary with all enrichment data attached

---

## Quickstart

Full setup guide: [`docs/setup.md`](docs/setup.md)

| Step | Action |
|------|--------|
| 1 | Clone this repo and deploy `scripts/enricher.py` to [Render](https://render.com) or [Replit](https://replit.com) |
| 2 | Set your environment variables (see `.env.example`) |
| 3 | Import the Zap template: *(link coming soon)* |
| 4 | Connect your alert sources in Zapier |
| 5 | Trigger a test alert and verify the output |

---

## Requirements

- Python 3.9+
- Zapier account (Free tier supported)
- VirusTotal API key (free tier available)
- GitHub or Slack account for output delivery

---

## Configuration

Copy `.env.example` to `.env` and fill in the required values:
```env
VIRUSTOTAL_API_KEY=your_key_here
GITHUB_TOKEN=your_token_here
GITHUB_REPO=owner/repo-name
SLACK_WEBHOOK_URL=https://hooks.slack.com/...
```

---

## Supported Alert Sources

| Source | Trigger Method |
|--------|---------------|
| Email | Zapier Email Parser |
| Datadog | Webhook monitor notification |
| Intruder | Webhook integration |
| Custom | Any HTTP POST webhook |

---

## Project Structure
```
sentinel-enricher/
├── scripts/
│   └── enricher.py       # Core enrichment logic — deploy this
├── docs/
│   └── setup.md          # Full configuration walkthrough
├── .env.example
└── README.md
```

---

## Contributing

Pull requests are welcome. For significant changes, please open an issue first to discuss what you'd like to change.

---

## License

[MIT](LICENSE)
