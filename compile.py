import os, frontmatter, markdown
from jinja2 import Environment, FileSystemLoader, contextfilter, Markup

def markdownfilter(val):
	return Markup(markdown.markdown(val))

env = Environment(loader=FileSystemLoader("./templates/"))
env.filters["markdown"]=markdownfilter
temp = env.get_template("article.html")

if not os.path.exists("build"):
	os.system("mkdir build; cp style.css build")

articles = os.listdir("articles")
articles = [[os.path.splitext(x)[0],frontmatter.load("articles/"+x)] for x in articles]
for article in articles:
	if article[1]["published"]:
		with open("build/"+article[0]+".html","w") as f:
			f.write(temp.render(article=article[1],filename=article[0]))
with open("build/index.html","w") as f:
	f.write(env.get_template("mainpage.html").render(articles=articles))
