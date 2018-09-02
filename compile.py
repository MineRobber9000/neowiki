import os, frontmatter, markdown

articles = os.listdir("articles")
articles = [[os.path.splitext(x)[0],frontmatter.load("articles/"+x)] for x in articles]
for article in articles:
	if article[1]["published"]:
		with open(article[0]+".html","w") as f:
			f.write(markdown.markdown(article[1].content))
