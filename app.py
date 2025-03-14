from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load BERT model and data
model = SentenceTransformer('all-MiniLM-L6-v2')
course_df = pd.read_csv("coursera_data.csv")

def get_recommendations(education, goals, top_n=5):
    # Create user profile embedding
    user_text = f"{education}. {goals}."
    user_embedding = model.encode(user_text)
    
    # Generate course embeddings if not already present
    if 'embedding' not in course_df.columns:
        course_df['embedding'] = course_df['course_description'].apply(
            lambda x: model.encode(x) if pd.notna(x) else None
        )
    
    # Calculate similarities
    course_embeddings = np.stack(course_df['embedding'].values)
    similarities = cosine_similarity([user_embedding], course_embeddings)[0]
    
    # Get top recommendations
    top_indices = similarities.argsort()[-top_n:][::-1]
    recommendations = course_df.iloc[top_indices][['course_title', 'course_url', 'course_difficulty']]
    
    return recommendations.to_dict('records')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    education = data.get('education')
    goals = data.get('goals')
    
    recommendations = get_recommendations(education, goals)
    return jsonify(recommendations)

if __name__ != '__main__':
    gunicorn_app = app  # Required for Gunicorn
gunicorn_app.run()  # Required for Gunicorn