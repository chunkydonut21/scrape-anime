from bs4 import BeautifulSoup
import cfscrape
import re

scraper = cfscrape.create_scraper()

def getAnimeList(link):
    source = scraper.get(link)
    soup = BeautifulSoup(source.text, 'lxml')

    lst = []

    for anime in soup.find_all('tr')[2:]:
        title = anime.td.a.text.strip()
        url = anime.td.a['href'].strip()
        status = anime.find_all('td')[-1].text.strip()

        lst.append({
            'title': title,
            'url': url,
            'status': status
        })

    return lst


def getAnimeInformantion(link):
    source = scraper.get(link)
    soup = BeautifulSoup(source.text, 'lxml')

    container = soup.find('div', id='container')

    name = container.find('a', class_='bigChar').text.strip()

    genreList = [genre.text.strip() for genre in container.find_all('a', class_='dotUnder')]

    p = container.find_all('p')

    description = p[-1].text.strip().replace(u'\xa0', u' ')

    aired = p[2].text.strip().replace(u'\xa0', u' ')

    detail = p[3].text.split("\n")
    detail = [x.strip().replace(u'\xa0', u' ') for x in detail if x is not None]

    status = detail[1].split(":")[1]
    views = detail[2].split(":")[1]

    animeDescription = {
        "name": name,
        "aired": aired,
        "status": status,
        "views": views,
        "genre": genreList,
        "description": description
    }

    return animeDescription


def getEpisodeVideoUrl(link):
    source = scraper.get(link)
    soup = BeautifulSoup(source.text, 'lxml')
    for line in soup:
        stuff = re.findall('\S+rapidvideo.com\S+', str(line))
        if (len(stuff) > 0):
            episodeUrl = stuff

    return episodeUrl[0]


def getAnimeEpisodesDetails(link):
    source = scraper.get(link)
    soup = BeautifulSoup(source.text, 'lxml')

    container = soup.find('table')

    lst = []
    for items in container.find_all('a'):
        name = items.text.strip()
        url = getEpisodeVideoUrl(f"http://kissanime.ru/{items['href']}&s=rapidvideo")
        title = items['title']
        lst.append({"name": name, "url": url, "title": title})

    return lst


def getCustomAnimeList(link):
    source = scraper.get(link)
    soup = BeautifulSoup(source.text, 'lxml')

    lst = []

    for anime in soup.find_all('tr')[2:]:
        title = anime.td.a.text.strip()
        url = anime.td.a['href'].strip()
        status = anime.find_all('td')[-1].text.strip()

        lst.append({
            'title': title,
            'url': url,
            'status': status
        })

    return lst