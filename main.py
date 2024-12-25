from flask import Flask, request, jsonify
from app.detect_spam import predict_spam
app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        # check json format
        if not data:
            return jsonify({
                'status': 'error',
                'message': 'Request payload must be JSON'
            }), 400
        contact_message = data.get('contact_message')
        # check invalid message
        if not contact_message or not isinstance(contact_message, str):
            return jsonify({
                'status': 'error',
                'message': 'Invalid or missing contact_message'
            }), 400
        else:
            result = predict_spam(contact_message)
            return jsonify({
                'status': 'success',
                'spam': str(result)
            }), 200

    except Exception as e:
        app.logger.error(f"Error: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'}), 500
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
