# otakudesu-api

Rest API to fetch anime data from otakudesu.

# get index home

```
https://latipharkat-api.my.id/api/otakudesu/home
```

# get ongoing anime

```
https://latipharkat-api.my.id/api/otakudesu/ongoing
```

`You can get the next page by appending /?next=page-2 or other.`

```
https://latipharkat-api.my.id/api/otakudesu/ongoing/?next=page-2
```

### results

```JSON
{
  "author": "Latip176",
  "data": {
    "data_anime": [
      {
        "cover": "https://otakudesu.cam/wp-content/uploads/2023/10/Dekoboko-Majo-no-Oyako-Jijou.jpg",
        "data": "dekobo-oyako-jijou-sub-indo",
        "episode": "Episode 10",
        "judul": "Dekoboko Majo no Oyako Jijou",
        "release": "27 Nov",
        "release_on_every": "Senin"
      },
      // ... (other anime entries)
    ],
    "next": "page-2"
  },
  "msg": "success"
}

```

# get complete anime

```
https://latipharkat-api.my.id/api/otakudesu/complete
```

`You can get the next page by appending /?next=page-2 or other.`

```
https://latipharkat-api.my.id/api/otakudesu/complete/?next=page-2
```

### results

```JSON
{
  "author": "Latip176",
  "data": {
    "data_anime": [
      {
        "cover": "https://otakudesu.cam/wp-content/uploads/2023/10/Dekoboko-Majo-no-Oyako-Jijou.jpg",
        "data": "dekobo-oyako-jijou-sub-indo",
        "episode": "Episode 10",
        "judul": "Dekoboko Majo no Oyako Jijou",
        "release": "27 Nov",
        "release_on_every": "Senin"
      },
      // ... (other anime entries)
    ],
    "next": "page-2"
  },
  "msg": "success"
}

```

# search anime by keyword

With the required keyword

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
      // ... (other anime entries)
    ]
  },
  "msg": "success"
}

```

# search anime by genre

## get all genre

```
https://latipharkat-api.my.id/api/otakudesu/genres
```

### results

```JSON
{
  "author": "Latip176",
  "data": {
    "genres": [
      // ... (list of genres with data and name)
    ]
  },
  "msg": "success"
}

```

## search genre

```
https://latipharkat-api.my.id/api/otakudesu/genres/<genre>/
```

### results example https://latipharkat-api.my.id/api/otakudesu/genres/action

```JSON
{
  "author": "Latip176",
  "data": [
    // ... (list of anime entries with cover, genre, rating, studio, judul, total_episode, data, next, prev)
  ],
  "msg": "success"
}

```

## seach genre by append page

```
https://latipharkat-api.my.id/api/otakudesu/genres/<genre>/<page>
```

### results example https://latipharkat-api.my.id/api/otakudesu/genres/action/2

```JSON
{
  "author": "Latip176",
  "data": [
    // ... (list of anime entries with cover, genre, rating, studio, judul, total_episode, data, next, prev)
  ],
  "msg": "success"
}

```

# get info of anime

With the required data anime

```
https://latipharkat-api.my.id/api/otakudesu/info/?data=berserk-gluttony-sub-indo
```

### results

```JSON
{
  "author": "Latip176",
  "data": {
    // ... (anime details like cover, data_episode, durasi, genre, japanese, judul, produser, sinopsis, skor, status, studio, tanggal_rilis, tipe, total_episode)
  },
  "msg": "success"
}
```

# get stream link

With the required data episode anime

```
https://latipharkat-api.my.id/api/otakudesu/view/?data=woar-episode-9-sub-indo
```

### results

```JSON
{
  "author": "Latip176",
  "data": {
    // ... (streaming details like judul_episode, next, prev, stream)
  },
  "msg": "success"
}

```
