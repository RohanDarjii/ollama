# ✈️ TripMate AI — Multi-Agent Travel Planner

TripMate AI is an AI-powered multi-agent travel planning platform that helps users generate complete travel plans including flights, hotels, sightseeing, budgets, and itineraries.

It uses a LangGraph-based multi-agent workflow with external APIs such as AviationStack and Tavily to collect real-time travel-related information and generate structured travel plans.

---

## 🚀 Features

- AI-powered travel planning
- Multi-agent architecture using LangGraph
- Flight search using AviationStack API
- Web search using Tavily API
- Hotel and sightseeing recommendation support
- Budget-aware itinerary generation
- Thread-based conversation memory
- Markdown-rendered AI responses
- Copy travel plan
- Download travel plan as PDF
- Responsive modern frontend UI
- Dark glassmorphism GPT-style interface

---

## 🧠 System Architecture

```text
User
 │
 ▼
Frontend HTML/CSS/JS
 │
 ▼
Backend API
 │
 ▼
LangGraph Multi-Agent Workflow
 │
 ├── Flight Agent
 │    └── AviationStack API
 │
 ├── Search Agent
 │    └── Tavily API
 │
 ├── Hotel Agent
 │
 ├── Itinerary Agent
 │
 └── Budget Agent
 │
 ▼
LLM Response Generator
 │
 ▼
Structured Travel Plan