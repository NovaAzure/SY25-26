import requests
from bs4 import BeautifulSoup

def scrape_books_from_page(url):
    try:
        response = requests.get(url)  # Send a GET request to the URL
        response.raise_for_status()  # Ensure the request was successful (status code 200)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")  # Print any error if the request fails
        return []  # Return an empty list if an error occurs

    soup = BeautifulSoup(response.text, 'html.parser')  # Parse the HTML content using BeautifulSoup
    books = soup.find_all('article', class_='product_pod')  # Find all 'article' elements representing books

    book_data = []  # Initialize an empty list to store the scraped book data
    for book in books:
        title = book.h3.a['title']  # Extract the title of the book from the 'title' attribute
        price = book.find('p', class_='price_color').text  # Extract the price of the book
        availability = book.find('p', class_='instock availability').text.strip()  # Extract availability status
        rating_class = book.p['class']  # Extract the 'class' attribute for the book's rating
        rating = rating_class[1] if len(rating_class) > 1 else "No rating"  # Get the rating (if available)
        image_url = 'https://books.toscrape.com/' + book.find('img')['src'].replace('../', '')  # Construct the image URL

        # Append the book details as a dictionary to the list
        
        book_info =({
            'Title': title,
            'Price': price,
            'Availability': availability,
            'Rating': rating,
            'Image URL': image_url
        })
        book_data.append(book_info)

    linklist = []
    genrelist = []
    print("Links found on page:")
    for link in soup.find_all('a'):
        href = link.get('href')
        text = link.text.strip()
        print(f"Text: {text} | URL: {href}")
        linklist.append(href)
        genrelist.append(text)

    return book_data # Return the list of scraped book data

def get_genre(url):
    try:
        response = requests.get(url)  # Send a GET request to the URL
        response.raise_for_status()  # Ensure the request was successful (status code 200)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")  # Print any error if the request fails
        return []  # Return an empty list if an error occurs

    soup = BeautifulSoup(response.text, 'html.parser')  # Parse the HTML content using BeautifulSoup
    books = soup.find_all('article', class_='product_pod')  # Find all 'article' elements representing books
    linklist = []
    genrelist = []
    print("Links found on page:")
    for link in soup.find_all('a'):
        href = link.get('href')
        text = link.text.strip()
        print(f"Text: {text} | URL: {href}")
        linklist.append(href)
        genrelist.append(text)

    return linklist

book_data = scrape_books_from_page("https://books.toscrape.com")
genrelist = get_genre("https://books.toscrape.com")
"""
print("Links found on page:")
for link in soup.find_all('a'):
    href = link.get('href')
    text = link.text.strip()
    print(f"Text: {text} | URL: {href}")
    """
"""
for book in book_data:
    data = book
    print(data['Title'])
    price = data['Price']
    print(price[1:])
    print(data['Availability'])
    print(data['Rating'] + " Star Rating")
    print(data['Image URL'])
    print("----------")
"""
genreask = input("What genre would you like to search for?: ")
for item in genrelist:
    if genreask.lower() in item:
        print(item)
    else:
        while genreask.lower() not in item:
            print("Chosen genre has not been found.")
            genreask = input("What genre would you like to search for?: ")
            for item in genrelist:
                if genreask.lower() in item:
                    print(item)
                    break