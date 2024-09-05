---
title: "Слайды мастер-класса по GWT и mvp4g"
author: Anton Kotenko
draft: false
---

<div class="ox-hugo-toc toc has-section-numbers">

<div class="heading">Table of Contents</div>

- <span class="section-num">1</span> [Слайды](#слайды)
- <span class="section-num">2</span> [План](#план)
- <span class="section-num">3</span> [Ссылки со слайдов](#ссылки-со-слайдов)
- <span class="section-num">4</span> [Вопросы](#вопросы)

</div>
<!--endtoc-->

29 апреля я читал мастер-класс по веб-разработке на [GWT](http://code.google.com/intl/ru/webtoolkit/) с использованием фреймворка [mvp4g](http://code.google.com/p/mvp4g/), на конференции [Application Developer Days](http://addconf.ru) 2011. Предоставляю вам слайды (видео должно быть позже).


## <span class="section-num">1</span> Слайды {#слайды}

[[[file:%7B%7B%20get_figure(slug,%20'gdocs.ru.png')%20%7D%7D](https://docs.google.com/viewer?a=v&pid=explorer&chrome=true&srcid=0B9lKUPDNyz1vYTViZjYwZTEtODNmNC00OWZlLWFhODUtMDNkYzE5N2NjM2Fk&hl=en)]]

[Также на Scribd](http://www.scribd.com/doc/54690967/)


## <span class="section-num">2</span> План {#план}

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


## <span class="section-num">3</span> Ссылки со слайдов {#ссылки-со-слайдов}

-   [Слайды в PDF](http://goo.gl/4GgnS)

-   Кратко о GWT

-   [Quake 2 в браузере](http://quake2-gwt-port.appspot.com)

-   Концепции GWT

-   [Статья про разницу MVC и MVP](http://geekswithblogs.net/kobush/archive/2006/01/09/65305.aspx)
-   [Ray Ryan про Архитектуру GWT-приложений](http://www.youtube.com/watch?v=PDuhR18-EdM)
-   [Видео про EventBus](http://tv.jetbrains.net/videocontent/gwt-event-bus-basics)
-   [Презентация по Deferred Binding](http://www.docstoc.com/docs/53396874/Deferred-Binding-The-Magic-of-GWT)
-   [Вики-страницы Guice](http://code.google.com/p/google-guice/wiki/Motivation?tm=6)
-   [Руководство по созданию Remote Services](http://developerlife.com/tutorials/?p=125)
-   [Обсуждение недостатков GWT](http://www.linux.org.ru/forum/talks/4497412)
-   [Резюме по оптимизации GWT-кода](http://galak-sandbox.blogspot.com/2010/10/gwt.html)

-   mvp4g

-   [Страница фреймворка mvp4g](http://code.google.com/p/mvp4g/)
-   [Showcase фреймворка mvp4g](http://mvp4gshowcase.appspot.com)
-   [Сравнение GWT и фреймворка mvp4g](http://code.google.com/p/mvp4g/wiki/Mvp4g_vs_GWTP)
-   [Небольшой туториал по созданию проекта на mvp4g](http://cambiatablog.wordpress.com/2010/12/04/gwt-and-mvp4g-tutorial-1/)

-   UI компоненты

-   [Библиотека компонентов GWT](http://code.google.com/webtoolkit/doc/latest/RefWidgetGallery.html)

-   Layouting

-   [Демонстрация Layouting (в процессе) на GWT+mvp4g](http://github.com/shamansir/gwt-mvp4g-layouting-demo)

-   Non-Java API

-   [Суть](http://code.google.com/p/google-web-toolkit-doc-1-5/wiki/GettingStartedJSON)
-   [Описание с исходным кодом](http://shamansir-ru.tumblr.com/post/1728720550/deferred-api-gwt-rpc)

-   i18n
-   Заключение

-   [Сайт Experika](http://experika.com)
-   [Твиттер Виталия Гашка](http://twitter.com/vgashock)
-   [Сайт Михаила Кашкина](http://www.vurt.ru)
-   [Сайт компании EmDev](http://emdev.ru)
-   [Мой Google-профиль](http://profiles.google.com/shaman.sir)


## <span class="section-num">4</span> Вопросы {#вопросы}

Во время презентации задавали вопросы, из которых я выделил самые важные:

**Для каких сайтов подходит GWT?**

По текущему состоянию, значительное расширение функциональности стандартных компонентов GWT вручную или добавление новых компонентов практически неизбежно ведёт к потере сразу нескольких достоинств GWT --- кроссбраузерности и системы переопределения стилей: эти компоненты придётся отлаживать и верстать в различных браузерах самостоятельно.

Поэтому, самое очевидное применение GWT --- сайты, где удобство пользователя достигается засчёт _существующей_ компонентной базы и \_не_изощрённого дизайном интерфейса (например, подобные [Google Groups](http://groups.google.com)).

Это больше _прикладные_ сайты, чем красивые. У таких сайтов часто вся функциональность происходит на одной странице, а не на нескольких. Нельзя сказать, что всё обратное --- невозможно: возможно, и примером служит [наш сайт](http://experika.com/ui/#!job/start), но всё это стоит намного больших трудов, чем использование стандартных компонентов и подходов. Однако, при всём при этом, для других UI-фреймворков упомянутое верно даже в большей степени, чем для GWT (то есть с использованием Apache Wicket сложнее сделать сложный красивый сайт, чем с использованием GWT).

**Как работать с дизайнерами и верстальщиками при разработке сайта на GWT?**

Дизайнерам надо дать установку либо на подавляющее использование стандартных компонентов/лэйаутов GWT в дизайне, либо на кропотливую разработку собственной библиотеки виджетов.

В первом случае вёрстка может даже не понадобиться (дизайн на страницы смогут наложить GWT-разработчики), во втором случае сдизайненную библиотеку виджетов верстальщикам придётся верстать кроссбраузерно, при этом верстальщиков придётся (очень желательно) учить лэйаутам GWT, системе CSS-стилей в GWT, концепциям виджето-ориентированного декларативного UI и структуре gwt.xml.

Как более худший вариает, верстальщики могут верстать виджеты в HTML (но всё равно, каждый виджет по отдельности), а GWT-разработчики "накладывать" эту вёрстку на виджеты, уже в стиле GWT. Но это, и правда, _худший_ вариант.

<div class="html">

&lt;/dd&gt;

</div>

**Как связаны понятия модулей в GWT и mvp4g?**

На практике модуль в GWT --- это чаще либо отдельная библиотека, либо веб-приложение целиком, либо его крупная часть. Модуль в mvp4g --- это более атомарное понятие, например один модуль mvp4g полностью отвечает за работу с пользователями, второй модуль --- за работу с новостями, третий --- за работу с компаниями. При этом модуль mvp4g подразумевает одну шину событий для модуля, один `HistoryConverter` и несколько презентеров и вьюх внутри. См. тж. [демонстрацию Layouting (в процессе)](http://github.com/shamansir/gwt-mvp4g-layouting-demo).

То есть в модуль mvp4g рекомендуется выделять работу с одним типом _сущностей_, в котором шина событий будет отвечать за _действия_ с этим типом сущностей.

В этом есть огромное преимущество, потому что модули mvp4g можно загружать асинхронно (_Code Splitting_) --- если пользователь не работает с какой-либо сущностью, эта часть JavaScript-кода даже не будет загружена в его браузер.

**Как устроена система навигации в фреймворке mvp4g?**

Из ответа на предыдущий вопрос сделаем вывод --- поскольку в модуль mvp4g рекомендуется выделять работу с одним типом сущностей и такой модуль имеет один `HistoryConverter`, предпочтительнее строить систему навигации по той же логике `сущность -> действие`, например:

```text
user/edit?56 // или user/edit/56, mvp4g позволяет это
user/show?56 // или user/show/56
user/friends?56 // или user/friends/56
user/list
company/edit?72 // или company/edit/72
company/show?72 // или company/show/72
company/employee?72 // или company/employee/72
company/list
```

Можно строить систему на URL вида `user/56/edit`, принимая в HistoryConverter `id` сущности и действие и в зависимости от действия вызывать соответствующее событие.

Это всё рекомендации, mvp4g на данный момент никак не ограничивает разработчика в разбиении кода на модули или способах формирования URL.

**Концепция MVP подразумевает лёгкое тестирование. Тестируем ли мы UI и как тестируется mvp4g?**

На данный момент мы тестируем UI вручную (тестеры ходят по сайту и проверяют функциональность). Фреймворк mvp4g позволяет использовать JUnit точно так же, как и для GWT --- то есть никак не ограничивает. Вы всё также можете тестировать `Presenter` как обычный класс, для моков можно использовать библиотеку [mockito](http://mockito.org/). Кроме того, каждый `Presenter` имеет методы `setView` и `setEventBus`, поэтому вы можете инжектить mock-view и mock-eventbus используя GIN ([обсуждение здесь](http://groups.google.com/group/mvp4g/browse_thread/thread/82cac05eabe2401b)).

Практического опыта в таком тестировании у нас нет, возможно кто-то опишется в комментариях по этому поводу.


This text is auto inserted at the end of the exported Markdown.
