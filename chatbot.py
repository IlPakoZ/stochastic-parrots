
from flask import Flask, request, jsonify, send_from_directory
import argparse
import project_rant as pr
import random

app = Flask(__name__)

# Define a function to generate responses based on user input
def generate_response(initial_context):
    initial_context = pr.get_initial_context(possible_starts)
    return pr.generate_text(freq_table, initial_context)

# Route to handle chat requests
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    response = generate_response(user_message)
    return jsonify({"response": response})

# Route to serve the index.html file
@app.route('/')
def serve_html():
    return send_from_directory('.', 'index.html')

def main():
    parser = argparse.ArgumentParser(description="Run the Flask chatbot server.")
    parser.add_argument('--port', type=int, default=5000, help='Port to run the Flask server on.')
    args = parser.parse_args()
    
    app.run(port=args.port, debug=True)

if __name__ == "__main__":
    freq_table = pr.load_dataset()
    pr.preprocessing(freq_table)
    possible_starts = pr.get_possible_starts(freq_table)
    
    random.seed(1933)

    main()

