import openai

# Set up the OpenAI API client
openai.api_key = ""  # Replace 'your-api-key' with your actual API key

def generate_response(prompt, model="text-davinci-002", n=1, max_tokens=150, temperature=0.5):
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        n=n,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    response = completions.choices[0].text.strip()
    return response

def chatbot(prompt):
    user_prompt = f"User: {prompt}\nAI:"
    response = generate_response(user_prompt)
    return response

if __name__ == "__main__":
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = chatbot(user_input)
        print(f"AI: {response}")
