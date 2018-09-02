import os, frontmatter, markdown
from jinja2 import Environment, FileSystemLoader, contextfilter, Markup

def markdownfilter(val):
	return Markup(markdown.markdown(val))

env = Environment(loader=FileSystemLoader("./templates/"))
env.filters["markdown"]=markdownfilter
temp = env.get_template("article.html")

articles = os.listdir("articles")
articles = [[os.path.splitext(x)[0],frontmatter.load("articles/"+x)] for x in articles]
for article in articles:
	if article[1]["published"]:
		with open(article[0]+".html","w") as f:
			f.write(temp.render(article=article[1]))
