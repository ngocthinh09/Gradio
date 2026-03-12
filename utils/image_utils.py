import requests
from PIL import Image
from io import BytesIO

def load_image_from_url(url):
    try:
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        return image
    except:
        return Image.new('RGB', (500, 300), color='lightblue')
    
