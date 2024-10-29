import requests
import os

# Define the base URL and directory to store files
base_url = "https://britishcomics.wordpress.com/feed/?paged="
save_dir = "resources"
os.makedirs(save_dir, exist_ok=True)
page = 0

while True:
    page += 1
    url = f"{base_url}{page}"
    response = requests.get(url)

    if response.status_code == 200:
        content = response.content
        file_path = os.path.join(save_dir, f"feed_page_{page}.xml")

        with open(file_path, "wb") as file:
            file.write(content)

        print(f"Saved feed page {page} to {file_path}")
    else:
        print(f"Failed to retrieve page {page}: Status code {response.status_code}")
        break

print("RSS feed pages retrieval complete.")
