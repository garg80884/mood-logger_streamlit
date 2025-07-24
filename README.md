A simple mental health mood classifier using logistic regression on text.


💻 How to Run the Project
1. Install Dependencies

pip install -r requirements.txt
2. Train the Model

python train_emotion_model.py
This saves model.pkl in the model/ folder.

3. Start the Web App

python app.py
Visit http://localhost:5000 in your browser.

mood-logger/
│
├── app.py                     # Flask app
├── train_emotion_model.py     # Model training script
├── requirements.txt
├── README.md
│
├── data/
│   └── goemotions_mini_subset.csv
│
├── model/
│   └── model.pkl              # Saved ML model
│
├── static/
│   └── style.css              # Styling
│
└── templates/
    └── index.html             # Web frontend


✅ Part 2: Deploy on Streamlit Community Cloud
🔹 Step 1: Log In to Streamlit
Go to https://share.streamlit.io

Log in with your GitHub account

🔹 Step 2: Deploy the App
Click “+ New App”

Select your repository: mood-logger

Set the following:

Branch: main

Main file path: app.py

Click Deploy

💡 Streamlit will install dependencies and launch your app.

✅ Done! 🎉
You’ll get a public URL like:

arduino
Copy
Edit
https://your-username-mood-logger.streamlit.app
🔧 Optional: To update your app in future
After making changes:

bash
Copy
Edit
git add .
git commit -m "Update features"
git push
Streamlit will automatically redeploy with the latest version.

