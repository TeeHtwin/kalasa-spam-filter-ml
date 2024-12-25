# Spam Message Detection API

This is a flask-based API for detecting whether a given message is spam or not. The model uses a Support Vector Machine (SVM) classifier trained on preprocessed message data, with text vectorization handled by a `TfidfVectorizer`.

## Features

- Preprocesses input by removing punctuation, stopwords, and stemming the text and vectorize the message.
- Utilizes a SVM model for classification.

## Requirements

- Python 3.9 or higher
- flask
- joblib
- nltk
- sklearn

<details>
<summary> Installation </summary>

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/----/spam-detection-api.git
2. Install required packages
   ```bash
   pip install -r requirements.txt
3. Start the app
   ```bash
   python main.py
</details>

<details>
<summary> API usage </summary>

- **Request**: 

    Endpoint is '/predict' and the method must be post. 

    For example:
    ```bash
    http://192.168.1.7:8000/predict
  ```
   The request must include a JSON object (Content-type: application/json) with a key called contact_message.
   Example
   ```json
  {
  "contact_message": "Congratulations! You've won a $1000 gift card. Click here to claim your prize."
  }

- **Response**  
   The response will indicate whether the message is classified as spam or not.  
   - Example response for a spam message:
  ```json
       {
           "spam": "1",
           "status": "success"
       }  
  ```
    - Example response for a non-spam message:
       ```json
       {
           "spam": "0",
           "status": "success"
       }  



