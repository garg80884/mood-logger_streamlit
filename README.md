
# Mood Logger – AI Mood Tracker and Tips Generator

A simple yet smart Streamlit web app to help users **log their mood**, **track mood history**, and **get personalized tips** for emotional well-being. Supports user login and CSV-based mood storage.

## 🧠 What the App Does

**MoodLogger AI** is a web-based mood detection and logging application that allows users to:
- Log their current mood using a simple and attractive interface.
- Visualize mood patterns over time.
- Get mood improvement tips based on past emotional trends.
- Authenticate and manage their entries securely.

## 🚀 Features

- 🔐 User Authentication (session-based)
- 😊 Mood Logging with reason and mood level
- 📈 Visualize mood trends over time
- 💡 Smart Mood Tips based on user entries
- 📱 Mobile Responsive & Professional UI
- 💾 Stores all data in `mood_log.csv` (no database required)



## 🔐 Default Users (for testing)

| Username | Password |
|----------|----------|
| `demo`  | `demo`  |
| `abc`   | `abc`   |

> (For production, you can connect to a database or use secure login methods.)

---

## 🛠️ How the ML Model Was Developed and Trained

We trained a multi-label emotion classification model using the **GoEmotions** dataset (released by Google Research). This dataset includes over 58k English Reddit comments labeled with 27 emotion categories.

### Model Training:
- **Framework**: PyTorch
- **Tokenizer**: Custom vocabulary with text preprocessing (no LLMs or pre-trained transformers used)
- **Model Architecture**: A simple feed-forward neural network with TF-IDF feature extraction
- **Validation Accuracy**: ~83% across 27 classes

### Dataset Source:
- [GoEmotions Dataset on GitHub](https://github.com/google-research/google-research/tree/master/goemotions/data)

## 🔗 ML Integration in the App

The trained model is integrated in the backend to:
- Classify user input text (mood description) into emotional categories.
- Store results in a CSV file with timestamped entries.
- Dynamically suggest tips and visualizations based on detected moods.

## 🚀 Tech Stack

- **Frontend**: Streamlit UI (custom styled)
- **Backend**: Python, CSV-based storage
- **Visualization**: Matplotlib
- **Authentication**: Username-password validation using secure hash comparison

## 🎯 Problem It Solves

Mental health tracking is often manual and inconsistent. MoodLogger AI addresses this by providing:
- Real-time emotional recognition from user input
- Easy-to-understand mood trends and graphs
- Supportive recommendations for better emotional health


## ⚙️ Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/garg80884/mood-logger_streamlit.git
cd mood-logger_streamlit
```

2. Create and activate virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
streamlit run app.py
```

## ✅ Requirements (requirements.txt)

```
streamlit
scikit-learn
pandas
matplotlib
```

## 🔐 Authentication

Only authenticated users can log moods and access tips.



## 📝 License

MIT License – Free to use, modify, and share.

---

## ❤️ Made with Streamlit

This project was built as a minimalistic tool for tracking emotions and generating actionable well-being suggestions using AI.


## 🌟 Live App

You can try the live version here: [Mood Logger Streamlit App](https://mood-logger-80884.streamlit.app/)

## 💻 GitHub Repository

Full codebase and ML training scripts: [GitHub - Mood Logger](https://github.com/garg80884/mood-logger_streamlit)

