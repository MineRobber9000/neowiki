---
published: true
title: Writing for neowiki
description: A small tutorial on how to write for neowiki.
---

Here's how to write for neowiki. (I'm not sure why you'd want to, but here's how.)

## Step 1. Fork

The first step is the easiest, and depending on how you're doing this, it may be automatically done for you! (If you're using GitHub on the web, skip this part)
Go to [the repo,](//github.com/MineRobber9000/neowiki) and click the "Fork" button at the top. Pick yourself (or wherever you
want to fork the wiki) and wait for it to finish. Then, [clone your fork](https://services.github.com/on-demand/github-cli/clone-repo-cli) to your desktop. (Or wherever.)

## Step 2. Write the article

Our writing style guide is [here](style-guide.html).
Copy the template article (articles/template.md) and pick a good filename for your article. (For example, this article's filename
is "writing-for-neowiki.md".) Be unique enough that another article can't collide with your use of the filename.
Go to the part at the top, and change the part after "published" to "true". Replace "New Page" with the title of your article and the part after "description" to
a description of the article. (In the future, this will be used for OGP and smart embeds.)
If you have never written an article for us before, add your Neocities username to the config.ini file, in the "contributors" key.
That way, your name will be added to our contributor list.
After the second group of 3 dashes, write your article! Articles are Markdown format with no header links.
Save and commit your article when you finish it.

## Step 3. Submit the pull request!

Push your changes to your fork (done automatically for you if using GitHub on the web).
Go to your fork, to the branch where your article is, and follow [this guide to submit the pull request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/).
I will review your changes and let you know if anything needs to be changed. When all is good, the PR will be merged!
