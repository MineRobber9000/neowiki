import os, frontmatter, markdown, configparser
from jinja2 import Environment, FileSystemLoader, contextfilter, Markup

def markdownfilter(val):
	return Markup(markdown.markdown(val))

env = Environment(loader=FileSystemLoader("./templates/"))
env.filters["markdown"]=markdownfilter

config = configparser.ConfigParser()
config.read("config.ini")
assert "neowiki" in config.sections(),"Invalid config file: must have neowiki section"
assert "published_path" in config["neowiki"],"Invalid config file: must have published_path directive under neowiki section"
pubdir = config["neowiki"]["published_path"]

temp = env.get_template("article.html")

if not os.path.exists("build"):
	os.system("mkdir build; cp assets/* build")

articles = os.listdir("articles")
articles = [[os.path.splitext(x)[0],frontmatter.load("articles/"+x)] for x in articles]
for article in articles:
	if article[1]["published"]:
		with open("build/"+article[0]+".html","w") as f:
			f.write(temp.render(article=article[1],filename=article[0],pubdir=pubdir))
with open("build/index.html","w") as f:
	f.write(env.get_template("mainpage.html").render(articles=articles,pubdir=pubdir))
