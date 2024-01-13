from .module import *


class Genres(cloudscraper.Session):
    def __init__(self, url) -> None:
        super().__init__()
        self._url = url
        self.__data = []

    def __response(self, url: str = None) -> BeautifulSoup:
        response = self.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    def _genres(self) -> dict:
        soup = self._Genres__response(self._url)
        genres = [
            {"data": k, "name": v}
            for k, v in re.findall(
                '<a\sdata\-wpel\-link\="internal"\shref\="(.*?)"\stitle\=".*?"\>(.*?)\<\/a\>',
                str(soup.find("ul", attrs={"class": "genres"})),
            )
        ]

        return {"genres": genres}

    def getData(self, genre: str = None) -> list:
        soup = self._Genres__response("https://otakudesu.media/genres/" + genre)
        venser = soup.find("div", attrs={"class": "venser"})

        for data in venser.findAll("div", attrs={"class": "col-anime"}):
            head = data.find("div", attrs={"class": "col-anime-title"}).find("a")
            url, title = (head["href"], head.string)
            studio, total_epsd, rating, genre, cover = [
                data.find("div", attrs={"class": "col-anime-studio"}).string,
                data.find("div", attrs={"class": "col-anime-eps"}).string,
                data.find("div", attrs={"class": "col-anime-rating"}).string,
                [
                    _.string
                    for _ in data.find(
                        "div", attrs={"class": "col-anime-genre"}
                    ).findAll("a")
                ],
                data.find("div", attrs={"class": "col-anime-cover"}).find("img")["src"],
            ]
            self._Genres__data.append(
                {
                    "url": url,
                    "title": title,
                    "studio": studio,
                    "total_episode": total_epsd,
                    "rating": rating,
                    "genre": genre,
                    "cover": cover,
                }
            )

        return self._Genres__data
