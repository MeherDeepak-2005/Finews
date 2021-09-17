import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)
info = []



class News:
    def __init__(self):
        self.topics = [
    'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSkwyMHZNREp3WW0xM0VnVmxiaTFIUWlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen',
    'https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNREpmTjNRU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen',
    'https://news.google.com/publications/CAAqBwgKMIzDmwsw0M2zAw?hl=en-IN&gl=IN&ceid=IN%3Aen']
        self.headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0",
    "Accept-Language": "en-US",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html"
}
    def get_news(self):
        for link in self.topics:
            web_page = requests.get(link)
            bs4 = BeautifulSoup(web_page.text,'lxml')
            headers = bs4.find_all('h3', class_='ipQwMb ekueJc RD0gLb')
            for header in headers:
                links = header.find('a')
                info.append([links['href'],links.text])


@app.route('/')
def home():
    news = News()
    news.get_news()
    return render_template('index.html',data=info)

if __name__ == "__main__":
    app.run(debug=True)


