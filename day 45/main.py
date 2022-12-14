from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text


soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

highest_upvote = max(article_upvotes)
max_index = article_upvotes.index(highest_upvote)

print(article_texts)
print(article_links)
print(article_upvotes)



# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.title.string)
# #
# # print(soup.prettify())
# #
# # print(soup.p)
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
#
# # for tag in all_anchor_tags:
# #     # print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# h3_heading = soup.find(name="h3", class_="heading")
# # print(h3_heading)
#
# company_url = soup.select_one(selector="p a")  # this code selects <a> tag that sits inside a <p> tag
# print(company_url.get("href"))
#
# name = soup.select_one(selector="#name")  # This code selects the item that has id="name"
# print(name.getText())
#
# class_heading = soup.select(".heading")  # This code selects the item that has class="heading"
# print(class_heading)
#
# new_list = [tag.getText() for tag in class_heading]
# print(new_list)
#
# # To summarize:
# # # to search id
# # . to search class
# # you can search a tag inside a tag like "p a" --> basically the a tag inside a p tag
