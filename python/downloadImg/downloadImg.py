import requests
from bs4 import BeautifulSoup
import os
import time

def download_image(image_url, save_path):
    response = None
    try:
        response = requests.get(image_url)
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
        time.sleep(60)
        download_image(image_url, save_path)
    if response.status_code == 200:
        content_disposition = response.headers.get('Content-Disposition')
        if content_disposition:
            filename = content_disposition.split('filename=')[-1].strip('"')
        else:
            # 如果没有文件名，则使用URL中的文件名
            filename = os.path.basename(image_url)
        file_path = os.path.join(save_path, filename)
        if os.path.exists(file_path):
                print(f"File already exists: {file_path}")
                return
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded: {save_path}")
    else:
        print(f"Failed to retrieve image from {image_url}")

def get_image_and_next_page_urls(page_url, img_selector, next_page_selector):
    response = None
    try:
        response = requests.get(page_url)
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
        time.sleep(60)
        get_image_and_next_page_urls(page_url, img_selector, next_page_selector)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tag = soup.select_one(img_selector)
        newpage_element = soup.select_one(next_page_selector)

        next_page_tag = None
        if newpage_element:
            children = newpage_element.find_all(recursive=False)
            if len(children) >= 3:
                next_page_tag = children[2]


        image_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else None
        next_page_url = next_page_tag['href'] if next_page_tag and 'href' in next_page_tag.attrs else None
        
        return {
            'image_url': image_url,
            'next_page_url': next_page_url
        }
    return None

# Example usage

img_selector = ".photo"  # Change this to the appropriate CSS selector for the image
save_path = "./save/"
next_page_selector = ".newpage"

def getImage(page_url, img_selector, next_page_selector,save_path):
    urlObj = get_image_and_next_page_urls(page_url, img_selector, next_page_selector)
    if urlObj['image_url']:
        # If the image URL is relative, make it absolute
        if not urlObj['image_url'].startswith('https://') and not urlObj['image_url'].startswith('http://'):
            urlObj['image_url'] = "https:"+ urlObj['image_url']
        download_image(urlObj['image_url'], save_path)
        if urlObj['next_page_url']:
           getImage(page_prefix + urlObj['next_page_url'], img_selector, next_page_selector,save_path)
        else:
            print("No more images")
    else:
        print("Image not found")


page_prefix = "https://"
page_outfix = ""

getImage(page_prefix+ page_outfix, img_selector, next_page_selector,save_path)