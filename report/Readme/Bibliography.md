# Библиография

* [Общие замечания](#Общие-замечания)
* [Назначение и размещение файлов с библиографией](#Назначение-и-размещение-файлов-с-библиографией)
* [Настройка библиографии](#Настройка-библиографии)
  * [Группированные подсписки литературы (ВАК, Web of Science и т.п.)](#Группированные-подсписки-литературы-ВАК-web-of-science-и-тп)
    * [В автореферате](#В-автореферате)
    * [В тексте диссертации](#В-тексте-диссертации)
    * [Выбор групп для отображения](#Выбор-групп-для-отображения)
    * [Наименование списков и подсписков литературы](#Наименование-списков-и-подсписков-литературы)
  * [Строгость соответствия ГОСТ](#Строгость-соответствия-ГОСТ)
* [Замечания по реализациям библиографии](#Замечания-по-реализациям-библиографии)
  * [`biblatex` + `biblatex-gost` + biber](#biblatex--biblatex-gost--biber)
  * [Встроенная + `gost` + bibtex](#Встроенная--gost--bibtex)
    * [ugost2008mod.bst](#ugost2008modbst)
* [Список статей в презентации](#Список-статей-в-презентации)
* [Дополнительная информация](#Дополнительная-информация)
* [В случае проблем](#В-случае-проблем)
* [Режим черновика](#Режим-черновика)

## Общие замечания
* Данный шаблон рассчитан на поддержку работы двух реализаций
автоматизированного формирования списка литературы и управления библиографией:
  * встроенная реализация с загрузкой файла через движок `bibtex` при
поддержке шаблонов пакета
[`gost`](http://mirrors.ctan.org/biblio/bibtex/contrib/gost/doc/gost.pdf);
  * реализация пакетом `biblatex` через движок `biber` (рекомендуемая)
при поддержке шаблонов пакета
[`biblatex-gost`](http://mirrors.ctan.org/macros/latex/contrib/biblatex-contrib/biblatex-gost/doc/biblatex-gost.pdf).
* Лучше всего всегда обрамлять значение BibTeX-атрибутов в фигурные скобки или
кавычки (то есть вместо *month = jul* писать *month = {jul}*).
* Также лучше всегда указывать язык BibTeX-записи (например, *language =
{russian}* или *language = {english}*). Запись языков всегда должна вестись
строчными (маленькими) буквами.
* Параметр *langid* заполнять не нужно -- он копируется из параметра *language*.
* Для пометки базы своей статьи (ВАК, Scopus, Web of Science), можно использовать *addendum = {(ВАК, Scopus, Web of Science)}*.
* Для автоматического подсчёта публикаций требуется добавить поля в публикациях в файле `biblio/author.bib`:
  * *authorvak = {true}* если публикация индексирована ВАК,
  * *authorscopus = {true}* если публикация индексирована Scopus,
  * *authorwos = {true}* если публикация индексирована Web of Science,
  * *authorconf = {true}* для докладов конференций,
  * *authorother = {true}* для других публикаций.
* Автоматический подсчёт патентов и зарегистрированных программ для ЭВМ осуществляется путём
  добавления в файл `biblio/registered.bib` полей:
  * *authorpatent = {true}* для патентов,
  * *authorprogram = {true}* для зарегистрированных программ.
* Для оптимального оформления списка литературы стоит убедиться, что исходный
*.bib файл заполнен правильным образом.
Примеры заполнения записей и результаты применения к ним основных стилей
приведены в [описании стилей пакета
`gost`](http://ctan.org/tex-archive/biblio/bibtex/contrib/gost) и в
[примерах применения пакета
`biblatex-gost`](http://mirrors.ctan.org/macros/latex/contrib/biblatex-contrib/biblatex-gost/doc/biblatex-gost-examples.pdf).

## Назначение и размещение файлов с библиографией
Файлы с библиографией расположены в папке [biblio/](../biblio/):
* работы автора — [author.bib](../biblio/author.bib);
* зарегистрированные патенты и программы для ЭВМ — [registered.bib](../biblio/reigstered.bib);
* чужие работы, на которые автор ссылается — [external.bib](../biblio/external.bib).

Кроме того, в этой же папке находится файл для автоматической проверки
библиографической информации на возможные дубликаты —
[check-bib-dupes-and-usage.py](../biblio/check-bib-dupes-and-usage.py)
Скрипт пытается найти повторяющиеся библиографические записи, которые внесены в
файлы с разными тегами (такое может произойти, если у вас уже есть несколько
публикаций, подготовленных в LaTeX. Их списки литературы могут пересекаться
если разные соавторы вносили их в разные исходные публикации под разными
тегами). Т.к. обычно список литературы достаточно небольшой (около 200
позиций), то скрипт считает маловероятным обнаружить публикации одного и того
же автора в разных работах на одной странице. Если такое происходит — выводится
уведомление. Вторая часть скрипта проверяет, все ли ссылки, внесённые в файл
библиографии, были использованы в тексте диссертации.

## Настройка библиографии

### Группированные подсписки литературы (ВАК, Web of Science и т.п.)

В некоторых советах принято литературу разбивать на подсписки: ВАК (или, например, рекомендованные для защиты в диссертационном совете МГУ по специальности), не из списка ВАК (другие) и прочее (тезисы докладов и т.п.).

В любом случае разбиение подразумевает в т.ч. подзаголовки в списке литературы. Пример:

![Пример подписка в МГУ](https://user-images.githubusercontent.com/146893/66545185-d5de5f00-eb42-11e9-8dd0-b93b681e57ab.png)

См. подробные обсуждения [#361](https://github.com/AndreyAkinshin/Russian-Phd-LaTeX-Dissertation-Template/issues/361) и [#362](https://github.com/AndreyAkinshin/Russian-Phd-LaTeX-Dissertation-Template/issues/362).

#### В автореферате
Настройка возможна в режиме biblatex (biber), но не bibtex. Для настройки подобного поведения в автореферате достаточно установить значение `bibgrouped` в `1` в файле [Synopsis/setup.tex](https://github.com/AndreyAkinshin/Russian-Phd-LaTeX-Dissertation-Template/blob/master/Synopsis/setup.tex) следующим образом:

```tex
\@ifundefined{c@bibgrouped}{
  \newcounter{bibgrouped}
  \setcounter{bibgrouped}{1}  % 0 --- единый список работ автора;
                              % 1 --- сгруппированные работы автора
}{}
```

#### В тексте диссертации

По умолчанию вся цитируемая литература выводится единым списком. Вывод литературы в тексте диссертации регулируется следующими строками в файле [Dissertation/references.tex](https://github.com/AndreyAkinshin/Russian-Phd-LaTeX-Dissertation-Template/blob/master/Dissertation/references.tex):

```tex
\insertbibliofull                           % Подключаем Bib-базы: все статьи единым списком
% Режим с подсписками
%\insertbiblioexternal                      % Подключаем Bib-базы: статьи, не являющиеся статьями автора по теме диссертации
% Для вывода выберите и расскомментируйте одно из двух
%\insertbiblioauthor                        % Подключаем Bib-базы: работы автора единым списком
%\insertbiblioauthorgrouped                 % Подключаем Bib-базы: работы автора сгруппированные (ВАК, WoS, Scopus и т.д.)
```

Чтобы настроить вывод работ автора, необходимо закомментировать команду `\insertbibliofull`, раскомментировать `\insertbiblioexternal` и одну из двух команд, подключающих работы автора. Например, для вывода группированных работ автора настройка выглядит так:

```tex
% \insertbibliofull                           % Подключаем Bib-базы: все статьи единым списком
% Режим с подсписками
\insertbiblioexternal                      % Подключаем Bib-базы: статьи, не являющиеся статьями автора по теме диссертации
% Для вывода выберите и расскомментируйте одно из двух
%\insertbiblioauthor                        % Подключаем Bib-базы: работы автора единым списком
\insertbiblioauthorgrouped                 % Подключаем Bib-базы: работы автора сгруппированные (ВАК, WoS, Scopus и т.д.)
```

#### Выбор групп для отображения

По умолчанию выводятся группы: ВАК, Web of Science, Scopus, тезисы конференций и прочие работы автора. Чтобы не выводить какую-то из указанных групп, достаточно закомментировать одну из следующих команд `\printbibliography` в файле [biblio/biblatex.tex](https://github.com/AndreyAkinshin/Russian-Phd-LaTeX-Dissertation-Template/blob/master/biblio/biblatex.tex):

```tex
    \section*{\bibtitleauthor}
    \ifsynopsis
    \printbibliography[heading=pubsubgroup, section=0, keyword=biblioauthorvak,    title=\bibtitleauthorvak,resetnumbers=true] % Работы автора из списка ВАК (сброс нумерации)
    \else
    \printbibliography[heading=pubsubgroup, section=0, keyword=biblioauthorvak,    title=\bibtitleauthorvak,resetnumbers=false] % Работы автора из списка ВАК (сквозная нумерация)
    \fi
    \printbibliography[heading=pubsubgroup, section=0, keyword=biblioauthorwos,    title=\bibtitleauthorwos,resetnumbers=false]% Работы автора, индексируемые Web of Science
    \printbibliography[heading=pubsubgroup, section=0, keyword=biblioauthorscopus, title=\bibtitleauthorscopus,resetnumbers=false]% Работы автора, индексируемые Scopus
    \printbibliography[heading=pubsubgroup, section=0, keyword=biblioauthorconf,   title=\bibtitleauthorconf,resetnumbers=false]% Тезисы конференций
    \printbibliography[heading=pubsubgroup, section=0, keyword=biblioauthorother,  title=\bibtitleauthorother,resetnumbers=false]% Прочие работы автора
```

#### Наименование списков и подсписков литературы

Может потребоваться изменить наименование списка\подсписка литературы. Например, с наименования по-умолчанию "В изданиях из списка ВАК РФ" на "Статьи в рецензируемых научных изданиях, рекомендованных для защиты в диссертационном совете МГУ по специальности". Для этого достаточно отредоактировать следующие строки в файле [common/newnames.tex](https://github.com/AndreyAkinshin/Russian-Phd-LaTeX-Dissertation-Template/blob/master/common/newnames.tex):

```tex
%%% Заголовки библиографии:

% для автореферата:
\newcommand{\bibtitleauthor}{Публикации автора по теме диссертации}

% для стиля библиографии `\insertbiblioauthorgrouped`
\newcommand{\bibtitleauthorvak}{В изданиях из списка ВАК РФ}
\newcommand{\bibtitleauthorscopus}{В изданиях, входящих в международную базу цитирования Scopus}
\newcommand{\bibtitleauthorwos}{В изданиях, входящих в международную базу цитирования Web of Science}
\newcommand{\bibtitleauthorother}{В прочих изданиях}
\newcommand{\bibtitleauthorconf}{В сборниках трудов конференций}

% для стиля библиографии `\insertbiblioauthorimportant`:
\newcommand{\bibtitleauthorimportant}{Наиболее значимые \protect\MakeLowercase\bibtitleauthor}

% для списка литературы в диссертации и списка чужих работ в автореферате:
\newcommand{\bibtitlefull}{Список литературы} % (ГОСТ Р 7.0.11-2011, 4)
```

### Строгость соответствия ГОСТ

  В соответствии с пунктом 5.6.7 [ГОСТ Р 7.0.11-2011 СИБИД. Диссертация
  и автореферат диссертации. Структура и правила
  оформления](http://docs.cntd.ru/document/1200093432) библиографические
  записи в списке литературы оформляют согласно [ГОСТ
  7.1](http://docs.cntd.ru/document/1200034383). Последний предписывает
  оформление записей в списке литературы примерно таким образом:

  > Лермонтов, М. Ю. Собрание сочинений: в 4 т. / М. Ю. Лермонтов. –– М. : Терра-Кн. клуб, 2009. –– 4 т.

  > Фамилия, И. О. Название статьи / И. О. Фамилия, И. О. Фамилия2, И. О. Фамилия3 // Журнал. –– 2013. –– Т. 1, № 5. –– С. 100––120.

  Подобное дублирование ФИО первого автора многих неподготовленных
  к строгости ГОСТ 7.1 читателей может сильно смутить. Кроме того, в вашем
  диссертационном совете может быть не принято строго соответствовать ГОСТ
  в этой части, и такой вид списка литературы может быть воспринят как
  следствие ошибки.

  В этом случае на свой страх и риск можно понизить строгость ГОСТ, закомментировать [следующие
  строки](https://github.com/AndreyAkinshin/Russian-Phd-LaTeX-Dissertation-Template/blob/master/biblio/biblatex.tex#L20-L22)
  файла `biblio/biblatex.tex`:

  ```tex
  \ltx@iffilelater{biblatex-gost.def}{2017/05/03}%
  {\toggletrue{bbx:gostbibliography}%
  \renewcommand*{\revsdnamepunct}{\addcomma}}{}
  ```

  Список литературы теперь будет выглядеть так:

  > Лермонтов М. Ю. Собрание сочинений: в 4 т. –– М. : Терра-Кн. клуб, 2009. –– 4 т.

  > Фамилия И. О., Фамилия2 И. О., Фамилия3 И. О. Название статьи // Журнал. –– 2013. –– Т. 1, № 5. –– С. 100––120.

  Подробнее, смотрите обсуждения в [#341](https://github.com/AndreyAkinshin/Russian-Phd-LaTeX-Dissertation-Template/issues/341), [#215](https://github.com/AndreyAkinshin/Russian-Phd-LaTeX-Dissertation-Template/issues/215).

## Замечания по реализациям библиографии
### `biblatex` + `biblatex-gost` + biber
* В версии `biblatex` 3.1 существует [баг](https://github.com/plk/biblatex/issues/355),
поэтому её не стоит использовать.
* Предупреждение в логе
```bash
Package biblatex Warning: 'babel/polyglossia' detected but 'csquotes' missing.
(biblatex) Loading 'csquotes' recommended.
```
является рекомендацией автора `biblatex` и `csquotes`.
`\usepackage{csquotes}` уберёт этот warning-recommendation,
только смысла в этом пакете для русскоязычной диссертации нет — он для
западноевропейских языков. Для русского языка `babel` и `polyglossia`
(с параметром `babelshorthands`) что могут — то решают.
* Посредством этой связки решается вопрос [подсчета авторских литературных
источников](https://github.com/AndreyAkinshin/Russian-Phd-LaTeX-Dissertation-Template/issues/33#issuecomment-150912772).

### Встроенная + `gost` + bibtex
* В bibtex отсутствует встроенная возможность создавать несколько списков
литературы для одного документа, поэтому для автореферата придётся обходиться
без ссылок на работы других авторов, оставляя нужный по ГОСТ список работ
автора по теме диссертации.
* Отечественный ГОСТ очень суров, в настоящее время ещё не создали такой
BibTeX-стиль, который бы ему полностью соответствовал. В данном шаблоне
используется стиль *utf8gost71u.bst*, он более или менее вменяемый и достаточно
близок к стандарту. Впрочем, при написании диссертации редко кто требует
точного соответствия ГОСТ-у, лишь всё было оформлено красиво и однообразно.
Если utf8gost71u.bst вас не устраивает, то вы можете выбрать любой другой стиль
(из папки [BibTeX-Styles](../BibTeX-Styles/) или найденный в интернете). В файле
biblio.bib аккуратно приведена вся библиография из ГОСТ Р 7.0.11–2011 и примеры
всех типов документов на английском, так что вы можете попробовать все
интересующие вас стили и увидеть, как каждый из них форматирует библиографию.
* В стилевых файлов русских ГОСТ-ов многие типы документов (например,
*PHDTHESIS* или *TECHREPORT*) сделаны очень плохо. В большинстве случаев лучше
их вполне можно заменить на *ARTICLE* или *BOOK*.
* `bibtex`(`bibtex8`) некорректно работает с преобразованиями юникодных
символов, потому сокращения до инициалов или возможности по изменению регистра
с utf8 работать не будут. Соответствующим образом надо заполнять `*.bib`
файл.
* Подборка русских стилевых пакетов BibTeX под UTF-8 размещена в папке
[BibTeX-Styles/](../BibTeX-Styles/).

#### ugost2008mod.bst
Доработанный шаблон `ugost2008.bst`:
* Теперь не ругается на тип `@Mastersthesis`.
* Теперь есть три функции (вместо одной) для выделения текста:
авторы, журнал, том издания, которыми можно управлять. По умолчанию выделения нет.
Пример задания выделения перед вызовом библиографии
(авторы — курсив, журнал — жирный, том — подчеркнутый):
```tex
\providecommand*{\BibEmph}[1]{\emph{#1}}
\providecommand*{\BibEmphi}[1]{\textbf{#1}}
\providecommand*{\BibEmphii}[1]{\underline{#1}}
```
* Ссылка DOI, при наличии у любого типа записей теперь проставлена
у первых пунктов после номера в списке литературы, а не только у названия журнала или книги.

* Если у записи есть DOI, но нет URL или eprint, то в конец записи в списке литературы пишется DOI: …

* Для того, чтобы убрать DOI из отображения, перед запуском библиографии пишется:
```tex
\makeatletter %http://tex.stackexchange.com/questions/40590/is-there-a-command-to-ignore-the-following-character
\def\?#1{}        % средство удаления последующего знака
\makeatother
\providecommand*{\BibDOI}[1]{\?}   % Пустой DOI, съедающий следующую за собой точку
```
* Как и у базового `ugost2008.bst` можно отключить разделительное
тире между элементами записи, записав перед вызовов библиографии:
```tex
\providecommand*{\BibDash}{}
```
* Теперь, если авторов больше трёх, то они перемещаются правее заглавия, в область
указания ответственности, и там сокращаются до первого «[и др.]» (согласно
распространённой практике применения библиографических ГОСТов).

## Список статей в презентации
В списке статей презентации не требуется соблюдение ГОСТ.
Для экономии места на слайде можно убрать лишнюю информацию о статьях автора, оставив лишь самое
необходимое.
Для этого в файле [biblatex.tex/](../biblio/biblatex.tex)
находится *Список лишних полей в презентации*.
В нём можно выбрать поля, которые требуется убрать из списка статей презентации.

## Дополнительная информация
Справка к пакету `biblatex-gost` рассказывает [о взаимосвязи ГОСТов на библиографию](http://mirrors.ctan.org/macros/latex/contrib/biblatex-contrib/biblatex-gost/doc/biblatex-gost.pdf).

[Цитирование в диссертации: рекомендации по оформлению](http://www.dissernet.org/instructions/instruction/citation-in-the-thesis-recommendations-on-the-formulation.htm).

## В случае проблем
Многие проблемы связаны с несоответствием выбранного движка данного шаблона
и движка настроенного в пользовательской системе для компиляции по умолчанию.
Движок настраивается в файлах `setup.tex` в строчке кода:
```tex
\setcounter{bibliosel}{1}           % 0 --- встроенная реализация с загрузкой файла через движок bibtex8; 1 --- реализация пакетом biblatex через движок biber
```

В случае проблем компиляции встроенной библиографии на движке
`bibtex`, попробуйте настроить в среде компиляции запуск `bibtex8`:
```bat
bibtex8.exe -B -c utf8cyrillic.csf %
```
где `%` — имя файла без расширения, или

```bat
bibtex8.exe -B -c utf8cyrillic.csf dissertation.aux
```

Если выводится в ошибка
```bash
I found no \citation commands---while reading file dissertation.aux
```
то, например под windows/texlive 2015/texstudio «лечится» изменением в
`Параметры`-`Конфигурация TeXStudio`-`Построение` настройки `Библиография по умолчанию`
на `Biber` (стоит часто `BibTeX`, и не работает, если в файлах `setup.tex`
настроено `\setcounter{bibliosel}{1}`). Если используется WinEdt и MikTEX: `Options`-`Execution Modes`- вкладка `Console Applications`- в списке слева пункт `BibTEX`. Параметр Executable меняем с `bibtex.exe` на `biber.exe`.

Если нумерация списка литературы начинается с неправильного номера, то
возможной причиной является старые версии используемых пакетов `biblatex` и
`biber`. Решается обновлением пакетов, обновлением всей установки TeX, или
можно в файле [biblatex.tex](../biblio/biblatex.tex) выставить в `false` или
закомментировать опцию пакета `biblatex`:
```tex
defernumbers=true,
```
рискуя при этом получить иные проблемы с нумерацией списка литературы.

## Режим черновика

При сборке в режиме черновика нумерация работ может быть неверной (для ускорения сборки).
Для правильной сортировки работ требуется:

* откомментировать строку `defernumbers=true,` в файле
[biblio/biblatex.tex](../biblio/biblatex.tex),
* в файле [common/characteristic.tex](../common/characteristic.tex) вынести строку
  `\printbibliography[heading=nobibheading,section=0,env=countexternal,keyword=biblioexternal]`
  за пределы условного оператора.