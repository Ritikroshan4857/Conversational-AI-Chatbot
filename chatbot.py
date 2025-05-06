import os
import openai
from flask import Flask, request, jsonify

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# Initialize conversation history
conversation_history = [
    {"role": "system", "content": "You are a helpful customer care assistant."}
]

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    conversation_history.append({"role": "user", "content": user_message})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=conversation_history,
            temperature=0.3  # Lower for more factual, higher for more creative
        )
        assistant_message = response.choices[0].message['content']
        conversation_history.append({"role": "assistant", "content": assistant_message})
        return jsonify({"response": assistant_message})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
