import os
import openai
import json

def main(req):
    code_diff = req.get_json().get("diff")

    prompt = open("prompt_template.txt").read().replace("{{DIFF}}", code_diff)

    openai.api_key = os.getenv("AZURE_OPENAI_KEY")

    response = openai.ChatCompletion.create(
        engine="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un revisor de código experto en buenas prácticas de desarrollo y DevOps."},
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "status": 200,
        "body": response["choices"][0]["message"]["content"]
    }
