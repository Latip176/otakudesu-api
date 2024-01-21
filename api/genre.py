from .module import *


class Genres:
    def __init__(self, url) -> None:
        super().__init__()
        self._url = url
        self.__data = []

    def __response(self, url: str = None) -> BeautifulSoup:
        scrap = cloudscraper.create_scraper()
        response = scrap.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    def get_genres(self) -> list:
        soup = self._Genres__response(self._url)
        genres = [
            {"data": re.findall("\/genres\/(.*?)\/", str(k))[0], "name": v}
            for k, v in re.findall(
                '<a\sdata\-wpel\-link\="internal"\shref\="(.*?)"\stitle\=".*?"\>(.*?)\<\/a\>',
                str(soup.find("ul", attrs={"class": "genres"})),
            )
        ]

        return genres

    def get_data(self, genre: str = None) -> dict:
        soup = self._Genres__response("https://otakudesu.media/genres/" + genre)
        venser = soup.find("div", attrs={"class": "venser"})

        for data in venser.findAll("div", attrs={"class": "col-anime"}):
            head = data.find("div", attrs={"class": "col-anime-title"}).find("a")
            url, title = (
                re.findall(
                    "https\:\/\/otakudesu\..*?\/anime\/(.*?)\/", str(head["href"])
                )[0],
                head.string,
            )
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
                    "data": url,
                    "judul": title,
                    "studio": studio,
                    "total_episode": total_epsd,
                    "rating": rating,
                    "genre": genre,
                    "cover": cover,
                }
            )

        wowmaskot = soup.find("div", attrs={"class": "wowmaskot"}).find(
            "div", attrs={"class": "venser"}
        )
        pagenation = wowmaskot.find("div", attrs={"class": "pagination"})

        next, prev = pagenation.find(
            "a", attrs={"class": "next page-numbers"}
        ), pagenation.find("a", attrs={"class": "prev page-numbers"})

        return {
            "data": self._Genres__data,
            "next": re.findall("\/page\/(\d+)\/", next["href"])[0]
            if next != None
            else "None",
            "prev": re.findall("\/page\/(\d+)\/", prev["href"])[0]
            if prev != None
            else "None",
        }
