---
title: "Лекция по GWT+mvp4g на ADDConf '11"
author: ["Anton Kotenko"]
draft: false
---

<div class="ox-hugo-toc toc has-section-numbers">

<div class="heading">Table of Contents</div>

- <span class="section-num">1</span> [План](#план)
- <span class="section-num">2</span> [Анонс](#анонс)

</div>
<!--endtoc-->

Буду читать мастер-класс на [ADDConf 2011](http://addconf.ru/) по разработке веб-приложений с помощью [GWT](http://code.google.com/webtoolkit/) и [mvp4g](http://code.google.com/p/mvp4g/) (29 апреля, 15:10). Санкт-Петербург, Россия

<div class="html">

&lt;center&gt;

</div>

{{< figure src="%7B%7B%20get_figure(slug,%20'firstslide.png')%20%7D%7D" caption="<span class=\"figure-number\">Figure 1: </span>Первый слайд презентации" >}}

<div class="html">

&lt;/center&gt;

</div>


## <span class="section-num">1</span> План {#план}

План на данный момент складывается такой:

1.  Введение. Краткая история и примеры использования GWT.
2.  Краткое описание концепций GWT
    1.  JSNI
    2.  Code Splitting
    3.  MVP, RMVP, EventBus
    4.  Deferred Binding
    5.  Dependency Injection
    6.  Remote Services
3.  mvp4g
    1.  Чем помогает, отличия и достоинства
    2.  Система аннотаций
    3.  Реализация RMVP, EventBus
    4.  History, `#!`
    5.  Мультимодульность
    6.  Замечания
4.  Компоненты в GWT
    1.  `UiBinder`, стандартные компоненты
    2.  Разработка каастомных компонентов
5.  Наша разработка Layouting-системы
6.  Работа с не-Java Server-Side API
7.  i18n в GWT
8.  Заключение. Ссылки на примеры

Будут рассказы о недостатках, можно будет обсудить опыт написания проектов на GWT (пример с моей стороны --- сайт [Experika](http://experika.com)) и тонкие моменты. Ещё не знаю, получится ли уложить всё это в полтора часа, возможно придётся от чего-то отказаться (от частей доклада, в пользу вопросов и обсуждений).

<div class="html">

&lt;center&gt;

</div>

{{< figure src="%7B%7B%20get_figure(slug,%20'add_logo.png')%20%7D%7D" caption="<span class=\"figure-number\">Figure 2: </span>Логотип ADDConf" >}}

<div class="html">

&lt;/center&gt;

</div>


## <span class="section-num">2</span> Анонс {#анонс}

Художественный анонс мастер-класса --- [здесь](http://addconf.ru/event.sdf/ru/add_2011/authors/AntonKotenko/313), цитирую:

> GWT - это библиотека инструментов от Google для написания сложных (и не очень) веб-приложений на Java с последующей трансляцией в качественно оптимизированный, кроссбраузерный JavaScript. В библиотеке обеспечена возможность создания декларативного пользовательского интерфейса, а также доступно множество готовых компонентов - от кнопок до разнообразных лэйаутов.

<!--quoteend-->

> Я расскажу о самой библиотеке GWT, о библиотеке mvp4g, значительно упрощающей работу по концепциям MVP и поддерживающей мульти-модульную архитектуру проекта, и о том как это сочетание используется в нашем текущем проекте, о наших достижениях, ошибках и опыте, который мы получили. Лекция, полагаю, будет интересна и тем, кто работает с GWT и тем, кто хочет подробнее ознакомиться с возможностями обоих библиотек на примере готового крупного проекта.

<!--quoteend-->

> В каждой части доклада я собираюсь рассказать и о достоинствах и о недостатках того или иного подхода, той или иной библиотеки. Также, если позволит время, постараюсь вкратце затронуть организационные моменты касающиеся разработки на GWT - о том, что нужно учитывать команде проекта при взаимодействии с GWT-разработчиками.

<!--quoteend-->

> Кстати, для разработчиков десктоп-приложений вход не менее свободный :).

Ещё собираюсь устроить там же Livecoding-сессию на [fluxus](http://www.pawfal.org/fluxus/), но это уже другая история, возможно о ней будет отдельно.


This text is auto inserted at the end of the exported Markdown.