# otakudesu-api

Rest API for get Data Anime from otakudesu

# get index home

```
https://latipharkat-api.my.id/api/otakudesu/home
```

# get info of anime

with required data anime

```
https://latipharkat-api.my.id/api/otakudesu/info/?data=berserk-gluttony-sub-indo
```

### results

```JSON
{
  "author": "Latip176",
  "data": {
    "cover": "https://otakudesu.cam/wp-content/uploads/2023/10/Boushoku-no-Berserk.jpg",
    "data_episode": [
      {
        "data": "bnb-episode-9-sub-indo",
        "judul_episode": "Boushoku no Berserk Episode 9 Subtitle Indonesia",
        "release": "27 November,2023"
      },
      {
        "data": "bnb-episode-8-sub-indo",
        "judul_episode": "Boushoku no Berserk Episode 8 Subtitle Indonesia",
        "release": "20 November,2023"
      },
      {
        "data": "bnb-episode-7-sub-indo",
        "judul_episode": "Boushoku no Berserk Episode 7 Subtitle Indonesia",
        "release": "13 November,2023"
      },
      {
        "data": "bnb-episode-6-sub-indo",
        "judul_episode": "Boushoku no Berserk Episode 6 Subtitle Indonesia",
        "release": "6 November,2023"
      },
      {
        "data": "bnb-episode-5-sub-indo",
        "judul_episode": "Boushoku no Berserk Episode 5 Subtitle Indonesia",
        "release": "30 Oktober,2023"
      },
      {
        "data": "bnb-episode-4-sub-indo",
        "judul_episode": "Boushoku no Berserk Episode 4 Subtitle Indonesia",
        "release": "23 Oktober,2023"
      },
      {
        "data": "bnb-episode-3-sub-indo",
        "judul_episode": "Boushoku no Berserk Episode 3 Subtitle Indonesia",
        "release": "16 Oktober,2023"
      },
      {
        "data": "bnb-episode-2-sub-indo",
        "judul_episode": "Boushoku no Berserk Episode 2 Subtitle Indonesia",
        "release": "9 Oktober,2023"
      },
      {
        "data": "bnb-episode-1-sub-indo",
        "judul_episode": "Boushoku no Berserk Episode 1 Subtitle Indonesia",
        "release": "2 Oktober,2023"
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
  "msg": "success"
}
```

# get stream link

with required data episode anime

```
https://latipharkat-api.my.id/api/otakudesu/view/?url=woar-episode-9-sub-indo
```

### results

```JSON
{
  "author": "Latip176",
  "data": {
    "judul_episode": "Watashi no Oshi wa Akuyaku Reijou. Episode 9 Subtitle Indonesia",
    "next": "None",
    "prev": "https://otakudesu.cam/episode/woar-episode-8-sub-indo/",
    "stream": "https://desustream.me/updesu/hd/?id=K1d3bTVkcExyN3VFb2prUHJMeTlxQT09"
  },
  "msg": "success"
}
```

# search anime by keyword

with required keyword

```
https://latipharkat-api.my.id/api/otakudesu/search/?keyword=kage+no+jitsu
```

### results

```JSON
{
  "author": "Latip176",
  "data": {
    "data": [
      {
        "cover": "https://otakudesu.cam/wp-content/uploads/2023/10/Kage-no-Jitsuryokusha-ni-Naritakute-2nd-Season.jpg",
        "data": "kage-ni-naritakute-s2-sub-indo",
        "genres": "Action, Comedy, Fantasy, Isekai, Reincarnation",
        "judul": "Kage no Jitsuryokusha ni Naritakute! Season 2 Subtitle Indonesia",
        "rating": "8.55",
        "status": "Ongoing"
      },
      {
        "cover": "https://otakudesu.cam/wp-content/uploads/2023/02/Kage-no-Jitsuryokusha-ni-Naritakute-Sub-Indo.jpg",
        "data": "kage-ni-naritakute-sub-indo",
        "genres": "Action, Comedy, Fantasy, Isekai, Reincarnation",
        "judul": "Kage no Jitsuryokusha ni Naritakute! (Episode 1 - 20) Subtitle Indonesia",
        "rating": "8.38",
        "status": "Completed"
      }
    ]
  },
  "msg": "success"
}
```
