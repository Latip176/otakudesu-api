from api.module import *


class View:
    def __init__(self, url: str = None, proxies: dict = None) -> None:
        self._url = url
        self._data = {}
        self.proxies = proxies

    # get mp4 from strem (not working, reason auth)
    def getMP4(self, link: str) -> str:
        with requests.Session() as session:
            response = session.get(link).text
        get_stream_mp4 = re.findall(r"sources:\s\[\{\'file\':\'(.*?)\'", str(response))
        get_stream_mp4 = get_stream_mp4[0] if len(get_stream_mp4) >= 1 else "None"
        return get_stream_mp4

    # get data from anime
    def __getData(self, soup) -> dict:
        venkonten = soup.find("div", attrs={"class": "wowmaskot"}).find(
            "div", attrs={"id": "venkonten"}
        )
        venutama = venkonten.find("div", attrs={"class": "venutama"})

        title = venutama.find("h1", attrs={"class": "posttl"}).string
        prev = venutama.find("div", attrs={"class": "flir"}).findAll("a")
        prev, next = prev[0], prev[-1]
        prev = (
            "None"
            if str(prev.string) == "See All Episodes"
            else re.findall(
                "https\:\/\/otakudesu\.cam\/episode\/(.*?)\/", prev["href"]
            )[0]
        )
        next = (
            "None"
            if str(next.string) == "See All Episodes"
            else re.findall(
                "https\:\/\/otakudesu\.cam\/episode\/(.*?)\/", next["href"]
            )[0]
        )

        self._data.update(
            {
                "judul_episode": title,
                "next": next,
                "prev": prev,
                "stream": venutama.find("div", attrs={"id": "lightsVideo"}).find(
                    "iframe"
                )["src"],
            }
        )

        return self._data

    @property
    def results(self) -> dict:
        soup = self._View__response()
        return self._View__getData(soup=soup)

    def __response(self) -> str:
        scrap = cloudscraper.create_scraper()
        response = scrap.get(self._url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup
