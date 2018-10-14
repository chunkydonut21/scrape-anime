# Scrape Anime

ScrapeAnime scrapes all Anime details, episodes, Video Url from KissAnime.
This scraper can scrape all Anime available on Kissanime in any genre, year, category. It also bypass Cloudflare's anti-bot protection to easily scrape Anime.


## INSTALLATION
``` pip install scrape-anime ```

## REQUIREMENTS
Python 3 is required to run this script. <br>
This script uses BeautifulSoup4 and cfscrape.
## USAGE


```from scrape_anime import scrape```



#### Returns All anime results from specific page.

```scrape.getAnimeList('http://kissanime.ru/AnimeList?page=21')```


#### Returns Anime information
```scrape.getAnimeInformantion('http://kissanime.ru/Anime/Naruto')```

#### Returns Anime Epsiode List with Episode Video URL (rapidvideo is default)
```scrape.getAnimeEpisodesDetails('http://kissanime.ru/Anime/Naruto')```

#### Returns Custom Anime List from Specific page (default is page 1)(based on category, status, year, alphabet)
```scrape.getCustomAnimeList('http://kissanime.ru/Genre/Harem')```
```scrape.getCustomAnimeList('http://kissanime.ru/AnimeList?c=g&page=3')```


<br>
### HAVE FUN <3
