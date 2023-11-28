from api.module import *


class WebScrapper:
    def __init__(self, url: str = None):
        self._url = url
        self.data = []

    @property
    def results(self):
        response = self.response()
        data = self.getData(soup=response)
        return data

    def getData(self, soup) -> list:
        self.data.clear()
        venutama = soup.find("div", attrs={"id": "venkonten"}).find(
            "div", attrs={"class": "venutama"}
        )
        konten = venutama.find("div", attrs={"class": "venz"}).find("ul")

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
                    "judul": title,
                    "cover": cover["src"],
                    "data": re.findall(
                        "https\:\/\/otakudesu\.cam\/anime\/(.*?)\/", str(thumb["href"])
                    )[0],
                    "episode": episode[0],
                    "release": release,
                    "release_on_every": release_on[0],
                }
            )

        if self.route != False:
            pagination = venutama.find("div", attrs={"class": "pagination"})
            next = pagination.find("a", attrs={"class": "next page-numbers"})
            return {
                "data_anime": self.data,
                "next": re.findall("\/(page\/\d+)\/", str(next["href"]))[0].replace(
                    "/", "-"
                )
                if next
                else "None",
            }

        return self.data


class Home(WebScrapper):
    def __init__(self, url: str = None, proxy: dict = None, route=False) -> None:
        super().__init__(url=url)
        self.proxies = proxy
        self.route = route

    def response(self) -> str:
        with requests.Session() as session:
            response = session.get(self._url)
            soup = BeautifulSoup(response.text, "html.parser")
        return soup
