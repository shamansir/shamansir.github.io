---
title: "Easy as Sandwich: Blog Engine in JavaScript and XML"
author: ["Anton Kotenko"]
draft: false
---

<div class="ox-hugo-toc toc has-section-numbers">

<div class="heading">Table of Contents</div>

- <span class="section-num">1</span> [Picture](#picture)
- <span class="section-num">2</span> [Components](#components)
- <span class="section-num">3</span> [Receipt](#receipt)
- <span class="section-num">4</span> [Advantages](#advantages)
- <span class="section-num">5</span> [Disadvantages](#disadvantages)
- <span class="section-num">6</span> [May be later](#may-be-later)
- <span class="section-num">7</span> [Example](#example)
- <span class="section-num">8</span> [Source code](#source-code)

</div>
<!--endtoc-->

Say you suddenly needed a personal blog. I already have some puny free hosting, and it hosting is puny for real, so it has no PHP and it even has no possibilities to set up any server-side at all. Or even worse, you have only a Dropbox account and in this very moment, suddenly, the personal blog is needed.

And more, may be you prefer to write you posts in Markdown-syntax instead of writing a heavy sad posts using dull HTML. The more, Markdown is now supported at a lot of places (excluding MSDN articles, may be). And there wouldn't be out of place to store separate posts in separate files, so you can take one and copy-paste it in Tumblr or somewhere else. And it gives you a possibility to push files in some repository and to make your articles versioned this way...

And more, you'd like to have two versions of your blog in one entry point. English and russian, for example.

I think you now feel what I mean: I have a proposal for you abou this all. It'd be better to give more than one link already but I am an evil geek so I'll put one in the end of article.


## <span class="section-num">1</span> Picture {#picture}

{{< figure src="%7B%7B%20get_figure(slug,%20'screenshot-small.png')%20%7D%7D" caption="<span class=\"figure-number\">Figure 1: </span>Screenshot" >}}


## <span class="section-num">2</span> Components {#components}

-   [JQuery](http://jquery.com), for bread
-   [Showdown](http://www.attacklab.net/showdown/), for a sausage
-   And a dates parser for a mustard

Not to make things to hard, I've taken [JQuery](http://jquery.com) (I use only DOM-operations and a helper to load XML files asynchronously from it, so for the cruel need it can be accurately excised). Then I've taken [Showdown](http://www.attacklab.net/showdown/), it is Markdown syntax parser moved to JavaScript. Then I've taken some strange dates parser (to display them nicely). And I've mixed all these stuff into one solid thing, so I've got a crazy little thing called JS/XML-driven blog engine. Easy as sandwich.


## <span class="section-num">3</span> Receipt {#receipt}

To write your first post in a blog, get [this package](http://code.google.com/p/showdown-blog/downloads/detail?name=swblog.zip), unpack. Update your preferences (`prefs.xml`), create some post (`posts/<post-id>.xml`), add `<post-id>` in `posts.xml`. That's all, you're ready, post is published. For the next posts just repeat only last two steps. (In `./create.html` you'll find an editor that is ripped out from Showdown, and it will help your phantasy to imagine what Markdown-syntax parsing result will look like).

Now, once more

1.  Set up ising `prefs.xml`
2.  Put `some-post.xml` in `posts` directory
3.  Add `some-post` to `posts.xml`
4.  Repeat steps 2 and 3 for next posts


## <span class="section-num">4</span> Advantages {#advantages}

-   Minimalism.
-   No server side. At all.
-   Posts are written with Markdown-syntax.
-   One post - one XML file
-   Configuration-over-XML
-   Styles-over-CSS
-   Tags, tags cloud and tags navigation
-   Permalink for every post
-   Supports mobile browsers (some)
-   Several entry-points are supported
-   RSS-generating script is included out-of-the-box


## <span class="section-num">5</span> Disadvantages {#disadvantages}

-   No commenting support
-   No indexing with search engines
-   Only for JavaScript-powered browsers
-   Javascript and JQuery sometimes go slowly in slow networks
-   If you have no `.htaccess`, user must name `index.html` explicitly
-   Things to optimize


## <span class="section-num">6</span> May be later {#may-be-later}

-   Paging
-   Templates support
-   More Nice RSS / RSS Automation
-   Calendar


## <span class="section-num">7</span> Example {#example}

[Path to example](http://showdown-blog.googlecode.com/hg/index.html)


## <span class="section-num">8</span> Source code {#source-code}

[Googlecode project](http://showdown-blog.googlecode.com/)

**Upd.** Advantages and disadvatages had a bit changed through time, visit the project page to see how exactly they've changed.


This text is auto inserted at the end of the exported Markdown.
