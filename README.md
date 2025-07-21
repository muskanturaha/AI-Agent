🧠 BrandPulse Watchdog
Real-time Customer Sentiment Spike Detector for Support Teams

🔍 Problem Statement
Support and CX teams receive hundreds of messages across chats, emails, and tickets every day.
But they often find out too late when customer frustration spikes — after churn, chaos, or escalations.

BrandPulse Watchdog is an AI agent that scans incoming support data, classifies sentiment, emotion, urgency, and type, and alerts teams when there's a sudden surge in negative emotions.

🚀 What It Does
📥 Reads live support messages from CSV or real-time input (chats, emails, tickets)

🧠 Classifies each message for:

Sentiment: positive / negative

Emotion: anger, joy, sadness, etc.

Urgency: low / medium / high

Type: complaint, request, praise, etc.

🔄 Uses a sliding 5-minute window to track trends

📊 Saves window-wise stats to window_stats.csv for RAG-style analysis

🔔 Sends Slack alerts if high-urgency negative messages spike above a threshold

📈 Includes a live dashboard (Streamlit) for monitoring and analytics

📁 Folder Structure
bash
Copy
Edit
brandpulse_watchdog/
│
├── main.py                # Run the agent here
├── classifier.py          # Multi-task message classification logic
├── spike_detector.py      # Sliding window + alert threshold logic
├── slack_alert.py         # Slack webhook alert sender
├── dashboard.py           # Streamlit dashboard (optional)
├── requirements.txt       # Dependencies
├── sample_tickets.csv     # Test dataset (30 mins of support messages)
├── classified_output.csv  # Output (created after run)
├── window_stats.csv       # Window-by-window metrics (created after run)
🛠️ Setup & Usage
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/yourusername/brandpulse_watchdog.git
cd brandpulse_watchdog
2. Create Virtual Env (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the Agent
bash
Copy
Edit
python main.py --csv sample_tickets.csv --slack_url "YOUR_SLACK_WEBHOOK_URL"
Outputs classified_output.csv and window_stats.csv

Sends Slack alerts if needed

5. Launch the Dashboard (Optional)
bash
Copy
Edit
streamlit run dashboard.py
Upload the CSVs to view trends and insights

🧪 Test Data
You can test the system with sample_tickets.csv, which includes 30 minutes of support-style messages with timestamps spaced every 2 minutes.

📦 Slack Alert Example
bash
Copy
Edit
🚨 Spike in Negative Sentiment
7 high-urgency angry/sad messages in the last 5 mins (28% of 25).
📊 Dashboard Preview
Message table with sentiment breakdown

Emotion, urgency, type charts

Line chart of high-urgency negatives per 5-minute window

Upload any output CSV for custom analysis

💡 Future Ideas
RAG-based summary or Q&A on historical spikes

Root cause extraction from complaints

AI reply suggestions for support teams

Real-time chat plugin

🧑‍💻 Built With
Python 🐍

🤗 Transformers

Streamlit

Slack Webhooks

Altair Charts

TQDM / Pandas

📣 Credits
Project built during the AI Agent Hackathon by Product Space
Designed for PMs + AI builders to solve real-world product problems.

📬 Questions or Suggestions?
Drop a GitHub issue or connect on LinkedIn. Contributions welcome!

