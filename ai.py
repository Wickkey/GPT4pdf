import openai

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0): 
    messages = [{"role": "system", "content": ""}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
    )
    return response.choices[0].message["content"]