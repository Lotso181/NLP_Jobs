import requests
import json

def chat_with_model(prompt, history=[]):
    # Use your server's public HTTPS endpoint
    url = "https://u276259-b5b1-12297c17.westc.gpuhub.com:8443/"
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps({'prompt': prompt, 'history': history})

    try:
        response = requests.post(url, headers=headers, data=payload, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Received response with status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    prompt = "介绍一下cahtglm2"
    model_response = chat_with_model(prompt)
    if model_response:
        print("Model response:", model_response.get('response'))
    else:
        print("Failed to get a response from the model.")