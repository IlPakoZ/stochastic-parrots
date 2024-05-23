from flask import Flask, request, jsonify, send_from_directory
import argparse
import project_rant as pr
import random

app = Flask(__name__)



# Define a function to generate responses based on user input
def generate_response(initial_context):
    #initial_context = pr.get_initial_context(possible_starts)
    tokens = pr.generate(model, initial_context, end_token)
    generated_tokens = list(tokens)[len(initial_context):]
    generated_text = model.tokenizer.decode(generated_tokens)
    return generated_text

# Route to handle chat requests
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    new_context = model.tokenizer(user_message)
    app.config["context"] += new_context + model.tokenizer("\n")
    print("Context:", model.tokenizer.decode(app.config["context"]))
    #print(app.config["context"])
    #print(app.config["context"])

    response = generate_response(app.config["context"])
    #print(response)
    app.config["context"] += model.tokenizer(response) + model.tokenizer("\n")

    print("Context:", model.tokenizer.decode(app.config["context"]))
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
    context_length = 4
    app.config["context"] = []
    model = pr.get_model(context_length)
    end_token = model.tokenizer("\2")[0]
    pr.train_model(model)
    #possible_starts = pr.get_possible_starts(model.predictor.follower_table, end_token)

    random.seed(1933)

    main()
