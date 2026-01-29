🧠 Agentic AI Task Executor

This project demonstrates a basic Agentic AI system that can autonomously execute multiple tasks—such as studying a topic and scheduling a meeting—based on user-defined priority. Unlike traditional Generative AI systems that only respond to prompts, this agent perceives tasks, reasons about priority, and takes real-world actions using external APIs.

🚀 Features

Interactive, console-based Agentic AI

Supports multiple task types:

📘 Study a topic

📅 Schedule a Google Calendar meeting

Executes tasks based on priority

Uses Google Calendar API for real-world action

Modular design following:

Perception

Planning

Action

Demonstrates core principles of Agentic AI
```
🧩 System Architecture
User Input
   ↓
Perception Module (Collect tasks)
   ↓
Planning Module (Sort by priority)
   ↓
Action Module
   ├── Study Agent
   └── Calendar Agent (Google Calendar API)
```
## 📂 Project Structure
```
trialagent/
│
├── main.py                 # Main agent loop
├── study_agent.py          # Study-related actions
├── calendar_agent.py       # Google Calendar integration
├── priority_manager.py     # Task prioritization logic
├── credentials.json        # Google API credentials (not committed)
├── token.json              # OAuth token (auto-generated)
└── README.md
```

⚙️ Prerequisites

Python 3.9+

Google account

Google Calendar API enabled

Required Python libraries:

pip install google-api-python-client google-auth google-auth-oauthlib

🔑 Google Calendar Setup

Go to Google Cloud Console

Create a project

Enable Google Calendar API

Create OAuth Client ID

Download credentials.json

Place it in the project root

⚠️ Do NOT commit credentials.json or token.json to GitHub.

▶️ How to Run
python main.py


You will be prompted to:

Enter a study topic and its priority

Enter meeting details (title, time, attendees) and priority

The agent will:

Sort tasks by priority

Execute them automatically

Schedule meetings on Google Calendar

🖥️ Sample Console Interaction
🎯 Agent Goal: Execute study and meeting tasks based on user-defined priority

🧠 Task 1: Study Topic
Enter topic to study: Agentic AI
Enter priority for study task: 2
```
📅 Task 2: Schedule Meeting
Enter meeting title: AI Review Meeting
Enter start time (YYYY-MM-DDTHH:MM:SS): 2026-01-20T10:00:00
Enter end time (YYYY-MM-DDTHH:MM:SS): 2026-01-20T11:00:00
Enter attendee emails: a@gmail.com, b@gmail.com
Enter priority for meeting task: 1
```
🧠 Why This Is Agentic AI

This system:

Accepts goals instead of static commands

Makes decisions based on priority

Uses tools (Google Calendar API)

Executes real-world actions

Adapts behavior based on user input

This clearly demonstrates the evolution from Generative AI → Agentic AI.