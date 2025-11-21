
🥤 Water Intake Tracker

A simple and efficient Python-based application for tracking daily water consumption.
This project helps users build healthier hydration habits by logging their water intake, storing the data, and retrieving historical usage records.


---

📌 Features

Log Water Intake: Record the amount of water consumed at any time.

SQLite Database Storage: All logs are stored locally for easy access and long-term tracking.

Easy API/Script Access: Lightweight Python modules (app.py, api.py, agent.py) make it easy to integrate or automate logging.

Activity Logging: Error and event tracking handled through logger.py.

Simple Architecture: 100% Python with no heavy dependencies, easy to understand and customize.



---

📁 Project Structure

water-intake-tracker/
│
├── app.py                # Main application entry point
├── api.py                # API functions or endpoints for interacting with the tracker
├── agent.py              # Automation/CLI agent for handling repeated tasks
├── database.py           # SQLite database connection + CRUD operations
├── logger.py             # Application logging utilities
├── water_tracker.db      # SQLite database file
└── requirements.txt      # Project dependencies


---

🚀 Getting Started

1. Clone the Repository

git clone https://github.com/Chizzy0428/water-intake-tracker.git
cd water-intake-tracker

2. Install Dependencies

pip install -r requirements.txt

3. Run the Application

Depending on your setup:

python app.py

or

python agent.py

or use functions inside api.py directly.


---

🗄️ How It Works

1. User logs water intake (e.g., 250ml, 500ml).


2. Entry is saved into an SQLite table through database.py.


3. Logs can be retrieved, summarized, and displayed through API or script.


4. logger.py tracks internal operations and errors for debugging.




---

🧩 Possible Improvements (Roadmap)

Future upgrades you can add:

🌐 Add a Streamlit or web dashboard for visualizing daily/weekly hydration trends.

🔔 Reminder notifications to encourage consistent drinking habits.

🎯 Daily water goal + progress tracking.

📊 Analytics: averages, streaks, and monthly summaries.

👤 Multi-user support for shared installations.

📤 Export logs to CSV/Excel.

☁️ Move to cloud database if scaling beyond local use.



---

🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests to enhance features, improve efficiency, or expand functionality.


---

📜 License

This project is released under the MIT License.
You are free to modify and use it in your code.
