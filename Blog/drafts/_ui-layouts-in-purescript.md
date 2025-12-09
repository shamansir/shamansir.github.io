# Play: UI Layouts in PureScript

## Introduction

My way to pure functional programming was quite long, but now here I am. Definitely not knowing everything yet and still, so the (seemingly?) unreachable end of the way of learning excites me even more. Thank you, Elm, for seducing me with your friendly syntax and error messages, and leading me hand-in-hand to these greater depths.

Now most of my latest projects are written in PureScript, which is not to be confused with you-know-which-language, but rather a non-lazy Haskell for web development. So no unhandled errors in your code, at all. Logical errors are possible still.

All the UI approaches are there, as in many other languages, but usually I use Halogen library which provides its own set of functions both for HTML and SVG, no DSL needed, and it has a clear approach for writing components, including complex parent-child communication. 

> Though it doesn't matter which framework you use, if any, for the layouting system.

However, already a few of my projects are complex web-apps with unique UI structure and yet there's no UI composer in PureScript, at least as far as I know. The examples are:

* Noodle — visual programming platform, where:
	* it is possible to open many side panels: documentation, action history, log, and so on;
	* there is a library of node families; 
	* there as well is status bar with several cells;
	* there is patch area where all the nodes are layed out;
	* and all the nodes have their own structure which I want to have modular;
		 * the node could be vertical: inlets on the top, outlets on the bottom;
		 * the node could be horizontal: inlets on the left, outlets on the right;
	* there are several stacked layers: canvas in the background, SVG main area as a layer in the middle, HTML layer on top, and recently I have added one more canvas on top for the node bodies;

* Tree graph explorer, to visualize the many kinds of tree-structured data I have; Sometimes I store UI dependencies in a graph, sometimes I keep my book library organized as a tree, where a shelf or an author's name first letters can represent a node; It has these optional panels:
	* The tree itself;
	* The pinned nodes area, to keep an eye on the specific tree nodes (they can be complex interactive components by themselves);
	* The area where I can see a tree in its plain representation for easier navigation, but the selected nodes are highlighted;
	* The export area, for JSON and other formats preview;
	* ...

...and counting. So I felt an acute need in easing my positioning calculations, because for every small part the position needs to be calculated and I want them responsive. And with PureScript we're not having Swift UI-like constructors... yet.

## Clay UI as an inspiration

Almost in the same moments when this need was most desperate in my mind, YouTube happened to suggest me the video about Clay UI : the UI layouting library for C++ with beautifully simple and consice algorithm (yes, in C++) and it was all explained in all details in full in 40 minutes.

So I decided to translate it to pure FP version, it is interesting thought-trainer by itself and, considering the problems I mentioned above, it tended to also be very helpful and useful for me.

One of the core features of Clay is measuring text size in any font, so that it can be layed out correctly. In front-end web development we have our own tricks for that, like rendering the text block in some element that is hidden from user and measuring it, so I decided to omit this part, which is probably better to implement through JavaScript FFI.

And I named the library Play, because no other word came to my mind in attempts to combine PureScript and Clay. ChatGPT, do you know any better?

Hey, and there is a layout constructor to play with: https://shamansir.github.io/purescript-play/constructor.html

## Play API

As it is common to do in FP, I decided to let user put in a polymorphic parameter `a` any type they want: `Play a` can be `Play Int`, `Play String`, `Play Color`, `Play UIPart`,`Play Key`, `Play Character`, `Play (Play Whatever)`...

PureScript allows you to define any operator you want, so I decided to have `*~`for chaining, which is actually just an alias for `#`, so you can use any you prefer, just don't mix them in the same code. Here's the example of a defintion:

```
let menuLayout
```

`Play a` contains all the layout definitions, which side of the container / cell is fixed in size, or grows, or if it fits its children (more on that later), but they are not layed out yet (don't lay off, better lay out!).

There is also `Layout a`, which, as you may suggest, contains all the items layed out strictly following your definitions, having their positions and dimensions calculated.

  Since, as you may have noticed, I like tree structures, both of those are just trees under the hood:

```
data Play a = ...
data Layout a = ...
```

So the `a` can be anything, for example in case of Noodle node layout I have `Play NodePart` where `NodePart` is defined this way:

```
TODO
```

You may find more examples later in the post.

Here's how you can convert a definition into the layout:

Any cell can have its orientation either:

* _Horizontal_ — width is the main axis, the children are aligned horizontally;
* _Vertical_ — height is the main axis, the children are aligned vertically;

Then, either width or height of any cell can either be:

* _Fixed_ to some exact pixel size;
* _Fit_ its children by this side: pack them and resize to the sum of their width;
* _Grow_, unless it meets the next child or its parent can not expand more on the right / to the bttom;
* _FitGrow_ — fit its children and only then grow to the right / to the bottom: TODO;
* _FitMin_ — fit the children but no less than given value in pixels, so if children take less requested space, the side will have this size anyway, otherwise it will fit them into a larger size;

Notice there are no percentation values, because at some level we need the exact value to fit children in.

Both of them are functors and applicatives:

```
TODO
```

So, when you have defined your layout, call the `layout` function, which is a verb in this case, and you'll have the calculated rectangles in place.

You may unwrap the tree in any way you like, for example make it into an array. The calculations are already made, so the order is not important anymore, as well as parent-child relations (if you need the order for something else, I recommend to prefer to use `Play a` structure over `Layout a`):

```
TODO
```

## The Constructor

Together with Claude, we've made you a constructor which can ease creating the layouts by making it visual instead of just code:

TODO

By enabling encoded sizing labels, you may get visual help on how your layout is structured:

TODO

Start with the _Blank UI_ example if you would like to experiment from scratch.

You can click blocks on the visual preview to edit their properties. Or, especially for the cases when the block is zero-size or hidden below being compltely covered by its children, you can  navigate using the Properties panel. For every child there is _Go_ button to switch to this child, and whene you're there, there are _Parent_ (which allows you to switch to the parent of this particular child) and _Root_ (which allows you to switch to the only one parent for all this layout) buttons. If they are both disabled, you're already at root. If _Parent_ is disabled, then you're on the top level.

There's another, third way, to navigate: If you open the _Code & Tree_ panel on the bottom side of the screen, there's a tab with fully navigatable tree. Just click on any leaf and there you have switched to it.

The first tab on this panel, _Code_,  contains the generated code for current layout. 

Both tree view and code are instantly updated whenever you change something in the layout. Same way as the visual preview, obviously :).

TODO JSON

## Examples

You could've been bored enough to this point, so I decided to give you more examples and illustrate them with Kanji structure.

### Kanji

Kanji are japanese hieroglyphs and they can be recursive in a sense: they can be treated as a single whole characters or contain other kanji characters inside and still be treated as a whole. But there are only few certain ways to lay them out: 

* single character;
* top to bottom;  no matter if there are two or three elements, the above element could be smaller than the element below it or vise versa; may be the middle element is in most cases larger than the others, because other way it wouldn't be beautiful and would be weird, and kanji are nothing about weird; 
* left to right; the left element could be smaller than the right one or vise versa, the same statements as for vertical axis could apply here;
* enclosing: where one larger element contains another smaller one and either wraps it around completely or wraps it at least from two connected sides;

It could be quite easy to implement, but languages and writing systems are a bit more natural than mathematical, so they tend to be unpredictable and suprising more often than solving an equation or proving a theorem. But always beatiful. As how leaves are disordered on the tree. Or may be there's pure order we aren't aware about. That's why we developed fractals...

So the laying out process of the kanji could repeat some times, there could be enclosing of one element inside another and then this enclosing could be attached to the left of other two elements.

The element of kanji that can be reused inside other characters is called _radical_. Not all of dozens of thousands kanji can be radicals, but only around 214. If we follow the book, then the number is exactly 214.

Becase Unicode tries to cover all the writing systems and tries to optimize the rendering algorithms whenever possible by finding the patterns of possible combinations of characters, they developed the system called IDS: https://en.wikipedia.org/wiki/Ideographic_Description_Characters.

It defines all the possible known ways of combining radicals by doing what we love to do in functional programming: binary or ternary operators/functions are applied to the results of the calls of another operators/functions, and the arguments of these functions are the forementioned radicals.

TODO image

Since we plan to stretch radicals in different ways and not always proportionally, fir rendering we'll use the slabby font instead of a caligraphic one, or the one with the serifs, or else the beauty will be completely broken.

So lets finally define what we know with the code, our implementation would mirror the IDS machine:

```
TODO
```

The difference is that we also remember the rate — the proportion between how much more one radical takes than its pair in a space of `1.0`. To represent triplets, we'll just add a pair to an element, again like in pure FP. Oh wait...

#### Kanji. A single sole character / radical:



#### Kanji. Two (or more) characters aside:

#### Kanji. Two (or more) characters above each other:

#### Kanji. The enclosure:

#### Kanji. Other variations

### The chess board with pieces

### The Riichi mahjong table

### SVG Tree Viewer

TODO