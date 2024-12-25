import string
import joblib
from nltk.stem import PorterStemmer
import os
stopwords_set = {
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your",
    "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she",
    "her", "hers", "herself", "it", "its", "itself", "they", "them", "their",
    "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
    "these", "those", "am", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an",
    "the", "and", "but", "if", "or", "because", "as", "until", "while", "of",
    "at", "by", "for", "with", "about", "against", "between", "into", "through",
    "during", "before", "after", "above", "below", "to", "from", "up", "down",
    "in", "out", "on", "off", "over", "under", "again", "further", "then",
    "once", "here", "there", "when", "where", "why", "how", "all", "any",
    "both", "each", "few", "more", "most", "other", "some", "such", "no",
    "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s",
    "t", "can", "will", "just", "don", "should", "now"
}
stemmer = PorterStemmer()
model = joblib.load(os.path.join(os.getcwd(), "app/models", "svm_model.pkl"))
vectorizer = joblib.load(os.path.join(os.getcwd(), "app/vectorizers", "vectorizer.pkl"))
def preprocess_message(message):
    text = message.lower().translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    stemmed_words = [stemmer.stem(word) for word in words if word not in stopwords_set]
    return " ".join(stemmed_words)
def predict_spam(data):
    preprocessed_data=preprocess_message(data)
    vectorized_data=vectorizer.transform([preprocessed_data]).toarray()
    prediction = model.predict(vectorized_data)[0]
    return prediction