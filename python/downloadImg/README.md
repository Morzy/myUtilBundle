# Image Downloader Script

This script is designed to download images from a webpage and navigate through pages to download additional images. It uses `requests` for HTTP requests and `BeautifulSoup` for HTML parsing.

## Features
- Downloads images from a specified webpage.
- Automatically navigates to the next page to download more images.
- Handles relative and absolute image URLs.
- Skips downloading if the image already exists.

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library

Install the required libraries using:
```bash
pip install requests beautifulsoup4
```

## Usage
1. Update the following variables in the script:
   - `img_selector`: CSS selector for the image tag.
   - `next_page_selector`: CSS selector for the next page navigation element.
   - `save_path`: Directory where images will be saved.
   - `page_prefix`: Base URL for the website.
   - `page_outfix`: Starting page URL suffix.

2. Run the script:
```bash
python downloadImg.py
```

## Example
If the webpage contains an image with the CSS class `.photo` and a navigation element with the class `.newpage`, set:
```python
img_selector = ".photo"
next_page_selector = ".newpage"
save_path = "./save/"
page_prefix = "https://example.com"
page_outfix = "/start-page"
```

The script will download all images starting from `https://example.com/start-page` and save them in the `./save/` directory.

## Notes
- Ensure the `save_path` directory exists before running the script.
- The script retries downloading in case of network errors or timeouts.