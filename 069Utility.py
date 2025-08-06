# In pythonn utilities are programs that can be run from cli or terminal .
# They are part of many workflows .
# WE can create our own utilities by using built-in argparese module

import argparse
import requests

def DownloadFile(url, local_filename):
    r = requests.get(url)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=512 * 1024): 
            if chunk:
                f.write(chunk)

parser = argparse.ArgumentParser()
parser.add_argument('url', help='url of file to download')
parser.add_argument('output', help='by which name do you want to download file')

args = parser.parse_args()

print(args.url)
print(args.output)

DownloadFile(args.url, args.output)
