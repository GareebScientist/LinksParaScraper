import requests
from bs4 import BeautifulSoup

def scrape_and_save(links, filename="output.txt"):
    """Scrapes paragraphs and titles from given links and saves to a text file.

    Args:
        links (list): A list of URLs (strings) to scrape.
        filename (str, optional): The name of the output file. Defaults to "output.txt".
    """

    with open(filename, "w", encoding="utf-8") as f:
        for link in links:
            try:
                response = requests.get(link)
                response.raise_for_status()  # Raise an error for bad status codes

                soup = BeautifulSoup(response.content, 'html.parser')

                title = soup.find('title').text.strip() if soup.find('title') else "Title Not Found"
                paragraphs = [p.text.strip() for p in soup.find_all('p')]

                f.write(f"## {title}\n\n")
                for paragraph in paragraphs:
                    f.write(f"{paragraph}\n\n")

            except requests.exceptions.RequestException as e:
                print(f"Error fetching {link}: {e}")

if __name__ == "__main__":
    links = [
        # Add your newline-separated links here
        "https://www.geo.tv/latest/541855-pakistans-historic-lunar-mission-set-to-be-launched-this-week",
        "https://www.thenews.com.pk/latest/1183996-pakistans-lunar-mission-all-set-to-be-launched-on-friday",
        "https://www.dawn.com/news/1830608",
        "https://urdu.geo.tv/latest/363630-",
        "https://www.urdunews.com/node/855356-",
        "https://www.bbc.com/urdu/articles/cekl195egg7o",
        "https://www.brecorder.com/news/40301210",
        "https://e.thenews.com.pk/detail?id=303367",
        "https://jang.com.pk/news/1346489",
        "https://www.thenews.com.pk/amp/1184911-pakistans-first-moon-mission-icube-qamar-to-be-launched-today",
        "https://cpecinfo.com/joint-triumph-pakistans-first-moon-mission-launched-from-chinas-change6/",
        "https://www.dawn.com/news/1831337"
        # ... more links
    ]
    scrape_and_save(links, "scraped_data.txt") 