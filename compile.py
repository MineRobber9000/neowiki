import os, frontmatter, markdown, configparser
from jinja2 import Environment, FileSystemLoader, contextfilter, Markup

def markdownfilter(val):
	return Markup(markdown.markdown(val))

env = Environment(loader=FileSystemLoader("./templates/"))
env.filters["markdown"]=markdownfilter

config = configparser.ConfigParser()
config.read("config.ini")
assert "neowiki" in config.sections(),"Invalid config file: must have neowiki section"
config = config["neowiki"]
assert "published_path" in config,"Invalid config file: must have published_path directive under neowiki section"
pubdir = config["published_path"]
assert "contributors" in config,"Invalid config file: must have contributors list under neowiki section"
contributors = config["contributors"].split(",")

temp = env.get_template("article.html")

if not os.path.exists("build"):
	os.system("mkdir build; cp assets/* build")

articles = os.listdir("articles")
articles = [[os.path.splitext(x)[0],frontmatter.load("articles/"+x)] for x in articles]
articles.sort(key=lambda x: x[1].title)
for article in articles:
	if article[1]["published"]:
		with open("build/"+article[0]+".html","w") as f:
			f.write(temp.render(article=article[1],filename=article[0],pubdir=pubdir))
with open("build/index.html","w") as f:
	f.write(env.get_template("mainpage.html").render(articles=articles,pubdir=pubdir))
with open("build/contributors.html","w") as f:
	f.write(env.get_template("contributors.html").render(contributors=contributors))
