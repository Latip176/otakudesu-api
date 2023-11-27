import re, requests
from bs4 import BeautifulSoup


class WebScrapper:
    def __init__(self, url: str = None):
        self._url = url
        self.data = []

    @property
    def results(self):
        response = self.response()
        data = self.getData(soup=response)
        return data

    def getData(self, soup) -> str:
        self.data.clear()
        konten = (
            soup.find("div", attrs={"id": "venkonten"})
            .find("div", attrs={"class": "venz"})
            .find("ul")
        )
        for data in konten.findAll("li"):
            detpost = data.find("div", attrs={"class": "detpost"})
            thumb = detpost.find("div", attrs={"class": "thumb"}).find("a", href=True)
            thumz = thumb.find("div", attrs={"class": "thumbz"})
            title = thumz.find("h2").string
            cover = thumz.find("img")
            episode = re.findall(
                " (Episode \d+)", str(detpost.find("div", attrs={"class": "epz"}))
            )
            release_on = re.findall(
                "\/i>\s+(.*?)<\/div>",
                str(detpost.find("div", attrs={"class": "epztipe"})),
            )
            release = detpost.find("div", attrs={"class": "newnime"}).string
            self.data.append(
                {
                    "title": title,
                    "cover": cover["src"],
                    "url": thumb["href"],
                    "episode": episode[0],
                    "release": release,
                    "release_on_every": release_on[0],
                }
            )

        return self.data


class Home(WebScrapper):
    def __init__(self, url: str = None, proxy: dict = None) -> None:
        super().__init__(url=url)
        self.proxies = proxy

    def response(self) -> str:
        with requests.Session() as session:
            response = session.get(self._url)
            soup = BeautifulSoup(response.text, "html.parser")
        return soup
