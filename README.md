# Places Search API — Free Business Search

Zero-cost global business search. No API keys. No sign-up. Deploy anywhere.

**Data source:** OpenStreetMap (Nominatim + Overpass API)
**Cost:** Free, forever
**Rate limits:** ~1 req/sec (Nominatim), reasonable use

## Run

```bash
pip install -r requirements.txt
python main.py
# → http://localhost:8000/docs
```

## Endpoints

| Endpoint | Params | Description |
|----------|--------|-------------|
| `/search` | `query`, `location`, `limit` | Search businesses by keyword + location |
| `/search-nearby` | `query`, `lat`, `lng`, `limit` | Search by coordinates (better for categories) |
| `/health` | — | Health check |

## Test

```bash
curl "http://localhost:8000/search?query=coffee+shop&location=New+York&limit=5"
curl "http://localhost:8000/search-nearby?query=restaurant&lat=40.7128&lng=-74.006&limit=5"
```

## Deploy to Render (free)

1. Push to GitHub
2. New Web Service → set start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
3. Done. Your API is live.

## RapidAPI Publishing

1. Deploy → note the URL (e.g. `https://your-api.onrender.com`)
2. Go to [rapidapi.com/studio](https://rapidapi.com/studio) → Add API Project
3. Set API Base URL to your deployed URL
4. Import from `/openapi.json`
5. Set pricing in Monetize tab — RapidAPI handles billing, you just collect
