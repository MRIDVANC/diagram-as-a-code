import requests
from bs4 import BeautifulSoup
import os

def get_image_urls(repo_url, directory):
    """
    Bir GitHub deposu altındaki belirli bir dizindeki tüm resimlerin URL'lerini döndürür.

    Args:
        repo_url: GitHub deposunun URL'si.
        directory: Resimlerin bulunduğu dizin.

    Returns:
        Resimlerin URL'lerinin bir listesi.
    """
    page_url = f"{repo_url}/tree/master/{directory}"
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, "html.parser")

    images = []
    for img in soup.find_all("img"):
        img_url = img.get("src")
        if img_url.startswith("/"):
            img_url = f"https://github.com{img_url}"
        images.append(img_url)

    return images

def main():
    repo_url = "https://github.com/MRIDVANC/diagram-as-a-code"
    directory = "custom_icons"

    images = get_image_urls(repo_url, directory)

    # Dosya adı = resim adresi olacak şekilde bir constant oluşturuyoruz.

    image_urls = {}
    for image in images:
        filename = os.path.basename(image)
        image_urls[filename] = image

    print(image_urls)

if __name__ == "__main__":
    main()