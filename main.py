import openai
import typer
import pytesseract
from PIL import Image
import os
from pprint import pprint
import json
from ai import get_completion

app = typer.Typer()

ctx = {"api_key": None}

# Path to the configuration file
CONFIG_FILE_PATH = "config.json"


@app.callback()
def common_options():
    # If the API key is provided, save it to the context object
    try:
        with open(CONFIG_FILE_PATH, 'r') as json_file:
            data = json.load(json_file)
            api_key = data['api_key']
            ctx["api_key"]  = api_key

        if api_key is None:
            typer.echo("API Key is not set. Use 'set-api-key' command to set it.", fg=typer.colors.GREY)
            return
        
    except:
        typer.secho(f"Config_File not found at {CONFIG_FILE_PATH}", fg=typer.colors.RED)

    

@app.command()
def set_api_key(api_key: str = typer.Argument(..., help="API Key to set for future use")):
    ctx['api_key'] = api_key
    try:
        with open(CONFIG_FILE_PATH, 'w') as json_file:
            json.dump(ctx, json_file)

    except:
        typer.secho(f"Warning: Config_File not found at {CONFIG_FILE_PATH}", fg=typer.colors.RED)


    typer.secho(f"Setting API Key to: {api_key}", fg=typer.colors.GREEN)
    typer.secho("API Key saved.", fg=typer.colors.GREEN)


@app.command()
def read_page(file_path: str):
    api_key = ctx["api_key"]

    if api_key is None:
        typer.echo("API Key is not set. Use 'set-api-key' command to set it.")
        return
    
    text = pytesseract.image_to_string(Image.open(file_path))
    text = f"""Text: ```{text}``` """
    question = typer.prompt('What do you need to do?')
    openai.api_key = api_key
    response = get_completion(text, question)
    typer.echo(response)




def get_completion(text, prompt, model="gpt-3.5-turbo", temperature=0.2): 
    with open("preprompts/assistant_msg", "r") as file:
        assistant_msg = file.read()
    
    messages = [{"role": "assistant", "content": assistant_msg},
                {"role": "user", "content": text},
                {"role": "user", "content": prompt}]
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
    )
    return response.choices[0].message["content"]


if __name__ == "__main__":
    app()