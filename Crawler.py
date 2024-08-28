from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException

class Website:
    ```

        Tags
    ```
    def __init__(self, url, bodyTag, titleTag, contentTag):
        self.url = url
        self.bodyTag = bodyTag
        self.titleTag = titleTag
        self.contentTag = contentTag

class Content:
    ```

        Content
    ```
    def __init__(self, url, title, content):
        self.url = url
        self.title = title
        self.content = content

    def print(self):
        print("Site's url: {}".formant(self.url))
        print("Page's title: {}".format(self.title))
        print("Content:\n{}".format(self.content))

class Crawler:
    def __init__(self):
        pass
