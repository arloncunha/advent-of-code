from newspaper import Article

article = Article('https://www.npr.org/2019/07/10/740387601/university-of-texas-austin-promises-free-tuition-for-low-income-students-in-2020')
article.download()
article.parse()
article.nlp()

print(article.title)
print(article.publish_date)
print(article.summary)
