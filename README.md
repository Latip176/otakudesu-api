# otakudesu-api
Rest API for get Data Anime from otakudesu
# get index
```
https://latipharkat-api.my.id/api/otakudesu/home
```
# get info of comic
with required url anime
```
https://latipharkat-api.my.id/api/otakudesu/info/?url=https://otakudesu.cam/anime/berserk-gluttony-sub-indo/
```
## output 
```JSON
{
  "author": "Latip176", 
  "data": {
    "cover": "https://otakudesu.cam/wp-content/uploads/2023/10/Boushoku-no-Berserk.jpg", 
    "data_episode": [
      {
        "judul_episode": "Boushoku no Berserk Episode 9 Subtitle Indonesia", 
        "release": "27 November,2023", 
        "url": "https://otakudesu.cam/episode/bnb-episode-9-sub-indo/"
      }, 
      {
        "judul_episode": "Boushoku no Berserk Episode 8 Subtitle Indonesia", 
        "release": "20 November,2023", 
        "url": "https://otakudesu.cam/episode/bnb-episode-8-sub-indo/"
      }, 
      {
        "judul_episode": "Boushoku no Berserk Episode 7 Subtitle Indonesia", 
        "release": "13 November,2023", 
        "url": "https://otakudesu.cam/episode/bnb-episode-7-sub-indo/"
      }, 
      {
        "judul_episode": "Boushoku no Berserk Episode 6 Subtitle Indonesia", 
        "release": "6 November,2023", 
        "url": "https://otakudesu.cam/episode/bnb-episode-6-sub-indo/"
      }, 
      {
        "judul_episode": "Boushoku no Berserk Episode 5 Subtitle Indonesia", 
        "release": "30 Oktober,2023", 
        "url": "https://otakudesu.cam/episode/bnb-episode-5-sub-indo/"
      }, 
      {
        "judul_episode": "Boushoku no Berserk Episode 4 Subtitle Indonesia", 
        "release": "23 Oktober,2023", 
        "url": "https://otakudesu.cam/episode/bnb-episode-4-sub-indo/"
      }, 
      {
        "judul_episode": "Boushoku no Berserk Episode 3 Subtitle Indonesia", 
        "release": "16 Oktober,2023", 
        "url": "https://otakudesu.cam/episode/bnb-episode-3-sub-indo/"
      }, 
      {
        "judul_episode": "Boushoku no Berserk Episode 2 Subtitle Indonesia", 
        "release": "9 Oktober,2023", 
        "url": "https://otakudesu.cam/episode/bnb-episode-2-sub-indo/"
      }, 
      {
        "judul_episode": "Boushoku no Berserk Episode 1 Subtitle Indonesia", 
        "release": "2 Oktober,2023", 
        "url": "https://otakudesu.cam/episode/bnb-episode-1-sub-indo/"
      }
    ], 
    "durasi": "23 Min.", 
    "genre": "Action, Fantasy", 
    "japanese": "\u66b4\u98df\u306e\u30d9\u30eb\u30bb\u30eb\u30af", 
    "judul": "Boushoku no Berserk", 
    "produser": "Genco, HIAN", 
    "sinopsis": "", 
    "skor": "", 
    "status": "Ongoing", 
    "studio": "A.C.G.T.", 
    "tanggal_rilis": "Okt 05, 2023", 
    "tipe": "TV", 
    "total_episode": "Unknown"
  }, 
  "msg": "debug!"
}
```
# get stream link
with required url episode anime
```
https://latipharkat-api.my.id/api/otakudesu/view/?url=https://otakudesu.cam/episode/bnb-episode-9-sub-indo/
```
### output
```JSON
{
  "author": "Latip176", 
  "data": {
    "judul_episode": "Boushoku no Berserk Episode 9 Subtitle Indonesia", 
    "next": "None", 
    "prev": "https://otakudesu.cam/episode/bnb-episode-8-sub-indo/", 
    "stream": "https://desustream.me/beta/stream/hd/?id=cS82L0lXZWJtN3BybStySDJvWnp3Zz09"
  }, 
  "msg": "debug!"
}
```
