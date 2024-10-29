import os
import re

link_file_path = "resources/extracted_links_v2.txt"
links_folder_path = "C:/Users/Franz3/PycharmProjects/Boutje777/src/links/"


def filter_wordpress_content(link):
    if re.search(r'britishcomics.wordpress.com/wp-content', link, re.IGNORECASE):
        with open("links/wordpress_download_links.txt", "a") as f:
            f.write(link + "\n")
            return True
    else:
        return filter_wordpress_page(link)


def filter_wordpress_page(link):
    if re.search(r'britishcomics.wordpress.com', link, re.IGNORECASE):
        with open("links/wordpress_page_links.txt", "a") as f:
            f.write(link + "\n")
            return True
    else:
        return filter_wordpress_page_redirect(link)


def filter_wordpress_page_redirect(link):
    if re.search(r'wp.me', link, re.IGNORECASE):
        with open("links/wordpress_page_redirect_links.txt", "a") as f:
            f.write(link + "\n")
            return True
    else:
        return False


def filter_google_drive(link):
    if re.search(r'drive.google.com', link, re.IGNORECASE):
        with open("links/drive_google_links.txt", "a") as f:
            f.write(link + "\n")
            return True
    else:
        return False


def filter_boutjefedankt(link):
    if re.search(r'boutjefedankt.nl', link, re.IGNORECASE):
        with open("links/boutjefedankt_links.txt", "a") as f:
            f.write(link + "\n")
            return True
    else:
        return False


def filter_media_fire(link):
    if re.search(r'mediafire.com', link, re.IGNORECASE):
        with open("links/media_fire_links.txt", "a") as f:
            f.write(link + "\n")
            return True
    else:
        return False


def filter_youtube(link):
    if re.search(r'youtu.be', link, re.IGNORECASE):
        with open("links/youtube_links.txt", "a") as f:
            f.write(link + "\n")
            return True
    else:
        return False


def filter_dmca(link):
    if re.search(r'wordpress.com/support/copyright-and-the-dmca/', link, re.IGNORECASE):
        return True
    else:
        return False


# filter links by specific domains
def filter_links():
    clear_folder()
    with open(link_file_path, 'r') as file:
        while line := file.readline():
            line = line.strip()
            if not (filter_wordpress_content(line) or filter_google_drive(line) or filter_boutjefedankt(line) or
                    filter_media_fire(line) or filter_youtube(line) or filter_dmca(line)):
                with open("links/leftover_links.txt", "a") as f:
                    f.write(line + "\n")
    delete_duplicates()


# remove duplicate links in file
def delete_duplicates():
    dir_list = os.listdir(links_folder_path)
    for file_path in dir_list:

        full_file_path = links_folder_path + file_path
        unique_lines = set()

        with open(full_file_path, 'r') as file:
            for line in file:
                unique_lines.add(line)

        with open(full_file_path, 'w') as file:
            for line in unique_lines:
                file.write(line)


# delete all files in links folder for clean start
def clear_folder():
    dir_list = os.listdir(links_folder_path)
    for file_path in dir_list:
        os.remove(links_folder_path + file_path)


filter_links()
