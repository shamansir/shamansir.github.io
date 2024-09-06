---
title: "Occasional Textpattern Bug"
author: Anton Kotenko
draft: false
---

While I've played with [textpattern](http://textpattern.org/) at [sharecode](http://sharedcode.info/), I faced this issue that may come in touch with those who uses [textpattern](http://textpattern.org/).

I was frightened with the fact that commenting support in articles which were written too long ago was expired. I've searched over all of the preferences - nothing about this - but it is almost obvious that it must be. The good thing is that I've googled and found the [post](http://hari.literaryforums.org/2007/04/22/textpattern-review/), and through its comments I've reached the [FAQ article](http://textpattern.com/faq/257/comment-preferences-are-missing).

The mean is if in your _Admin_ -&gt; _Preferences_ -&gt; _Basic_ page for _Comments_ section you see only two points (and you have 4.0.4 version and no wish/ossibility to update currently) -- this article is for you.

You need to do just two actions. First - take `./textpattern/include/txp_prefs.php` file from your hosting, find a 89 line:

```php

$evt_list = safe_column('event', 'txp_prefs',
     "type = 0 and prefs_id = 1 group by 'event' order by event desc");
```

and to delete the quotes wrapping `event` to make it match with [this variant](http://dev.textpattern.com/browser/development/4.0/textpattern/include/txp_prefs.php?rev=2156#L89)):

```php

$evt_list = safe_column('event', 'txp_prefs',
     "type = 0 and prefs_id = 1 group by event order by event desc");
```

second -- redeploy the file back. Finita la comedia -- you're welcome in preferences, _Comments:Disabled after_.


This text is auto inserted at the end of the exported Markdown.
