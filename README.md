# 🛡️ Phishing Detection using Machine Learning

This project is a web-based phishing URL detection system that uses a trained machine learning model to classify URLs as **phishing** or **safe**.

## 🚀 Features

- Detects phishing URLs using trained ML model
- Feature extraction from raw URLs
- Flask-based backend with model inference
- Web interface for user input

## 📁 Project Structure


phishing_detection_updated/
├── backend/
│   ├── __pycache__
|   |__  train_model.py
│   ├── create_sample_dataset.py
│   └── __init__.py
|   |__ app.py
|   |__ model.py
|   |__ utils.py
├── dataset/
│   └── sample_phishing_data.csv   <-- ekhane file ta thakbe
└── frontend/
|   |__images
|   |__moedels
|   |__ index.html
|   |__ login.css
|   |__ login.html
|   |__ recquirement.txt
|   |__ script.js
|   |__ sign_up.csss
|   |__ sign_up.html
|   |__ style.css
|__myenv/
|   |__ Include
|   |__ Lib
|   |__ Scripts
|___|__ pyvenv.cfg



## ⚙️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/rahulgit64/Phishing-Detection.git
   cd Phishing-Detection
## Install requirements:

   pip install -r requirements.txt

## Run the app:

    python app.py
    
## 📊 Dataset

  ### We used a labeled dataset with URL-based features such as:
     Number of dots
     URL length
     Use of @ symbol
     Presence of IP address
     etc

### 🧠 Model
The machine learning model was trained using DecisionTreeClassifier from Scikit-learn.

### 🔒 Disclaimer
This project is for educational purposes only and may not detect all phishing attempts. Use responsibly.

### 👨‍💻 Author
@rahulgit64

Feel free to edit and add more based on your project.

### 📌 How to Add This in Your Project
In your project folder, create a file:

touch README.md
(Or just right-click → New File → README.md in VS Code)

Save it.

Add & push:

git add README.md
git commit -m "Add README"
git push


