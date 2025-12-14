from flask import Flask, request, jsonify
from flask_cors import CORS
import anthropic

app = Flask(__name__)
CORS(app)  # Allow frontend to access this API

ANTHROPIC_API_KEY = ""
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    
    response = client.messages.create(
        model="claude-3-opus-20240229",  # Or another model like "claude-2.1"
        max_tokens=1024,
        messages=[{"role": "user", "content": user_message}]
    )
    
    return jsonify({"reply": response.content[0].text})

if __name__ == "__main__":

    app.run(port=5000)
