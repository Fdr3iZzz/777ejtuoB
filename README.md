# What does the code do?
- download all RSS feeds from the wordpress site
- filter out all links found in the contents of every RSS item and store them in a file
- filter out important link types/ domains e.g. google drive, mediafire etc. and delete duplicates to store them into their respective files
- filtering was done with regex
- filepaths are static at times (quick and dirty)

# How can I use that?
- if you want to download all of the comics, they are probably hosted on google drive, mediafire and boutjefedankt
- download or generate the .txt link files for them
- download the desired files using their link

# I want to download all links from a file?
- use a download manager like Jdownloader2 to bulk download the files
