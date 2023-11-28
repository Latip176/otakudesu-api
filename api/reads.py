from api.module import *


class WebScrapper:
    def __init__(self, url: str = None) -> None:
        self._url = url
        self.data = {}

    @property
    def results(self):
        response = self.response()
        data = self.getData(soup=response)
        return data

    def getDataEpisode(self, soup) -> list:
        data_private = []
        venkonten = soup.find("div", attrs={"id": "venkonten"}).findAll(
            "div", attrs={"class": "episodelist"}
        )[1]
        for data in venkonten.find("ul").findAll("li"):
            span = data.find("span").find("a")
            title_episode = span.string
            href_episode = span["href"]
            release_episode = data.find("span", attrs={"class": "zeebr"}).string

            data_private.append(
                {
                    "judul_episode": title_episode,
                    "data": re.findall(
                        "https\:\/\/otakudesu\.cam\/episode\/(.*?)\/", str(href_episode)
                    )[0],
                    "release": release_episode,
                }
            )
        return data_private

    def getData(self, soup):
        self.data.clear()
        venkonten = soup.find("div", attrs={"id": "venkonten"}).find(
            "div", attrs={"class": "fotoanime"}
        )
        info = venkonten.find("div", attrs={"class": "infozin"})

        info_anime = info.find("div", attrs={"class": "infozingle"})
        sinopsis = re.findall(
            "\>(.*?)\<\/div\>", str(venkonten.find("div", attrs={"class": "sinopc"}))
        )[0]
        for data in info_anime.findAll("p"):
            dat = data.find("span")
            key, value = (
                re.findall("\<b\>(.*?)\<\/b\>", str(dat))[0].lower().replace(" ", "_"),
                re.findall("\:\s(.*?)\<\/span\>", str(dat))[0],
            )
            if key == "genre":
                value = ", ".join(re.findall(">(.*?)<\/a>", str(value)))
            self.data.update({key: value})
        self.data.update(
            {
                "cover": venkonten.find("img")["src"],
                "sinopsis": str(sinopsis),
                "data_episode": self.getDataEpisode(soup=soup),
            }
        )

        return self.data


class Reads(WebScrapper):
    def __init__(self, url: str = None, proxies: dict = None) -> None:
        super().__init__(url=url)
        self.proxies = proxies

    def response(self) -> str:
        with requests.Session() as session:
            response = session.get(self._url)
            soup = BeautifulSoup(response.text, "html.parser")
        return soup
