import newspaper
from newspaper import Article
import nltk
from textblob import TextBlob

def getContent(link1):
    nltk.download('punkt')
    url = link1
    image_url = ''  # Default value for image_url
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        # Extract the image URL from the article
        image_url = article.top_image

        
    except newspaper.ArticleException as e:
        print(f"Error occurred while downloading/parsing the article: {str(e)}")
    
    # Return the article object and image_url
    return article, image_url
