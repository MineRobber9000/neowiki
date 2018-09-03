---
author: dotcomboom
published: true
title: Neocities CLI
description: Neocities' command line interface.
---

The [Neocities CLI](https://neocities.org/cli) is a utility written in the Ruby programming language to interface with the Neocities API from a terminal. It allows a website to be managed entirely through the console, without a web browser.

## Installation
The Neocities CLI runs on any platform with [Ruby and its Gem package manager](https://www.ruby-lang.org/en/downloads/) installed. Run `gem install neocities` and it will install. 

In the case of macOS or Linux users, the page on Neocities' website advises to run it with `sudo` if there are permissions issues. If the installation has an error about `rake` not being installed, run `gem install rake` before trying again.

## Usage
Using any of the Neocities CLI's functions will prompt you to enter your site's username and password. After this, it will store the API key and you won't need to enter it again.

A full list of the CLI's functions can be found by just typing `neocities` into the terminal.

If you have an existing site, you may want to download and extract it first through the Neocities dashboard, so you can jump into editing right away.

You can push the entire directory to your site by going to the folder and running `neocities push .`.

Additionally, you can upload files (`neocities upload`), delete files (`neocities delete`), list your files (`neocities list`), get stats (`neocities info`), or log out (`neocities logout`).

The Neocities CLI's specialty feature, though, is its pizza delivery service, which can be accessed through `neocities pizza`. Every time I've tried, they've been out of dough.. but hey, it's worth a shot.

## External Links
- [Neocities - Cli](https://neocities.org/cli) - The page on Neocities' site about the CLI.
- [neocities/neocities-ruby](https://github.com/neocities/neocities-ruby) - The Github repository for the CLI.
- [neocities/neocities-ruby - pizza](https://github.com/neocities/neocities-ruby/search?q=pizza&unscoped_q=pizza) - Proof that fat head pizza crust doesn't exist
