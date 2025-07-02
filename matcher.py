import argparse
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download stopwords if not already
nltk.download('stopwords')
from nltk.corpus import stopwords

def load_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"❌ Error reading {filepath}: {e}")
        return ""

def preprocess(text):
    text = text.lower()
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered = [word for word in words if word not in stop_words]
    return " ".join(filtered)

def get_match_score(resume_text, jd_text):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text, jd_text])
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(score * 100, 2)

def main():
    parser = argparse.ArgumentParser(description="Resume vs JD Keyword Matcher")
    parser.add_argument('--resume', type=str, required=True, help="Path to resume text file")
    parser.add_argument('--jd', type=str, required=True, help="Path to job description text file")
    args = parser.parse_args()

    resume_raw = load_file(args.resume)
    jd_raw = load_file(args.jd)

    resume = preprocess(resume_raw)
    jd = preprocess(jd_raw)

    score = get_match_score(resume, jd)

    print("\n🎯 Resume Matching Report 🎯")
    print(f"✅ Match Score: {score}%")

    resume_words = set(resume.split())
    jd_words = set(jd.split())

    matched = resume_words.intersection(jd_words)
    missing = jd_words.difference(resume_words)

    print(f"\n✅ Matched Keywords ({len(matched)}): {', '.join(sorted(matched))}")
    print(f"❌ Missing Keywords ({len(missing)}): {', '.join(sorted(missing))}\n")

if __name__ == "__main__":
    main()
