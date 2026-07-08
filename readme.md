# ✈️ TripMate AI --- Multi-Agent Travel Planner

## Overview

TripMate AI is an AI-powered travel planning platform built using
**LangGraph** and multiple specialized AI agents. It generates complete
travel itineraries by combining real-time flight information, web
search, hotel recommendations, sightseeing suggestions, and budget
planning into a single AI response.

## Features

-   🤖 Multi-Agent architecture with LangGraph
-   ✈️ Flight search using AviationStack
-   🌍 Web search using Tavily
-   🏨 Hotel recommendations
-   🗺️ AI itinerary generation
-   💰 Budget planning
-   💬 Thread-based conversations
-   📄 Markdown rendering
-   📥 PDF export
-   📋 Copy results
-   📱 Responsive UI

## Architecture

``` text
User
 │
 ▼
Frontend (HTML/CSS/JavaScript)
 │
 ▼
REST API
 │
 ▼
LangGraph Router
 │
 ├── Flight Agent
 │      └── AviationStack
 │
 ├── Search Agent
 │      └── Tavily
 │
 ├── Hotel Agent
 ├── Budget Agent
 ├── Itinerary Agent
 │
 ▼
LLM
 │
 ▼
Final Travel Plan
```

## Tech Stack

### Frontend

-   HTML5
-   CSS3
-   JavaScript
-   Marked.js
-   html2pdf.js

### Backend

-   Python
-   FastAPI or Django REST Framework
-   LangGraph
-   LangChain

### APIs

-   AviationStack
-   Tavily Search

### Database

-   PostgreSQL (optional)
-   Redis (optional)
-   Vector Database (optional)

## Folder Structure

``` text
tripmate-ai/
│
├── backend/
│   ├── main.py
│   ├── graph/
│   ├── agents/
│   ├── tools/
│   ├── utils/
│   └── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── .env
├── README.md
└── requirements.txt
```

## Environment Variables

``` env
AVIATIONSTACK_API_KEY=YOUR_KEY
TAVILY_API_KEY=YOUR_KEY
GROQ_API_KEY=YOUR_KEY
DEFAULT_ORIGIN_IATA=DEL
```

## Installation

``` bash
git clone https://github.com/yourusername/tripmate-ai.git
cd tripmate-ai
python -m venv venv
```

Windows

``` bash
venv\Scripts\activate
```

Linux/macOS

``` bash
source venv/bin/activate
```

Install dependencies

``` bash
pip install -r requirements.txt
```

## Run

FastAPI

``` bash
uvicorn main:app --reload
```

Django

``` bash
python manage.py runserver
```

## API

### POST /api/travel

Request

``` json
{
  "message":"Plan a 7 day Japan trip from India",
  "thread_id":"optional"
}
```

Response

``` json
{
  "success": true,
  "thread_id":"abc123",
  "answer":"# Japan Trip\n..."
}
```

## Multi-Agent Workflow

### Flight Agent

Fetches live flight status using AviationStack.

### Search Agent

Searches the web using Tavily.

### Hotel Agent

Suggests accommodation based on budget and destination.

### Budget Agent

Calculates estimated travel cost.

### Itinerary Agent

Creates a day-by-day travel schedule.

### Response Agent

Combines outputs into a single markdown response.

## Example Prompts

-   Plan a complete 7 days Japan trip from India.
-   Plan a Dubai trip with flights and hotels.
-   Give me all country flight information.
-   Plan a Thailand trip under ₹1,00,000.

## Error Handling

The platform handles:

-   Missing API keys
-   Network failures
-   Invalid user input
-   API timeouts
-   Empty responses
-   Markdown rendering fallback
-   PDF generation errors

## Future Improvements

-   Authentication
-   Saved itineraries
-   Maps integration
-   Weather API
-   Payment gateway
-   Real flight pricing
-   Email export
-   Multilingual support

## License

MIT License
