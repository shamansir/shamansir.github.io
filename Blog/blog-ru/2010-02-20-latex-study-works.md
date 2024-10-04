---
title: "Подготовка учебных документов в LaTeX"
author: Anton Kotenko
publishDate: 2010-02-20T23:54:00
draft: false
---

<div class="ox-hugo-toc toc has-section-numbers">

<div class="heading">Table of Contents</div>

- <span class="section-num">1</span> [Установка](#установка)
- <span class="section-num">2</span> [Титульная страница](#титульная-страница)
- <span class="section-num">3</span> [Схемы](#схемы)
- <span class="section-num">4</span> [Пакеты pgf](#пакеты-pgf)
    - <span class="section-num">4.1</span> [Таблицы](#таблицы)
    - <span class="section-num">4.2</span> [Графики](#графики)
- <span class="section-num">5</span> [Заключение](#заключение)

</div>
<!--endtoc-->

В этой статье я вкратце расскажу об общих способах при подготовке различных учебных документов в LaTeX, а конкретно - о подготовке титульной страницы, вставке векторных рисунков (схем), вставке таблиц и вставке графиков, создающихся на основе подготовленных данных, занесённых или даже вычисляемых в электронной таблице.

Процесс будет рассматриваться со стороны Ubuntu/TeX Live, хотя всё рассказанное можно будет сделать и в Windows с использованием MikTeX и на Маке с использованием MacTeX. Также я затрону дополнительные open-source пакеты (версии которых, опять же, есть для всех операционных систем), которые помогут в процессе и опишу какие действия необходимо предпринять, чтобы получившийся в результате документ выглядел максимально близко к желаемому :). Это [Inkscape](http://www.inkscape.org), [Gnumeric](http://www.gnome.org/gnumeric) и пакеты [`pgfplots`](http://pgfplots.sourceforge.net) и [`pgfplotstable`](http://pgfplots.sourceforge.net) для LaTex.

Если вы в первый раз используете LaTeX, рекомендую стандартный [вводный документ](http://www.rpi.edu/dept/arc/docs/latex/latex-intro.pdf) _(англ., PDF)_ и небольшой [справочник по форматированию текста](http://en.wikibooks.org/wiki/LaTeX/Formatting) _(англ.)_. В качестве документации к `pgfplots` подойдёт официальная: [`pgfplots`](http://pgfplots.sourceforge.net/pgfplots.pdf) _(англ., PDF)_, [pgplotstable](http://pgfplots.sourceforge.net/pgfplotstable.pdf) _(англ., PDF)_.


## <span class="section-num">1</span> Установка {#установка}

Устанавливаем LaTeX:

```text
$ sudo apt-get install tex-common texlive-base texlive-base-bin texlive-common \
texlive-doc-base texlive-fonts-recommended texlive-lang-cyrillic \
texlive-latex-base texlive-latex-recommended
```

Создадим тестовый документ в любом редакторе (для `gedit` вы можете установить `gedit-latex-plugin`). Условимся, что наш основной документ будет называться `work_0001_2010.tex`, а все относящиеся к нему файлы будут использовать это название + какой-либо постфикс:

```text
$ touch ./work_0001_2010.tex
$ gedit ./work_0001_2010.tex
```

Вставим представленный тект в качестве содержимого, сохраним:

```latex

\documentclass[a4paper,12pt]{article}
\usepackage[T2A]{fontenc}
\usepackage[utf8]{inputenc} % любая желаемая кодировка
\usepackage[russian,english]{babel}
\usepackage[pdftex,unicode]{hyperref}
\usepackage{indentfirst} % включить отступ у первого абзаца

\title{Заголовок документа}
\author{Имя автора}
\date{02/2010}

\begin{document} % начало документа

\maketitle % заголовок

Тестовый документ, подготовленный в \LaTeX
\end{document} % конец документа
```

Скомпилируем и посмотрим, что получилось:

```text
$ pdflatex ./work_0001_2010.tex
$ evince ./work_0001_2010.pdf
```

Если всё было сделано правильно - перед нами готовый результат.


## <span class="section-num">2</span> Титульная страница {#титульная-страница}

Итак, генерируемая по умолчанию страница обычно не соответствует тому, что ожидают преподаватели или ученики. Я просто покажу шаблон и то, что должно из него получиться - результат больше похож на ожидания, но конечно, при желании или необходимости, вы можете изменить его как заблагорассудится.

```latex

\begin{document} % начало документа

\begin{titlepage} % начало титульной страницы

\begin{center} % включить выравнивание по центру

\large Российский технический институт <<ACME-ТЕХ>>\\[4.5cm]
% название института, затем отступ 4,5см

\huge Теоретическая работа \No 5\\[0.6cm] % название работы, затем отступ 0,6см
\large по~теме <<Хабраобщество. Внутреннее и внешнее влияние>>\\[3.7cm]
% тема работы, затем отступ 3,7см

\begin{minipage}{0.5\textwidth} % начало маленькой врезки в половину ширины текста
\begin{flushleft} % выровнять её содержимое по левому краю
\emph{Автор:} Цокотуха~Флай\\
\emph{Группа:} 7822\\
\emph{Факультет:} МХХПХХ\\
\emph{Преподаватель:} Шаманова~Эллина~Канделябровна
\end{flushleft} % конец выравнивания по левому краю
\end{minipage} % конец врезки

\vfill % заполнить всё доступное ниже пространство

{\large \today} % вывести дату
{\large \LaTeX} % вывести логотип LaTeX

\end{center} % закончить выравнивание по центру

\thispagestyle{empty} % не нумеровать страницу
\end{titlepage} % конец титульной страницы

\tableofcontents % содержание

\section{Глава I}
\section{Глава II}
\section{Глава III}
\section{Глава IV}

Тестовый документ, подготовленный в \LaTeX
\end{document} % конец документа
```

Содержание включено для примера и оно обновится в соотвествии с главами только при следующей компиляции - это правило для LaTeX. В результате всё это должно выглядеть так:

{{< figure src="%7B%7B%20get_figure(slug,%20'latex_habr_titlepage.png')%20%7D%7D" caption="<span class=\"figure-number\">Figure 1: </span>Титульная страница" >}}


## <span class="section-num">3</span> Схемы {#схемы}

Есть много способов вставить изображение в LaTeX-документ, и вам подойдёт любой из них, но так как я обо всём рассказываю, то должен рассказать хотя бы об одном. Я подготавливаю схемы в [Inkscape](http://www.inkscape.org) (свободный векторный редактор), экспортирую их в PDF и затем вставляю в LaTeX-документ.

Inkscape очень удобен для подготовки схем - у прямых линий (да и у фигур и кривых) можно установить с любых концов стрелки или сделать их пунктирными (Object -&gt; Fill and Stroke -&gt; Stroke Style), сектора можно делать ограничивая углы развёртки у круга, любую фигуру можно залить стандартными для таких схем кистями (хоть в полька-точечку (Object -&gt; Fill and Stroke -&gt; Fill Style -&gt; Polka dots)), кривые удобно рисовать инструментом Кривая Безье и кроме всего прочего есть "примагничивание" (правда оно почему-то включается в свойствах документа (File -&gt; Document Properties -&gt; Snap)). Практически любой график или схему из методички/учебника можно перенести в векторный вид за полчаса.

Итак, экспорт из Inkscape. Исходный файл, по принятому ранее соглашению, назовём `work_0001_2010_graph01.svg`

В меню File -&gt; Save as... выберем формат \*.pdf:

{{< figure src="%7B%7B%20get_figure(slug,%20'latex_habr_graph01_save.png')%20%7D%7D" caption="<span class=\"figure-number\">Figure 2: </span>Сохранение в PDF" >}}

И отметим конвертацию шрифтов в пути (в Stroke Style -&gt; Width у надписей советую ставить значения 0.1-0.3, иначе надписи в pdf-файле получаются очень толстыми):

{{< figure src="%7B%7B%20get_figure(slug,%20'latex_habr_graph01_pdf.png')%20%7D%7D" caption="<span class=\"figure-number\">Figure 3: </span>Опции экспорта в PDF" >}}

Теперь в шапку LaTeX-документа наряду с остальными пакетами нужно добавить пакет `graphicx`:

```latex

\usepackage{graphicx}
```

А в тело документа вставить новую картинку:

```latex

\newpage
```

Картинка:

```latex

\begin{figure}
\centering
\includegraphics[width=0.9\textwidth]{work_0001_2010_graph01.pdf}
\caption{Преломление света}
\label{fig:graph01}
\end{figure}
```

Заново компилируем:

```text
$ pdflatex ./work_0001_2010.tex
$ evince ./work_0001_2010.pdf
```

И вот результат:

{{< figure src="%7B%7B%20get_figure(slug,%20'latex_habr_graph01_inside.png')%20%7D%7D" caption="<span class=\"figure-number\">Figure 4: </span>SVG-картинка в PDF" >}}


## <span class="section-num">4</span> Пакеты pgf {#пакеты-pgf}

Пакет `pgfplotstable` помогает очень гибко настраивать/составлять таблицы и позволяет считывать таблицу из csv-файла при компиляции.

Пакет `pgfplots` позволяет строить практически любые цветные настраиваемые графики на основе таблиц.

Установка пакетов на Windows/MikTex описана в [документации](http://pgfplots.sourceforge.net/pgfplots.pdf) _(англ., PDF)_ , в случае Ubuntu нужно сделать следующее:

```text
$ sudo nano /etc/apt/sources.list
```

В конец файла добавить (заменять версию `lucid` на вашу не нужно):

```text
deb http://ppa.launchpad.net/johannes-reinhardt/ppa/ubuntu lucid main
```

Выполнить:

```text
$ sudo apt-get update
$ sudo apt-get install pgfplots
```


### <span class="section-num">4.1</span> Таблицы {#таблицы}

Таблицы будем подготавливать в [Gnumeric](http://www.gnome.org/gnumeric). Можно использовать любой табличный редактор, главное - гибкая возможность экспорта в текстовый вид.

Создадим таблицу, в первых трёх столбцах которой будут различные значения, а в четвёртом столбце - среднее по этим трём значениям и сохраним её под именем `work_0001_2010_table01.gnumeric` (кстати, gnumeric умеет сохранять таблицы в формате LaTeX, но мы намереваемся использовать пакет `pgfplotstable`, поэтому не будем этого делать):

{{< figure src="%7B%7B%20get_figure(slug,%20'latex_habr_table01_save.png')%20%7D%7D" caption="<span class=\"figure-number\">Figure 5: </span>Сохранение gnumeric-таблицы" >}}

Теперь необходимо экспортировать таблицу в текстовый файл. Важно заметить две вещи, первая: в текстовый файл импортируется только текущий лист (Sheet), вторая: для того, чтобы удобно работать со столбцами при использовании пакета `pgfplotstable`, необходимо в первой строке таблицы указать короткие однословные названия (алиасы) для столбцов.

Таблицу можно сохранить в CSV, но если вы используете русскую локаль в операционной системе, то дробные числа в таблице будут представлены с использованием запятой. Так что лучше сохраним файл в формате Text (configurable), а назовём его, для удобства, `work_0001_2010_table01.dat`

{{< figure src="%7B%7B%20get_figure(slug,%20'latex_habr_table01_savecsv.png')%20%7D%7D" caption="<span class=\"figure-number\">Figure 6: </span>Сохранение таблицы в CSV" >}}

После этого вас спросят о дополнительных настройках - символ конца строки установите в соответствии с вашей операционной системой, разделитель - "пробел" и отключите кавычки.

{{< figure src="%7B%7B%20get_figure(slug,%20'latex_habr_table01_export.png')%20%7D%7D" caption="<span class=\"figure-number\">Figure 7: </span>Параметры экспорта для CSV" >}}

В результате должен получиться такой файл:

```text

a b c mid
0.09 0.07 0.072 0.0773333333333333
0.15 0.073 0.073 0.0986666666666667
0.155 0.074 0.8 0.343
0.156 0.078 0.9 0.378
0.17 0.079 0.99 0.413
0.18 0.08 0.1 0.12
0.189 0.09 0.12 0.133
0.192 0.1 0.14 0.144
0.195 0.12 0.153 0.156
0.2 0.128 0.16 0.162666666666667
```

Теперь можно вставить таблицу в LaTeX-документ. Добавьте в заголовок:

```latex

\usepackage{pgfplotstable}
```

Теперь, в теле документа, настроим вывод у пакета pgf (запятые в качестве дробных разделитей, округление до шести знаков) и загрузим файл с данными, привязав его к алиасу `midvalues`:

```latex

\pgfkeys{/pgf/number format/.cd,precision=6,use comma,fixed,1000 sep={}}

\pgfplotstableread{work_0001_2010_table01.dat}\midvalues
```

Теперь опишем саму таблицу:

```latex

\newpage

Таблица

\begin{table}[h]
\centering
\caption{Средние числа}
\pgfplotstabletypeset[
    columns={a,b,c,mid},  % алиасы колонок, определённые в первой строке таблицы
    columns/a/.style={ column name=Значение $a$ }, % стиль столбца: определяем только заголовок
    columns/b/.style={ column name=Значение $b$ }, % стиль столбца: определяем только заголовок
    columns/c/.style={ column name=Значение $c$ }, % стиль столбца: определяем только заголовок
    columns/mid/.style={ column name=Среднее значение }, % стиль столбца: определяем только заголовок
    every head row/.style={ before row=\hline, after row=\hline\hline }, % одиночная линия над и двойная линия под первой строкой таблицы
    every last row/.style={ after row=\hline }, % одиночная линия под последней строкой таблицы
    every first column/.style={
        column type/.add={|}{} % вертикальная линия перед первым столбцом
    },
    every last column/.style={
        column type/.add={|}{|} % вертикальные линии с обоих сторон последнего столбца
    }
]\midvalues \\[0.5cm]
\label{tab:midvalues}
\end{table}
```

Снова перекомпилируем файл, и вот результат:

{{< figure src="%7B%7B%20get_figure(slug,%20'latex_habr_table01_rendered.png')%20%7D%7D" caption="<span class=\"figure-number\">Figure 8: </span>Как выглядит таблица" >}}


### <span class="section-num">4.2</span> Графики {#графики}

В завершение построим график по данной таблице.

Добавьте в заголовок документа:

```latex

\usepackage{pgfplots}
\pgfplotsset{compat=newest} % использовать новые возможности pgfplots
```

И, в тело документа:

```latex

\newpage

\begin{tikzpicture}
    \begin{axis}[ % начать график
        xlabel=Измерение, % метка для оси x
        ylabel=Значение, % метка для оси y
        xtick align=center, % риски оси x внутри графика
        yminorgrids, ymajorgrids, % линии для основных и второстепенных значений по оси y
        xmajorgrids, % линии для основных значений по оси x
        minor y tick num=4, % 4 второстепенных риски между каждыми основными рисками по оси y
        legend style={at={(0.74,0.74)}, anchor=south west} % позиционирование легенды относительно нижнего левого угла
    ],
    \addplot[green!40!black,mark=x] table[y=a] from \midvalues; % тёмно-зелёным отметить данные из столбца 'a' таблицы midvalues на оси
    \addlegendentry{$a$ (таб. \ref{tab:midvalues})} % добавить линию на легенду
    \addplot[red!60!black,mark=x] table[y=b] from \midvalues; % тёмно-красным отметить данные из столбца 'b' таблицы midvalues на оси
    \addlegendentry{$b$ (таб. \ref{tab:midvalues})} % добавить линию на легенду
    \addplot[yellow!80!black,mark=x] table[y=c] from \midvalues; % тёмно-жёлтым отметить данные из столбца 'c' таблицы midvalues на оси
    \addlegendentry{$c$ (таб. \ref{tab:midvalues})} % добавить линию на легенду
    \addplot[blue!80!black,mark=o,smooth] table[y=mid] from \midvalues; % тёмно-синим сглаженной линией отметить данные из столбца 'mid' таблицы midvalues на оси
    \addlegendentry{Среднее (таб. \ref{tab:midvalues})}  % добавить линию на легенду
    \end{axis}
\end{tikzpicture}
```

Мы указываем только значения для оси y и pgf автоматически подбирает значения на оси x, но в команде `addplot` также можно указать и столбец-источник для оси x: `table[x=mid,y=b]`

Снова перекомпиляция, и теперь мы видим отличный график-за-пять-минут по нашим значениям (значения я подбирал наугад, поэтому выглядят они не очень удачно (чуть лучше на графике с логарифмическими осями, однако задание сделать его таковым я лучше оставлю вам на дом), но надеюсь суть понятна).

{{< figure src="%7B%7B%20get_figure(slug,%20'latex_habr_plot01_rendered.png')%20%7D%7D" caption="<span class=\"figure-number\">Figure 9: </span>Как выглядит график" >}}

Я привёл лишь простейший пример, но пакет `pgfplots` обладает настолько широкими возможностями, что если вы заинтересованы в данной теме, то вы просто обязаны хотя бы очень подробно рассмотреть всё [руководство по пакету](http://pgfplots.sourceforge.net/pgfplots.pdf) _(англ., PDF)_.


## <span class="section-num">5</span> Заключение {#заключение}

Итак, LaTeX и `pgfplots` - удобный способ оформлять не только текстовые документы с формулами, но и целые работы со схемами, графиками и таблицами. Причём делать их просто и удобно. Желаю вам большого количества полезных и легко созданных научных работ!


This text is auto inserted at the end of the exported Markdown.
