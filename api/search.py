from api.module import *


class WebScrapper:
    def __init__(self, url: str = None) -> None:
        self._url = url
        self.data = []

    @property
    def results(self) -> dict:
        soup = self._Search__response()
        data = self.getData(soup=soup)
        return {"data": self.data}

    def getData(self, soup) -> list:
        venkonten = soup.find("div", attrs={"id": "venkonten"})
        page = venkonten.find("div", attrs={"class": "page"})
        for data in page.find("ul").findAll("li"):
            data_private = {}
            cover = data.find("img")["src"]
            title = data.find("h2")
            url = re.findall(
                "https\:\/\/otakudesu\.cam\/anime\/(.*?)\/",
                str(title.find("a")["href"]),
            )[0]
            title = title.string.replace("\u2013", "-")
            for dat in data.findAll("div", attrs={"class": "set"}):
                key, value = (
                    re.findall("\<b\>(.*?)\<\/b\>", str(dat))[0]
                    .lower()
                    .replace(" ", "_"),
                    re.findall("\:\s(.*?)\<\/div\>", str(dat))[0],
                )
                if key == "genres":
                    value = ", ".join([x.string for x in dat.findAll("a")])
                data_private.update({key: value})
            data_private.update({"cover": cover, "data": url, "judul": title})
            self.data.append(data_private)

        return self.data


class Search(WebScrapper):
    def __init__(self, url: str = None, proxies: dict = None) -> None:
        super().__init__(url=url)
        self.proxies = proxies

    def __response(self) -> str:
        with requests.Session() as session:
            response = session.get(self._url)
            soup = BeautifulSoup(response.text, "html.parser")
        return soup
