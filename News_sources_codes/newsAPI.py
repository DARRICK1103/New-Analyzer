from concurrent.futures import ThreadPoolExecutor
import random
import requests
import json
from PIL import Image
from io import BytesIO


def getNews():
    headers = {'Authorization': '9f6cddd1f26045cfbe21691dac62ed03'}
    top_headlines = "https://newsapi.org/v2/top-headlines?"
    symbols = " "
    country = ['my']
    sources = ['bbc-news', 'business-insider', 'financial-post', 'google-news', 'reuters', 'nbc-news', 'techcrunch', 'the-wall-street-journal']
    sorby = "popularity"
    # set up the query parameters
    params = {
        'q': symbols,
        'apiKey': '9f6cddd1f26045cfbe21691dac62ed03',
        'sortBy': sorby,
        'language': 'en',
        'pageSize': 100,  # Update the pageSize to 10
        'page': 1
    }

    # send the request to the API and get the response
    response = requests.get(url=top_headlines, headers=headers, params=params)

    # convert the response to a JSON object
    output = response.json()

    # retrieve all articles from the response
    articles = output['articles']

    # Create a new list to store the desired properties
    filtered_articles = []
    for article in articles:
        filtered_article = {
            'title': article['title'],
            'image_url': article['urlToImage'],
            'url': article['url']
        }
        filtered_articles.append(filtered_article)

    while 'next' in response.links.keys():
        response = requests.get(response.links['next']['url'], headers=headers, params=params)
        output = response.json()
        articles = output['articles']
        for article in articles:
            filtered_article = {
                'title': article['title'],
                'image_url': article['urlToImage'],
                'url': article['url']
            }
            filtered_articles.append(filtered_article)

    # return the filtered articles list
    return filtered_articles



def getByCategory(category):
    headers = {'Authorization': '9f6cddd1f26045cfbe21691dac62ed03'}
    top_headlines = "https://newsapi.org/v2/top-headlines?"
    symbols = " "
    country = ['my']
    sources = ['bbc-news', 'business-insider', 'financial-post', 'google-news', 'reuters','nbc-news', 'techcrunch', 'the-wall-street-journal']
    sorby = "popularity"
    # set up the query parameters
    params= {
        'q': symbols,
        'category': category,
        'apiKey': '9f6cddd1f26045cfbe21691dac62ed03',
        'sortBy': sorby,
        'language': 'en',
        'pageSize': 100,
        'page': 1
        }

    # send the request to the API and get the response
    response = requests.get(url=top_headlines, headers=headers, params=params)

    # convert the response to a JSON object
    output = response.json()

    # retrieve all articles from the response
    articles = output['articles']
    while 'next' in response.links.keys():
        response = requests.get(response.links['next']['url'], headers=headers, params=params)
        output = response.json()
        articles += output['articles']

    return articles


def searchNews(search):
    headers = {'Authorization': '9f6cddd1f26045cfbe21691dac62ed03'}
    top_headlines = "https://newsapi.org/v2/everything?"
    sorby = "relevancy"
    # set up the query parameters
    params= {
        'q': search,
        'apiKey': '9f6cddd1f26045cfbe21691dac62ed03',
        'sortBy': sorby,
        'language': 'en',
        'pageSize': 50,
        'page': 1
        }

    # send the request to the API and get the response
    response = requests.get(url=top_headlines, headers=headers, params=params)

    # convert the response to a JSON object
    output = response.json()

    # Check if the response contains 'articles'
    if 'articles' in output:
        articles = output['articles']
    else:
        print("Error: Unable to retrieve articles from the response.")
        return []

    total_results = output.get('totalResults', 0)
    total_pages = (total_results + params['pageSize'] - 1) // params['pageSize']

    # Retrieve all articles from multiple pages (up to page 300)
    for page in range(2, min(total_pages + 1, 301)):
        params['page'] = page
        response = requests.get(url=top_headlines, headers=headers, params=params)
        output = response.json()

        # Check if the response contains 'articles'
        if 'articles' in output:
            print(f"Found articles from page {page}.")
            new_articles = output['articles']
        else:
            print(f"Error: Unable to retrieve articles from page {page}.")
            continue

        # Filter articles with valid image URLs using the validate_image function
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(validate_image, article) for article in new_articles]
            for future in futures:
                article = future.result()
                if article is not None:
                    articles.append(article)
        
    return articles

def getSports():
  
    category = "sports"
    headers = {'Authorization': '9f6cddd1f26045cfbe21691dac62ed03'}
    top_headlines = "https://newsapi.org/v2/top-headlines?"
    symbols = " "
    country = ['my']
    sources = ['bbc-news', 'business-insider', 'financial-post', 'google-news', 'reuters','nbc-news', 'techcrunch', 'the-wall-street-journal']
    sorby = "popularity"
    # set up the query parameters
    params= {
        'q': symbols,
        'category': category,
        'apiKey': '9f6cddd1f26045cfbe21691dac62ed03',
        'sortBy': sorby,
        'language': 'en',
        'pageSize': 100,
        'page': 1
        }

    # send the request to the API and get the response
    response = requests.get(url=top_headlines, headers=headers, params=params)

    # convert the response to a JSON object
    output = response.json()

    # Check if the response contains 'articles'
    if 'articles' in output:
        articles = output['articles']
    else:
        print("Error: Unable to retrieve articles from the response.")
        return []

    total_results = output.get('totalResults', 0)
    total_pages = (total_results + params['pageSize'] - 1) // params['pageSize']

    # Retrieve all articles from multiple pages
    for page in range(2, total_pages + 1):
        params['page'] = page
        response = requests.get(url=top_headlines, headers=headers, params=params)
        output = response.json()

        # Check if the response contains 'articles'
        if 'articles' in output:
            new_articles = output['articles']
        else:
            print(f"Error: Unable to retrieve articles from page {page}.")
            continue

        # Filter articles with valid image URLs using the validate_image function
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(validate_image, article) for article in new_articles]
            for future in futures:
                article = future.result()
                if article is not None:
                    articles.append(article)
        
        # Check if we have collected 30 articles with valid images
        if len(articles) >= 70:
            break

    # Randomly select 8 articles from the selected articles
    random_articles = random.sample(articles, k=min(45, len(articles)))

    # Print the total number of results
    print(f"Total Results: {total_results}")

    return random_articles


def getEntertainment():
  
    category = "entertainment"
    headers = {'Authorization': '9f6cddd1f26045cfbe21691dac62ed03'}
    top_headlines = "https://newsapi.org/v2/top-headlines?"
    symbols = " "
    country = ['my']
    sources = ['bbc-news', 'business-insider', 'financial-post', 'google-news', 'reuters','nbc-news', 'techcrunch', 'the-wall-street-journal']
    sorby = "popularity"
    # set up the query parameters
    params= {
        'q': symbols,
        'category': category,
        'apiKey': '9f6cddd1f26045cfbe21691dac62ed03',
        'sortBy': sorby,
        'language': 'en',
        'pageSize': 100,
        'page': 1
        }

    # send the request to the API and get the response
    response = requests.get(url=top_headlines, headers=headers, params=params)

    # convert the response to a JSON object
    output = response.json()

    # Check if the response contains 'articles'
    if 'articles' in output:
        articles = output['articles']
    else:
        print("Error: Unable to retrieve articles from the response.")
        return []

    total_results = output.get('totalResults', 0)
    total_pages = (total_results + params['pageSize'] - 1) // params['pageSize']

    # Retrieve all articles from multiple pages
    for page in range(2, total_pages + 1):
        params['page'] = page
        response = requests.get(url=top_headlines, headers=headers, params=params)
        output = response.json()

        # Check if the response contains 'articles'
        if 'articles' in output:
            new_articles = output['articles']
        else:
            print(f"Error: Unable to retrieve articles from page {page}.")
            continue

        # Filter articles with valid image URLs using the validate_image function
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(validate_image, article) for article in new_articles]
            for future in futures:
                article = future.result()
                if article is not None:
                    articles.append(article)
        
        # Check if we have collected 30 articles with valid images
        if len(articles) >= 70:
            break

    # Randomly select 8 articles from the selected articles
    random_articles = random.sample(articles, k=min(45, len(articles)))

    # Print the total number of results
    print(f"Total Results: {total_results}")

    return random_articles


def getTechnology():
  
    category = "technology"
    headers = {'Authorization': '9f6cddd1f26045cfbe21691dac62ed03'}
    top_headlines = "https://newsapi.org/v2/top-headlines?"
    symbols = " "
    country = ['my']
    sources = ['bbc-news', 'business-insider', 'financial-post', 'google-news', 'reuters','nbc-news', 'techcrunch', 'the-wall-street-journal']
    sorby = "popularity"
    # set up the query parameters
    params= {
        'q': symbols,
        'category': category,
        'apiKey': '9f6cddd1f26045cfbe21691dac62ed03',
        'sortBy': sorby,
        'language': 'en',
        'pageSize': 100,
        'page': 1
        }

    # send the request to the API and get the response
    response = requests.get(url=top_headlines, headers=headers, params=params)

    # convert the response to a JSON object
    output = response.json()

    # Check if the response contains 'articles'
    if 'articles' in output:
        articles = output['articles']
    else:
        print("Error: Unable to retrieve articles from the response.")
        return []

    total_results = output.get('totalResults', 0)
    total_pages = (total_results + params['pageSize'] - 1) // params['pageSize']

    # Retrieve all articles from multiple pages
    for page in range(2, total_pages + 1):
        params['page'] = page
        response = requests.get(url=top_headlines, headers=headers, params=params)
        output = response.json()

        # Check if the response contains 'articles'
        if 'articles' in output:
            new_articles = output['articles']
        else:
            print(f"Error: Unable to retrieve articles from page {page}.")
            continue

        # Filter articles with valid image URLs using the validate_image function
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(validate_image, article) for article in new_articles]
            for future in futures:
                article = future.result()
                if article is not None:
                    articles.append(article)
        
        # Check if we have collected 30 articles with valid images
        if len(articles) >= 70:
            break

    # Randomly select 8 articles from the selected articles
    random_articles = random.sample(articles, k=min(45, len(articles)))

    # Print the total number of results
    print(f"Total Results: {total_results}")

    return random_articles

# ------------------------------------------------------------

def validate_image(article):
    image_url = article['urlToImage']
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        img_data = response.content

        img_file = BytesIO(img_data)
        image = Image.open(img_file)
        image.verify()

        return article

    except (requests.exceptions.RequestException, Image.UnidentifiedImageError) as e:
        print(f"Error: Unable to process image for article: {e}")
        return None

# 4a1881413b8143db95b834e4b976230d
def getNewsItem():
    headers = {'Authorization': '9f6cddd1f26045cfbe21691dac62ed03'}
    top_headlines = "https://newsapi.org/v2/top-headlines?"
    symbols = " "
    country = ['my']
    sources = ['bbc-news', 'business-insider', 'financial-post', 'google-news', 'reuters','nbc-news', 'techcrunch', 'the-wall-street-journal']
    sorby = "popularity"
    
    params= {
        'q': symbols,
        'apiKey': '9f6cddd1f26045cfbe21691dac62ed03',
        'sortBy': sorby,
        'language': 'en',
        'pageSize': 100,  # Increase the page size to reduce the number of API requests
        'page': 1
    }

    response = requests.get(url=top_headlines, headers=headers, params=params)
    output = response.json()


    # Check if the response contains 'articles'
    if 'articles' in output:
        articles = output['articles']
    else:
        print("Error: Unable to retrieve articles from the response.")
        return []

    total_results = output.get('totalResults', 0)
    total_pages = (total_results + params['pageSize'] - 1) // params['pageSize']

    # Retrieve all articles from multiple pages
    for page in range(2, total_pages + 1):
        params['page'] = page
        response = requests.get(url=top_headlines, headers=headers, params=params)
        output = response.json()

        # Check if the response contains 'articles'
        if 'articles' in output:
            new_articles = output['articles']
        else:
            print(f"Error: Unable to retrieve articles from page {page}.")
            continue

        # Filter articles with valid image URLs using the validate_image function
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(validate_image, article) for article in new_articles]
            for future in futures:
                article = future.result()
                if article is not None:
                    articles.append(article)
        
        # Check if we have collected 30 articles with valid images
        if len(articles) >= 70:
            break

    # Randomly select 8 articles from the selected articles
    random_articles = random.sample(articles, k=min(45, len(articles)))

    # Print the total number of results
    print(f"Total Results: {total_results}")

    return random_articles


