from bs4 import BeautifulSoup
import requests

def fetch_and_parse_news(url, limit):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    article_containers = soup.select('li.post-item')[:limit]

    news_data = []
    for container in article_containers:
        title_element = container.find('h2', class_='post-title')
        title = title_element.get_text().strip() if title_element else None
        link = title_element.find('a')['href'] if title_element and title_element.find('a') else None

        date_element = container.select_one('span.date.meta-item.tie-icon')
        date_time = date_element.get_text().strip() if date_element else None

        image_element = container.find('img', class_='attachment-jannah-image-large')
        image_url = image_element['src'] if image_element else None

        if title and link and date_time and image_url:
            news_data.append({
                'title': title,
                'link': link,
                'time': date_time,
                'image_url': "https://new-science.ru/" + image_url
            })

    return news_data