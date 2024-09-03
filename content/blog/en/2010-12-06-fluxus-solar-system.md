---
title: "Modelling a Solar System in Fluxus"
author: ["Anton Kotenko"]
draft: false
---

<div class="ox-hugo-toc toc has-section-numbers">

<div class="heading">Table of Contents</div>

- <span class="section-num">1</span> [Sources](#sources)
- <span class="section-num">2</span> [Description](#description)
- <span class="section-num">3</span> [Examining code](#examining-code)
- <span class="section-num">4</span> [Videos](#videos)

</div>
<!--endtoc-->

Some time ago I&nbsp;[^fn:1] about [fluxus](http://www.pawfal.org/fluxus/), livecoding and 3D-prototyping system. Now I want to demonstrate some of its features and describe how you may use them in pseudo(;))scientific needs. For example, you can create a model of a simplified solar system and make it fit in only 125 lines of code (including comments) -- it is the advantage of [Racket](http://racket-lang.org/) language with graphic steroids, the core of fluxus and a descendant of PLT Scheme. Here how the result will look like:

[[[file:%7B%7B%20get_figure(slug,%20'screen04-thumb.png')%20%7D%7D](%7B%7B%20get_figure(slug,%20'screen04.png')%20%7D%7D)]]

[[[file:%7B%7B%20get_figure(slug,%20'screen05-thumb.png')%20%7D%7D](%7B%7B%20get_figure(slug,%20'screen05.png')%20%7D%7D)]]

There are sources in the post, a short desription of code structure, tutorial movies in Slavic English, examining in detail the whole process of writing this complicated (;)) code.


## <span class="section-num">1</span> Sources {#sources}

[HERE](http://paste.pocoo.org/show/301220/)

> Note: Since it was lost with the Poocoo, I'll try to restore it from video.


## <span class="section-num">2</span> Description {#description}

Fluxus uses a term of state machine for scene construction. If you have programmed in OpenGL already, you are familiar with this principle - every next function in the code either modifies the matrix of scene state or changes the content of the scene (i.e. draws an object). You may construct the required scene objects just before any rendering will happen and then change their conditions later or just draw a new primitives in every frame (OpenGL understands that it may cache the objects which state is not changed a lot between frames). I am using the both ways of these, so I prepare the text labels and planets' orbits before rendering process but I draw planets in every new frame.

I have taken all the data about equatorial diameters, orbital radiuses and orbital periods of the planets from the single one table in [Wikipedia article](http://en.wikipedia.org/wiki/Planet#Solar_System). It is very handy that all parameters are presented relatively to Earth properties (that is how astronomical units are calculated), so the Earth diameter and Earth year can be used as system of units in our model.

> Do you know that distance from mass center of Earth to mass center of Sun is approximately equal to 11740 Earth diameters? It is the astronomical unit (`astro-unit` constant) and the distances from Sun to planets are measured relativey to it. And more, 109 Earth diameters fits the diameter of Sun (the Earth diameter is represented with `diameter-factor` constant in the model).

When we know this data, we can calculate the angles for planets positions (the orbital eccentricities are not taken in account in the model, it's a homework) and place them appropriately in the model.


## <span class="section-num">3</span> Examining code {#examining-code}

-   `star`, `planet` and planetary system (it is called `star-system` because the center of it is a star), consisting of star and planets, structures are defined
-   defined functions of
    -   getting translate vector (`qtv` - _quick translate vector_) for planet using its orbital radius and orbital period
    -   getting scale vector (`qsv` - _quick scale vector_) of planet using its diameter
    -   fast calculation of planet position angle (`curang`), relatively to (Sun) (0, 0) point, using planet's orbital period
    -   building orbit primitive (`build-orbit`) using its orbital radius
    -   building label primitive (`qto` - \_quick text object\`) for planet using the passed string
-   the star of Sun is created, planets and all of them are put into "solar system" instance (`solar-system`). while filling planets structures, the labels primitives are built for each one.
-   using the planets data the orbits are built
-   functions are defined
    -   `draw-star`, it draws a star
    -   `draw-planet`, it draws a planet in the required position depending on current time and moving the text label in the same position
-   `render` function is defined, it draws sun and planets one by one, calling `draw-star` and `draw-planet`
-   `render` is assigned to be a function executed for each frame


## <span class="section-num">4</span> Videos {#videos}

<div class="html">

&lt;iframe src="<http://player.vimeo.com/video/17502661>" width="400" height="300" frameborder="0"&gt;

</div>

<div class="html">

&lt;/iframe&gt;

</div>

<div class="html">

&lt;p&gt;

</div>

Fluxus Livecoding: Building 3D Solar System / Part 1 from Ulric Wilfred on Vimeo.

<div class="html">

&lt;/p&gt;

</div>

<div class="html">

&lt;iframe src="<http://player.vimeo.com/video/17515694>" width="400" height="300" frameborder="0"&gt;

</div>

<div class="html">

&lt;/iframe&gt;

</div>

<div class="html">

&lt;p&gt;

</div>

Fluxus Livecoding: Building 3D Solar System / Part 2 from Ulric Wilfred on Vimeo.

<div class="html">

&lt;/p&gt;

</div>

<div class="html">

&lt;iframe src="<http://player.vimeo.com/video/17516078>" width="400" height="300" frameborder="0"&gt;

</div>

<div class="html">

&lt;/iframe&gt;

</div>

<div class="html">

&lt;p&gt;

</div>

Fluxus Livecoding: Building 3D Solar System / Part 3 from Ulric Wilfred on Vimeo.

<div class="html">

&lt;/p&gt;

</div>

[^fn:1]: Located here: <./post-about-fluxus>

This text is auto inserted at the end of the exported Markdown.
