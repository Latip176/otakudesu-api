from api.module import *


class View:
    def __init__(self, url: str = None, proxies: dict = None) -> None:
        self._url = url
        self._data = {}
        self.proxies = proxies

    def __getData(self, soup):
        venkonten = soup.find("div", attrs={"class": "wowmaskot"}).find(
            "div", attrs={"id": "venkonten"}
        )
        venutama = venkonten.find("div", attrs={"class": "venutama"})

        title = venutama.find("h1", attrs={"class": "posttl"}).string
        prev = venutama.find("div", attrs={"class": "flir"}).findAll("a")
        prev, next = prev[0], prev[1]
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
            {"judul_episode": title, "next": next, "prev": prev, "stream": stream}
        )

        return self._data

    @property
    def results(self):
        soup = self._View__response()
        return self._View__getData(soup=soup)

    def __response(self):
        with requests.Session() as session:
            response = session.get(self._url)
            soup = BeautifulSoup(response.text, "html.parser")
        return soup
