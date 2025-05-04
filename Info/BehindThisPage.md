If you are wondering, this page is built by [Emanote].

Since I have started as a programmer, I loved to update my homepage design manually, there is the track of the last version at Webarchive: [2014-2021](https://web.archive.org/web/20210214045457/http://shamansir.github.io/) and also I have screenshots of every of five-or-six versions though time somewhere, I hope to include here some day.

Lastly I almost had no wish to do it, since I really got obsessed with the idea of keeping all my data organized in [Org-mode](https://orgmode.org/) and I was bothered with collecting and processing it. While I did it, [Obsidian] became very popular thing, but it is still built on #Markdown. For me, #org over #Markdown has tons of advantages:

* It supports different kinds of tasks out of the box and also showing progress for groups of them;
* It shows you your agenda as a calendar right in the editor; And it's a very useful agenda and it is rendered in text format in CLI;
* It treats all the `.org` files on your drive or in some folder, depends on your configuration, as one source of data, and so all the TODOs and tasks are there;
* It did all the things [Obsidian] does even before the Big Bang, and very probably was the inspiration for all the [Notion] and [Obsidian] etc.
* Its syntax is much more powerful and supports LaTeX and many things #Markdown lacks even nowadays;
* And many more...

_Still I currently write this page is in Markdown :)_. I was looking for some `orgmode`-based data/blog/site engine for _truly_ a lot. #Emacs and especially #Spacemacs are awesome and, as said, it is one of the advantages of `org` to have all these things close to your code, but I am still very bad in using #emacs or #vim and through my career I used mostly lightweight visual IDEs, while being a fan of text-mode. Anyway, I probably don't have to explain myself at my own homepage, yet I try using/learning #spacemacs every three months so once I could succeed.

My friend introduced me to his friend, who is a fan of #Nix and all functional stuff, like me, and that friend showed me #Logseq, which supports `org` files quite good, being written in Clojure. I was very happy and use it everyday now, it has its own issues, but now I can fill in my thoughs/tasks in `org` both on mobile and notebook and anywhere. I prefer it to #Obsidian, it also is free and open-source...

So I was trying [Hugo] first. It has nice themes, it is also written in Clojure, it supports `org` in some way. But its configuration and theming turned out not to be easy for me and while I really liked several themes but haven't found the matching one.

And yesterday, by searching something for #PureScript or #Haskell, I discovered the blog of [Emanote author]: [This one](https://srid.ca/generics-sop-intro). And both its' structure and look has triggered very pleasing emotions in me. And then I discovered that its engine [Ema] is written in #Haskell!! In background, I was already representing my data like [[Library]] or [[CV]] or a [[Talks|list of my Talks]] in ADTs in #PureScript to generate `org` or `json` or `CSV` from it, and it turned out that the idea of #Ema is the very same! The same day was the day I was learning #Nix, installing #Emanote works in #Nix as a single command, and #Emanote has GitHub Pages support from the box, and it supports `org`!!! It turned out Sridhar has similar passions to me and also started to love FP when it wasn't so hippie yet :). And so here we are!

[Ema]: https://ema.srid.ca/
[Emanote]: https://emanote.srid.ca/
[Emanote author]: https://srid.ca/cv
[Notion]: <https://notion.com>
[Obsidian]: https://obsidian.md/
