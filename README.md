# SkillAscend - AI-Powered Online Course Recommender

## 📌 Project Overview
SkillAscend is an **AI-powered online course recommender system** that provides personalized course recommendations based on a user's **educational background** and **learning goals**. It leverages a **hybrid recommendation approach** by combining **collaborative filtering (SVD)** and **content-based filtering (BERT & TF-IDF)** to suggest the most relevant courses dynamically.

## 🚀 Features
- **Personalized Recommendations**: Matches users with courses based on their education and career goals.
- **Hybrid Recommendation Approach**:
  - **Collaborative Filtering (SVD)**: Predicts user preferences based on historical interactions.
  - **Content-Based Filtering (BERT)**: Recommends courses by analyzing course descriptions and user profiles.
  - **Real-Time NLP Pipeline**: Updates recommendations dynamically as users interact with the system.
- **User-Friendly Web App**: Simple and interactive UI for seamless course discovery.

## 🏗️ Tech Stack
- **ML:** TensorFlow, scikit-learn, Surprise (SVD), Sentence Transformers (BERT), TF-IDF, Pandas, NumPy
- **Backend:** Flask, Hugging Face Spaces
- **Frontend:** React.js, Tailwind CSS, HTML

## 📂 Project Structure
```
SkillAscend/
│── data/                           # Dataset (Coursera courses & interactions)
│── models/                         # Trained models (SVD, BERT, TF-IDF)
│── backend/
│   ├── app.py                      # Flask backend for recommendations
│   ├── realtime_nlp.py              # Real-time NLP-based recommendation
│   ├── collaborative_filtering_svd.py  # SVD-based recommendation
│   ├── content_filtering_bert.py    # BERT-based content filtering
│   ├── content_filtering_tfidf.py   # TF-IDF-based content filtering
│── frontend/
│   ├── index.html                   # Web UI for recommendations
│   ├── static/                      # CSS, JavaScript, images
│── README.md                        # Project documentation
│── requirements.txt                  # Python dependencies
```

## 🔧 Installation & Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/SkillAscend.git
   cd SkillAscend
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Backend**:
   ```bash
   python backend/app.py
   ```
4. **Access the Web App**:
   Open `http://127.0.0.1:5000/` in your browser.

## 📊 How It Works
1. **User inputs** their **education** and **learning goals**.
2. **BERT & TF-IDF** process the user profile and compute similarity with course descriptions.
3. **SVD-based collaborative filtering** predicts courses based on past user interactions.
4. The **top 5 courses** are recommended and displayed to the user.

## 💡 Future Improvements
- **Support for multiple course providers (Udemy, edX, etc.)**
- **User authentication & profile saving**
- **Improved ranking with hybrid weighting techniques**
- **Integration with APIs for real-time course updates**

---

