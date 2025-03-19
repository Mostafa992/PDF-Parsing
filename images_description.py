import base64
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.environ['OPENAI_API_KEY']


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


client = OpenAI(api_key=openai_api_key)

def get_image_description(image_path):
    base64_image = encode_image(image_path)
    response = client.chat.completions.create(
    model="gpt-4o-mini-2024-07-18",
    messages=[
        {"role": "system", "content": """You are an AI assistant that provides accurate and concise image descriptions.
         Prioritize relevant details, if the image lacks meaningful content (e.g., a logo, abstract patterns, or unrelated images), provide only a brief response."""},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Analyze the given image and describe its key elements, objects, text, and contextual information, emphasizing relevance to the specified topic. If the image has little meaningful content, provide a brief response without unnecessary details."},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
            ],
        }
    ],
    max_tokens=300,
)

    return response.choices[0].message.content

if __name__ == "__main__":
    image_path = "/Users/mostafaelgharib/Desktop/prep_sprint/project_1/images_out/page_1_image_1.png"
    image_description = get_image_description(image_path)
    print(image_description)
