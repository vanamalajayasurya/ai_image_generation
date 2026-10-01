import requests
from urllib.parse import quote
prompt = "A beautiful landscape with mountains and a river"
# URL encode the prompt
encoded_prompt = quote(prompt)
# Construct the URL for the image generation API
url = (f"https://image.pollinations.ai/prompt/"
       f"{encoded_prompt}"
       f"model=flux"
       )
print("generating image...")
response = requests.get(url,timeout=100)
if response.status_code == 200:
    with open("generated_image.png", "wb") as file:
        file.write(response.content)
print("IMAGE GENERATED SUCCESSFULLY")
print("SAVE IMAGE AS generated_image.png")
print(response.text)

