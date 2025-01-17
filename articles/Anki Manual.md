Anki Manual

# Anki 2.1 User Manual

Looking for the [Anki 2.0 user manual?](https://apps.ankiweb.net/docs/manual20.html)

## Intro Videos

These videos were made with Anki 2.0, but 2.1 functions in largely the same way.

- [Shared Decks and Review Basics](http://www.youtube.com/watch?v=QS2G-k2hQyg&yt:cc=on)
- [Switching Card Order](http://www.youtube.com/watch?v=DnbKwHEQ1mA&yt:cc=on)
- [Styling Cards](http://www.youtube.com/watch?v=F1j1Zx0mXME&yt:cc=on)
- [Typing in the Answer](http://www.youtube.com/watch?v=5tYObQ3ocrw&yt:cc=on)

If YouTube is blocked in your country, you can[download the videos](https://apps.ankiweb.net/downloads/archive/screencasts/2.0/) instead.

## Translations

This page translated into other languages:

- [Bahasa Indonesia](https://apps.ankiweb.net/docs/manual.id.html)
- [Deutsch](http://www.dennisproksch.de/anki)
- [Español](https://apps.ankiweb.net/docs/manual.es.html)
- [Français](https://apps.ankiweb.net/docs/manual.fr.html)
- [Italiano](https://web.archive.org/web/20160423223801/http://192.167.9.6/Anki_ITA/Manual_ITA.htm)
- [Polski](https://apps.ankiweb.net/docs/manual.pl.html)
- [فارسى](http://ankidroid.ir/anki.pdf)
- [日本語](http://wikiwiki.jp/rage2050/?FrontPage)
- [简体中文](http://www.ankichina.net/anki20.html)

These translations are contributed by volunteers. If you would like to help translate the manual into a different language, or you would like to look at the translations that are currently in progress, please see the[translating the manual](https://apps.ankiweb.net/docs/manual.html#translatingmanual) section.

## Introduction

Anki is a program which makes remembering things easy. Because it is a lot more efficient than traditional study methods, you can either greatly decrease your time spent studying, or greatly increase the amount you learn.

Anyone who needs to remember things in their daily life can benefit from Anki. Since it is content-agnostic and supports images, audio, videos and scientific markup (via LaTeX), the possibilities are endless. For example:

- learning a language
- studying for medical and law exams
- memorizing people’s names and faces
- brushing up on geography
- mastering long poems
- even practicing guitar chords!

There are two simple concepts behind Anki: *active recall testing* and *spaced repetition*. They are not known to most learners, despite having been written about in the scientific literature for many years. Understanding how they work will make you a more effective learner.

### Active Recall Testing

*Active recall testing* means being asked a question and trying to remember the answer. This is in contrast to *passive study*, where we read, watch or listen to something without pausing to consider if we know the answer. Research has shown that active recall testing is far more effective at building strong memories than passive study. There are two reasons for this:

- The act of recalling something *strengthens* the memory, increasing the chances we’ll be able to remember it again.
- When we’re unable to answer a question, it tells us we need to return to the material to review or relearn it.

You have probably encountered active recall testing in your school years without even realizing it. When good teachers give you a series of questions to answer after reading an article, or make you take weekly progress-check tests, they are not doing it simply to see if you understood the material or not. By testing you, they are increasing the chances you will be able to remember the material in the future.

A good way to integrate active recall testing into your own studies is to use*flashcards*. With traditional paper flashcards, you write a question on one side of a card, and the answer on the other side. By not turning the card over until you’ve thought about the answer, you can learn things more effectively than passive observation allows.

### Use It or Lose It

Our brains are efficient machines, and they rapidly discard information that doesn’t seem useful. Chances are that you don’t remember what you had for dinner on Monday two weeks ago, because this information is not usually useful. If you went to a fantastic restaurant that day and spent the last two weeks telling people about how great it was, however, you’re likely to still remember in vivid detail.

The brain’s “use it or lose it” policy applies to everything we learn. If you spend an afternoon memorizing some science terms, and then don’t think about that material for two weeks, you’ll probably have forgotten most of it. In fact, studies show we forget about 75% of material learnt within a 48 hour period. This can seem pretty depressing when you need to learn a lot of information.

The solution is simple, however: *review*. By reviewing newly-learnt information, we can greatly reduce forgetting.

The only problem is that traditionally review was not very practical. If you are using paper flashcards, it’s easy to flick through all of them if you only have 30 of them to review, but as the number grows to 300 or 3000, it quickly becomes unwieldy.

### Spaced Repetition

The *spacing effect* was reported by a German psychologist in 1885. He observed that we tend to remember things more effectively if we spread reviews out over time, instead of studying multiple times in one session. Since the 1930s there have been a number of proposals for utilizing the spacing effect to improve learning, in what has come to be called *spaced repetition*.

One example is in 1972, when a German scientist called Sebastian Leitner popularized a method of spaced repetition with paper flashcards. By separating the paper cards up into a series of boxes, and moving the cards to a different box on each successful or unsuccessful review, it was possible to see at a glance a rough estimate of how well a card was known and when it should be reviewed again. This was a great improvement over a single box of cards, and it has been widely adopted by computerized flashcard software. It is a rather rough approach however, as it can’t give you an exact date on which you should review something again, and it doesn’t cope very well with material of varying difficulty.

The biggest developments in the last 30 years have come from the authors of SuperMemo, a commercial flashcard program that implements spaced repetition. SuperMemo pioneered the concept of a system that keeps track of the ideal time to review material and optimizes itself based on the performance of the user.

In SuperMemo’s spaced repetition system, every time you answer a question, you tell the program how well you were able to remember it – whether you forgot completely, made a small mistake, remembered with trouble, remembered easily, etc. The program uses this feedback to decide the optimal time to show you the question again. Since a memory gets stronger each time you successfully recall it, the time between reviews gets bigger and bigger – so you may see a question for the first time, then 3 days later, 15 days later, 45 days later, and so on.

This was a revolution in learning, as it meant material could be learnt and retained with the absolute minimum amount of effort necessary. SuperMemo’s slogan sums it up: with spaced repetition, you can *forget about forgetting*.

### Why Anki?

While there is no denying the huge impact SuperMemo has had on the field, it is not without its problems. The program is often criticized for being buggy and difficult to navigate. It only runs on Windows computers. It’s proprietary software, meaning end-users can’t extend it or access the raw data. And while very old versions are made available for free, they are quite limited for modern use.

Anki addresses these issues. There are free clients for Anki available on many platforms, so struggling students and teachers with budgetary constraints are not left out. It’s open source, with an already flourishing library of add-ons contributed by end-users. It’s multi-platform, running on Windows, Mac OSX, Linux/FreeBSD, and some mobile devices. And it’s considerably easier to use than SuperMemo.

Anki’s spaced repetition system is based on an older version of the SuperMemo algorithm called [SM-2](https://apps.ankiweb.net/docs/manual.html#what-algorithm).

## The Basics

### Cards

A question and answer pair is called a *card*. This is based on a paper flashcard with a question on one side and the answer on the back. In Anki a card doesn’t actually look like a physical card, and when you show the answer the question remains visible by default. For example, if you’re studying basic chemistry, you might see a question like:

Q: Chemical symbol for oxygen?

After thinking about it, and deciding the answer is O, you click the show answer button, and Anki shows you:

Q: Chemical symbol for oxygen?
A: O

After confirming that you are correct, you can tell Anki how well you remembered, and Anki will choose a next time to show you again.

### Decks

A *deck* is a group of cards. You can place cards in different decks to study parts of your card collection instead of studying everything at once. Each deck can have different settings, such as how many new cards to show each day, or how long to wait until cards are shown again.

Decks can contain other decks, which allows you to organize decks into a tree. Anki uses “::” to show different levels. A deck called “Chinese::Hanzi” refers to a “Hanzi” deck, which is part of a “Chinese” deck. If you select “Hanzi” then only the Hanzi cards will be shown; if you select “Chinese” then all Chinese cards, including Hanzi cards, will be shown.

To place decks into a tree, you can either name them with “::” between each level, or drag and drop them from the deck list. Decks that have been nested under another deck (that is, that have at least one “::” in their names) are often called *subdecks*, and top-level decks are sometimes called *superdecks*or *parent decks*.

Anki starts with a deck called “default”; any cards which have somehow become separated from other decks will go here. Anki will hide the default deck if it contains no cards and you have added other decks. Alternatively, you may rename this deck and use it for other cards.

Decks are best used to hold broad categories of cards, rather than specific topics such as “food verbs” or “lesson 1”. For more info on this, please see the [using decks appropriately](https://apps.ankiweb.net/docs/manual.html#manydecks) section.

For information on how decks affect the order cards are displayed in, please see the [display order](https://apps.ankiweb.net/docs/manual.html#displayorder) section.

### Notes & Fields

When making flashcards, it’s often desirable to make more than one card that relates to some information. For example, if you’re learning French, and you learn that the word “bonjour” means “hello”, you may wish to create one card that shows you “bonjour” and asks you to remember “hello”, and another card that shows you “hello” and asks you to remember “bonjour”. One card is testing your ability to recognize the foreign word, and the other card is testing your ability to produce it.

When using paper flashcards, your only option in this case is to write out the information twice, once for each card. Some computer flashcard programs make life easier by providing a feature to flip the front and back sides. This is an improvement over the paper situation, but there are two major downsides:

- Because such programs don’t track your performance of recognition and production separately, cards will tend not to be shown to you at the optimum time, meaning you forget more than you’d like, or you study more than is necessary.
- Reversing the question and answer only works when you want exactly the same content on each side. This means it’s not possible to display extra info on the back of each card for example.

Anki solves these problems by allowing you to split the content of your cards up into separate pieces of information. You can then tell Anki which pieces of information you want on each card, and Anki will take care of creating the cards for you and updating them if you make any edits in the future.

Imagine we want to study French vocabulary, and we want to include the page number on the back of each card. We want our cards to look like this:

Q: Bonjour
A: Hello
Page #12
And:
Q: Hello
A: Bonjour
Page #12

In this example, we have three pieces of related information: a French word, an English meaning, and a page number. If we put them together, they’d look like this:

French: Bonjour
English: Hello
Page: 12

In Anki, this related information is called a *note*, and each piece of information is called a *field*. So we can say that this type of note has three fields: French, English, and Page.

To add and edit fields, click the “Fields…” button while adding or editing notes. For more information on fields, please see the [Customizing Fields](https://apps.ankiweb.net/docs/manual.html#fields) section.

### Card Types

In order for Anki to create cards based on our notes, we need to give it a blueprint that says which fields should be displayed on the front or back of each card. This blueprint is called a *card type*. Each type of note can have one or more card types; when you add a note, Anki will create one card for each card type.

Each card type has two *templates*, one for the question and one for the answer. In the above French example, we wanted the recognition card to look like this:

Q: Bonjour
A: Hello
Page #12
To do this, we can set the question and answer templates to:
Q: {{French}}
A: {{English}}<br>
Page #{{Page}}

By surrounding a field name in double curly brackets, we tell Anki to replace that section with the actual information in the field. Anything not surrounded by curly brackets remains the same on each card. (For instance, we don’t have to type “Page #” into the Page field when adding material – it’s added automatically to every card.) <br> is a special code that tells Anki to move to the next line; more details are available in the [templates](https://apps.ankiweb.net/docs/manual.html#templates)section.

The production card templates work in a similar way:
Q: {{English}}
A: {{French}}<br>
Page #{{Page}}

Once a card type has been created, every time you add a new note, a card will be created based on that card type. Card types make it easy to keep the formatting of your cards consistent and can greatly reduce the amount of effort involved in adding information. They also mean Anki can ensure related cards don’t appear too close to each other, and they allow you to fix a typing mistake or factual error once and have all the related cards updated at once.

To add and edit card types, click the “Cards…” button while adding or editing notes. For more information on card types, please see the [Cards and Templates](https://apps.ankiweb.net/docs/manual.html#templates) section.

### Note Types

Anki allows you to create different types of notes for different material. Each type of note has its own set of fields and card types. It’s a good idea to create a separate note type for each broad topic you’re studying. In the above French example, we might create a note type called “French” for that. If we wanted to learn capital cities, we could create a separate note type for that as well, with fields such as “Country” and “Capital City”.

When Anki checks for duplicates, it only compares other notes of the same type. Thus if you add a capital city called “Orange” using the capital city note type, you won’t see a duplicate message when it comes time to learn how to say “orange” in French.

When you create a new collection, Anki automatically adds some standard note types to it. These note types are provided to make Anki easier for new users, but in the long run it’s recommended you define your own note types for the content you are learning. The standard note types are as follows:

Basic

Has Front and Back fields, and will create one card. Text you enter in Front will appear on the front of the card, and text you enter in Back will appear on the back of the card.

Basic (and reversed card)

Like Basic, but creates two cards for the text you enter: one from front→back and one from back→front.

Basic (optional reversed card)

This is a front→back card, and optionally a back→front card. To do this, it has a third field called “Add Reverse.” If you enter any text into that field, a reverse card will be created. More information about this is available in the [Cards and Templates](https://apps.ankiweb.net/docs/manual.html#templates) section.

Cloze

A note type which makes it easy to select text and turn it into a cloze deletion (e.g., “Man landed on the moon in […]” → “Man landed on the moon in 1969”). More information is available in the [cloze deletion](https://apps.ankiweb.net/docs/manual.html#cloze) section.

To add your own note types and modify existing ones, you can use Tools → Manage Note Types from the main Anki window.

|     |     |
| --- | --- |
| Note | Notes and note types are common to your whole collection rather than limited to an individual deck. This means you can use many different types of notes in a particular deck, or have different cards generated from a particular note in different decks. When you add notes using the Add window, you can select what note type to use and what deck to use, and these choices are completely independent of each other. You can also change the note type of some notes [after you’ve already created them](https://apps.ankiweb.net/docs/manual.html#browsermisc). |

### Collection

Your *collection* is all the material stored in Anki – your cards, notes, decks, note types, deck options, and so on.

## Adding Material

### Downloading Shared Decks

You can watch [a video about Shared Decks and Review Basics](http://www.youtube.com/watch?v=QS2G-k2hQyg&yt:cc=on) on YouTube.

The easiest way to get started with Anki is to download a deck of cards someone has shared:

1. Click the “Get Shared” button at the bottom of the deck list.

2. When you’ve found a deck you’re interested in, click the “Download” button to download a deck package.

3. Double-click on the downloaded package to load it into Anki, or File→Import it.

Please note that it’s not currently possible to add shared decks directly to your AnkiWeb account. You need to import them with the desktop program, then synchronize to upload them to AnkiWeb.

Please see [sharing decks](https://apps.ankiweb.net/docs/manual.html#sharingdecks) for info on sharing your own decks with others.

Self-made versus pre-made

Creating your own deck is the most effective way to learn a complex subject. Subjects like languages and the sciences can’t be understood simply by memorizing facts — they require explanation and context to learn effectively. Furthermore, inputting the information yourself forces you to decide what the key points are, leading to a better understanding.

If you are a language learner, you may be tempted to download a long list of words and their translations, but this won’t teach you a language any more than memorizing scientific equations will teach you astrophysics. To learn properly, you need textbooks, teachers, or exposure to real-world sentences.

Do not learn if you do not understand.
--SuperMemo

Most shared decks are created by people who are learning material outside of Anki – from textbooks, classes, TV, etc. They select the interesting points from what they learn and put them into Anki. They make no effort to add background information or explanations to the cards, because they already understand the material. So when someone else downloads their deck and tries to use it, they’ll find it very difficult as the background information and explanations are missing.

That is not to say shared decks are useless – simply that for complex subjects, they should be used as a *supplement* to external material, not as a*replacement* for it. If you’re studying textbook ABC and someone has shared a deck of ideas from ABC, that’s a great way to save some time. And for simple subjects that are basically a list of facts, such as capital city names or pub quiz trivia, you probably don’t need external material. But if you attempt to study complex subjects without external material, you will probably meet with disappointing results.

### Adding Cards and Notes

Recall from the [basics](https://apps.ankiweb.net/docs/manual.html#basics) that in Anki we add notes rather than cards, and Anki creates cards for us. Click *Add* in the main window, and the Add Notes window will appear.

The top left of the window shows us the current note type. If it does not say “Basic,” then you may have added some note types when you downloaded a shared deck. The text below assumes that “Basic” is selected.

The top right of the window shows us the deck cards will be added to. If you’d like to add cards to a new deck, you can click on the deck name button and then click “Add”.

Below the note type, you’ll see some buttons, and an area labeled “Front” and “Back”. Front and Back are called *fields*, and you can add, remove and rename them by clicking the “Fields…” button above.

Below the fields is another area labelled “Tags”. Tags are labels that you can attach to your notes, to make organizing and finding notes easier. You can leave the tags blank if you wish, or add one or more of them. Tags are separated by a space. If the tags area says

vocab check_with_tutor
…then the note you add would have two tags.

When you’ve entered text into the front and back, you can click the “Add” button or press Ctrl+Enter (Command+Enter on a Mac) to add the note to your collection. When you do so, a card will be created as well, and placed into the deck you chose. If you’d like to edit a card you added, you can click the history button to search for a recently added card in the [browser](https://apps.ankiweb.net/docs/manual.html#browser).

Anki checks the first field for uniqueness, so it will warn you if you enter two cards with a Front field of “apple” (for example). The uniqueness check is limited to the current note type, so if you’re studying multiple languages, two cards with the same Front would not be listed as duplicates as long as you had a different note type for each language.

Anki doesn’t check for duplicates in other fields automatically for efficiency reasons, but the browser has a “Find Duplicates” function which you can run periodically.

For more information on the buttons between the note type and the fields, please see the [editor](https://apps.ankiweb.net/docs/manual.html#editor) section.

Best Practices

Different people like to review in different ways, but there are some general concepts to keep in mind. An excellent introduction is[this article](http://www.supermemo.com/articles/20rules.htm) on the SuperMemo site. In particular:

- **Keep it simple**: The shorter your cards, the easier they are to review. You may be tempted to include lots of information “just in case,” but reviews will quickly become painful.
- **Don’t memorize without understanding**: If you’re studying a language, try to avoid large lists of words. The best way to learn languages is in context, which means seeing those words used in a sentence. Likewise, imagine you’re studying a computer course. If you attempt to memorize the mountain of acronyms, you’ll find it very difficult to make progress. But if you take the time to understand the concepts behind the acronyms, learning the acronyms will become a lot easier.

### Adding a Note Type

While basic note types are sufficient for simple cards with only a word or phrase on each side, as soon as you find yourself wanting to include more than one piece of information on the front or back, it’s better to split that information up into more fields.

You may find yourself thinking "but I only want one card, so why can’t I just include the audio, a picture, a hint and the translation in the Front field?" If you’d prefer to do that, that’s fine. But the disadvantage of that approach is that all the information is stuck together. If you wanted to sort your cards by the hint, you wouldn’t be able to do that as it’s mixed in with the other content. You also wouldn’t be able to do things like move the audio from the front to the back, except by laboriously copying and pasting it for every note. By keeping content in separate fields, you make it much easier to adjust the layout of your cards in the future.

To create a new type of note, choose Tools → Manage Note Types from the main Anki window. Then click “Add” to add a new type of note. You’ll now see another screen that gives you a choice of note types to base the new type on. “Add” means to base the newly created type on one that comes with Anki. “Clone” means to base the newly created type on one that is already in your collection. For instance, if you’d created a French vocab type already, you might want to clone that when creating a German vocab type.

After choosing OK, you’ll be asked to name the new type. The subject material you’re studying is a good choice here – things like “Japanese”, ”Trivia”, and so on. Once you’ve chosen a name, close the Note Types window, and you’ll return to the adding window.

### Customizing Fields

To customize fields, click the “Fields…” button when adding or editing a note, or while the note type is selected in the Manage Note Types window.

You can add, remove, or rename fields by clicking the appropriate buttons. To change the order in which the fields appear in this dialog and the add notes dialog, you can use the reposition button, which asks for the numerical position you want the field to have. So if you want to change a field to be the new first field, enter “1”.

|     |     |
| --- | --- |
| Note | Do not use *Tags*, *Type*, *Deck*, *Card*, or *FrontSide* as field names, as they are [special fields](https://apps.ankiweb.net/docs/manual.html#specialfields) and will not work properly. |

The options at the bottom of the screen allow you to edit various properties of the fields to be used when adding and editing the cards. This is *not* where you customize what appears on your cards when reviewing; for that, please see[templates](https://apps.ankiweb.net/docs/manual.html#templates).

**Editing Font** allows you to customize the font and size used when editing notes. This is useful if you want to make unimportant information smaller, or increase the size of foreign characters which are hard to read. The changes you make here do not affect how cards appear when reviewing: to do that, please see the [templates](https://apps.ankiweb.net/docs/manual.html#templates) section. If you have enabled the “type in the answer” function, however, the text you type will use the font size defined here. (For information about how to change the actual font face when typing the answer, please see the [checking your answer](https://apps.ankiweb.net/docs/manual.html#typinganswers) section.)

**Sort by this field…** tells Anki to show this field in the Sort Field column of the browser. You can use this to sort cards by that field. Only one field can be the sort field at once.

When **Remember last input…** is checked, Anki will not clear out this field’s content after a note is added. If you find yourself entering the same content into multiple notes, you may find this useful.

**Reverse text direction** is useful if you are studying languages that display text from right to left (RTL), such as Arabic or Hebrew. This setting currently only controls editing; to make sure the text displays correctly during review, you’ll need to adjust your [template](https://apps.ankiweb.net/docs/manual.html#templatesrtl).

After you’ve added fields, you’ll probably want to add them to the front or back of your cards. For more information on that, please see the[templates](https://apps.ankiweb.net/docs/manual.html#templates) section.

### Changing Deck / Note Type

While adding, you can click on the top left button to change note type, and the top right button to change deck. The window that opens up will not only allow you to select a deck or note type, but also to add new decks or manage your note types.

### Using Decks Appropriately

Decks are designed to divide your content up into broad categories that you wish to study separately, such as English, Geography, and so on. You may be tempted to create lots of little decks to keep your content organized, such as “my geography book chapter 1”, or “food verbs”, but this is not recommended, for the following reasons:

- Lots of little decks mean you end up reviewing cards in a recognizable order. Whether it’s because you’re clicking on each deck in turn (which is slow) or you’ve added a number of decks under a single parent deck, you’ll end up seeing all the “chapter 1” or “food verb” cards together. This makes it easier to answer the cards, as you can guess them from the context, which leads to weaker memories. When you need to recall the word or phrase outside Anki, you won’t have the luxury of being shown related content first!
- Anki was not designed to handle many decks (more than several dozen), and it will slow down as you add more – especially if you’re studying on a mobile client. A few extra decks is not going to make a noticeable difference, but if you have many decks the delays will start to add up.

Instead of creating lots of little decks, it’s a better idea to use tags and/or fields to classify your content. Instead of creating a “food verbs” decks for example, you could add those cards to your main language study deck, and tag the cards with “food” and “verb”. Each card can have multiple tags, which means you can do things like search for all verbs, or all food-related vocabulary, or all verbs that are related to food.

For those who like to stay very organized, you can add fields to your notes to classify your content, such as “book”, “page”, and so on. Anki supports searching in specific fields, which means you can do a search for “book:'my book' page:63” and immediately find what you’re looking for.

Anki’s [custom study and filtered deck](https://apps.ankiweb.net/docs/manual.html#filtered) features make this especially powerful, as you can create temporary decks out of search terms. This allows you to review your content mixed together in a single deck most of the time (for optimum memory), but also create temporary decks when you need to focus on particular material, such as before a test. The general rule is that if you always want to be able to study some content separately, it should be in a normal deck, and if you only occasionally need to be able to study it separately (for a test, when under a backlog, etc), tags/fields and filtered decks are better.

## Studying

When you have found a deck you like or entered some notes in, it’s time to start studying.

### Decks

Study in Anki is limited to the currently selected deck as well as any subdecks it contains.

On the decks screen, your decks will be displayed in a list. There are two number columns, *due* and *new*. *Due* is the count of waiting reviews and cards currently in learning. *New* is the number of new cards that are ready to be learnt that day.

When you click on a deck, it will become the *current deck*, and Anki will change to the study screen. You can return to the deck list to change the currently selected deck at any time by clicking on “Decks” at the top of the main window. (You can also use the [Study Deck](https://apps.ankiweb.net/docs/manual.html#studydeck) feature to select a new deck from the keyboard, or you can press the ‘s’ key to study the currently selected deck.)

You can click the gears button to the right of a deck to rename or delete a deck, change its options, or [export](https://apps.ankiweb.net/docs/manual.html#exporting) it.

When a deck has subdecks, the cards will appear from [each deck in turn](https://apps.ankiweb.net/docs/manual.html#displayorder).

### Study Overview

After clicking on a deck to study, you’ll see a screen that shows you how many cards are due today. This is called the *deck overview* screen. The cards are split into three types:

- **New** refers to cards that you have downloaded or entered in, but have never been studied before.
- **Learning** refers to cards that were seen for the first time recently, and are still being learnt.
- **To Review** refers to cards that were previously learnt, and now need to be reviewed so you don’t forget them.

To start a study session, click the **Study Now** button. Anki will proceed to show you cards until the cards to be shown for the day have run out.

While studying, you can return to the overview by pressing the “s” key on your keyboard.

### Questions

When a card is shown, only the question is shown at first. After thinking about the answer, either click the **Show Answer** button, or press the spacebar. The answer will then be shown. It’s okay if it takes you a little while to recall the answer, but as a general rule if you can’t answer within about 10 seconds, it’s probably better to give up and show the answer than keep struggling to remember.

When the answer is shown, you should compare the answer you thought of with the answer which is shown and tell Anki how well you remembered. If you don’t trust yourself to compare your answer accurately, you can ask Anki to[prompt you to type in the answer](https://apps.ankiweb.net/docs/manual.html#typinganswers) rather than just showing it to you.

The number of buttons available for grading depends on whether the card is being *learnt* or *reviewed*.

### Learning

When learning new cards, or when relearning cards that you have forgotten, Anki will show you the cards one or more times to help you memorize them. Each time is called a *learning step*. By default there are two steps: 1 minute and 10 minutes. You can change the number of steps and the delays between them in the[deck options](https://apps.ankiweb.net/docs/manual.html#deckoptions).

There are three rating buttons when learning:
**Again** moves the card back to the first step.

**Good** moves the card to the next step. If the card was on the final step, the card is converted into a review card (it *graduates*). By default, once the card has reached the end of the learning steps, the card will be shown again the next day, then at increasingly long delays (see the next section).

**Easy** immediately converts the card into a review card, even if there were steps remaining. By default, the card will be shown again 4 days later, and then at increasingly long delays. The easy button will not be shown if you are in relearning mode and it would give the same interval as “good.”

When cards are seen for the first time, they start at step one. This means answering **Good** on a card for the first time will show it one more time in 10 minutes, and the initial 1 minute step will be skipped. If you push Again, though, the card will come back in 1 minute.

You can use the 1, 2 and 3 keys on your keyboard to select a particular button, where 1 is **Again**. Pressing the spacebar will select **Good**.

If there are no other cards to show you, Anki will show learning cards again even if their delay has not elapsed completely. If you’d prefer to wait the full learning delay, you can change this behaviour in the[preferences](https://apps.ankiweb.net/docs/manual.html#preferences).

### Reviewing

When a card has been previously learnt and is ready to be reviewed again, there are four buttons to rate your answer:

**Again** marks your answer as incorrect and asks Anki to show the card more frequently in the future. The card is said to have *lapsed*. Please see the[lapses](https://apps.ankiweb.net/docs/manual.html#lapses) section for more information about how lapsed reviews are handled.

**Hard** shows the card at a slightly longer delay than last time, and tells Anki to show the card more frequently in the future.

**Good** tells Anki that the last delay was about right, and the card easiness doesn’t need to be adjusted down or up. At the default starting easiness, the card will be shown again approximately 2 1/2 times longer than the previous time, so if you had waited 10 days to see the card previously, the next delay would be about 25 days.

**Easy** tells Anki you found the delay too short. The card will be scheduled further into the future than *Good*, and Anki will schedule the card less frequently in the future. Because *Easy* rapidly increases the delay, it’s best used for only the easiest of cards. Usually you should find yourself answering *Good* instead.

As with learning cards, you can use 1-4 on the keyboard to select an answer. Pressing the spacebar will select *Good*.

### Due Counts and Time Estimates

When only the question is shown, Anki shows three numbers like 12 + 34 + 56 at the bottom of the screen. These represent the new cards, cards in learning, and cards to review. If you’d prefer not to see the numbers, you can turn them off in Anki’s preferences.

|     |     |
| --- | --- |
| Note | The numbers count *reviews* needed to finish all the cards in that queue, not the number of *cards*. If you have multiple steps configured for lapsed cards, the number will increase by more than one when you fail a card, since that card needs to be shown several times. |

When the answer is shown, Anki shows an estimate of the next time a card will be shown above each button. If you’d prefer not to see the estimates, you can disable them in Anki’s [preferences](https://apps.ankiweb.net/docs/manual.html#preferences).

|     |     |
| --- | --- |
| Note | Anki additionally adds a small amount of random variation to the next due times, in order to prevent cards that were introduced together and always rated the same from always staying next to each other. This variation is not shown on the time estimates but will be applied after selecting the button. |

### Editing and More

You can click the **Edit** button in the bottom left to edit the current note. When you finish editing, you’ll be returned to study. The editing screen works very similarly to the [add notes](https://apps.ankiweb.net/docs/manual.html#addingnotes) screen.

At the bottom right of the review screen is a button labeled **More**. This button provides some other operations you can do on the current card or note:

Mark Note

Adds a “marked” tag to the current note, so it can be easily found in the browser. This is useful when you want to take some action on the note at a later date, such as looking up a word when you get home. Marked cards also show a small star in the upper-right-hand corner during reviews.

Bury Card / Note

Hides a card or all of the note’s cards from review until the next day. (If you want to unbury cards before then, you can click the “unbury” button on the [deck overview](https://apps.ankiweb.net/docs/manual.html#deckoverview) screen.) This is useful if you cannot answer the card at the moment or you want to come back to it another time. Burying can also [happen automatically](https://apps.ankiweb.net/docs/manual.html#siblings) for cards of the same note. If cards were in learning when they are buried, they are moved back to the new card queue or review queue prior to being buried.

Suspend Card / Note

Hides a card or all of the note’s cards from review until they are manually unsuspended (by clicking the suspend button in the browser). This is useful if you want to avoid reviewing the note for some time, but don’t want to delete it. If cards were in learning when they are suspended, they are moved back to the new card queue or review queue prior to being suspended.

Delete Note
Deletes the note and all of its cards.
Options
Edit the options for the current deck.
Replay Audio
If the card has audio on the front or back, play it again.
Record Own Voice

Record from your microphone for the purposes of checking your pronunciation. This recording is temporary and will go away when you move to the next card. If you want to add audio to a card permanently, you can do that in the edit window.

Replay Own Voice

Replay the previous recording of your voice (presumably after showing the answer).

### Display Order

Studying will show cards from the selected deck and any decks it contains. Thus, if you select your “French” deck, the subdecks “French::Vocab” and “French::My Textbook::Lesson 1” will be shown as well.

For new cards and reviews, Anki fetches cards from the decks in alphabetical order. So in the above example, you would get cards first from “French”, then “My Textbook”, and finally “Vocab”. You can use this to control the order cards appear in, placing high priority cards in decks that appear higher in the list. When computers sort text alphabetically, the “-” character comes before alphabetical characters, and “~” comes after them. So you could call the deck “-Vocab” to make them appear first, and you could call the other deck “~My Textbook” to force it to appear after everything else.

New cards and reviews are fetched separately, and Anki won’t wait until both queues are empty before moving on to the next deck, so it’s possible you’ll be exposed to new cards one deck while seeing reviews from another deck, or vice versa. If you don’t want this, click directly on the deck you want to study instead of one of the parent decks.

Since cards in learning are somewhat time-critical, they are fetched from all decks at once and shown in the order they are due.

To control the order reviews from a given deck appear in, or change new cards from ordered to random order, please see the [deck options](https://apps.ankiweb.net/docs/manual.html#deckoptions). For more fine-grained ordering of new cards, you can change the order in the[browser](https://apps.ankiweb.net/docs/manual.html#browser).

### Siblings and Burying

Recall from [the basics](https://apps.ankiweb.net/docs/manual.html#basics) that Anki can create more than one card for each thing you input, such as a front→back card and a back→front card, or two different cloze deletions from the same text. These related cards are called*siblings*.

When you answer a card that has siblings, Anki can prevent the card’s siblings from being shown in the same session by automatically *burying* them. Buried cards are hidden from review until the clock rolls over to a new day or you manually unbury them using the “Unbury” button that’s visible at the bottom of the [deck overview](https://apps.ankiweb.net/docs/manual.html#deckoverview) screen. Anki will bury siblings even if the siblings are not in the same deck (for instance, if you use the[deck override](https://apps.ankiweb.net/docs/manual.html#deckoverride) feature).

You can enable burying from the [deck options](https://apps.ankiweb.net/docs/manual.html#deckoptions) screen - there are separate settings for new cards and reviews.

Anki will only bury siblings that are new or review cards. It will not hide cards in learning, as time is of the essence for those cards. On the other hand, when you study a learning card, any new/review siblings will be buried.

### Keyboard Shortcuts

Most of the common operations in Anki have keyboard shortcuts. Most of them are discoverable in the interface: menu items list their shortcuts next to them, and hovering the mouse cursor over a button will generally show its shortcut in a tooltip.

When studying, either space or enter will show the answer. When the answer is shown, you can use space or enter to select the Good button. You can use the 1-4 keys to select a specific ease button. Many people find it convenient to answer most cards with space and keep one finger on 1 for when they forget.

The "Study Deck" item in the Tools menu allows you to quickly switch to a deck with the keyboard. You can trigger it with the */* key. When opened, it will display all of your decks and show a filter area at the top. As you type characters, Anki will display only decks matching the characters you type. You can add a space to separate multiple search terms, and Anki will show only decks that match all the terms. So “ja 1” or “on1 ja” would both match a deck called “Japanese::Lesson1”.

### Falling Behind

If you fall behind in your reviews, Anki will prioritize cards that have been waiting the longest. It does this by taking the the cards that have been waiting the longest and showing them to you in a random order up until your daily review limit. This ordering ensures that no cards will be left waiting indefinitely, but it means that if you introduce new cards, their reviews won’t appear until you’ve gotten through your backlog.

If you wish to change the order of the overdue reviews, you can do so by creating a [filtered deck](https://apps.ankiweb.net/docs/manual.html#filtered).

When you answer cards that have been waiting for a while, Anki factors in that delay when determining the next time a card should be shown. Please see the section on Anki’s spaced-repetition [algorithm](https://apps.ankiweb.net/docs/manual.html#what-algorithm) for more information.

## Editing

### Features

The editor is shown when [adding notes](https://apps.ankiweb.net/docs/manual.html#addingnotes), [editing a note](https://apps.ankiweb.net/docs/manual.html#editmore) during reviews, or [browsing](https://apps.ankiweb.net/docs/manual.html#browser).

On the top left are two buttons, which open the [fields](https://apps.ankiweb.net/docs/manual.html#fields) and[cards](https://apps.ankiweb.net/docs/manual.html#templates) windows.

On the right are buttons that control formatting. Bold, italic and underline work like they do in a word processing program. The next two buttons allow you to subscript or superscript text, which is useful for chemical compounds like H2O or simple math equations like x2.

The Fx button clears any formatting in the currently selected text. This includes colours, bold, etc.

The next two buttons allow you to change text colour.
The […] button is visible when a cloze note type is selected.

You can use the paperclip button to select audio, images and videos from your computer’s hard drive to attach to your notes. Alternatively, you can copy the media onto your computer’s clipboard (for instance, by right-clicking an image on the web and choosing *Copy Image*) and paste it into the field that you want to place it in. For more information about media, please see the[media](https://apps.ankiweb.net/docs/manual.html#media) section.

The microphone icon allows you to record from your computer’s microphone and attach the recording to the note.

The last button shows more advanced features, such as editing the underlying HTML of a field, and shortcuts to add MathJax or [LaTeX](https://apps.ankiweb.net/docs/manual.html#latex) to your notes.

Most of the buttons have shortcut keys. You can hover the mouse cursor over a button to see its shortcut.

When pasting text, Anki will strip most formatting by default. If you hold down the shift key while pasting, Anki will preserve more formatting.

### Cloze Deletion

*Cloze deletion* is the process of hiding one or more words in a sentence. For example, if you have the sentence:

Canberra was founded in 1913.
…and you create a cloze deletion on “1913”, then the sentence would become:
Canberra was founded in [...].

Sometimes sections that have been removed in this fashion are said to be*occluded*.

For more information on why you might want to use cloze deletion, see rule number 5 [here](http://www.supermemo.com/articles/20rules.htm).

Anki provides a special cloze deletion type of note, to make creating clozes easy. To create a cloze deletion note, select the Cloze note type, and type some text into the "Text" field. Then drag the mouse over the text you want to hide to select it, and click the […] button. Anki will replace the text with:

Canberra was founded in {{c1::1913}}.

The “c1” part means that you’ve created one cloze deletion on the sentence. You can create more than one deletion if you’d like. For example, if you select Canberra and click […] again, the text will now look like:

{{c2::Canberra}} was founded in {{c1::1913}}.

When you add the above note, Anki will create two cards. The first card will show:

Canberra was founded in [...].

…on the question, with the full sentence on the answer. The other card will have the following on the question:

[...] was founded in 1913.

You can also elide multiple sections on the same card. In the above example, if you change c2 to c1, only one card would be created, with both Canberra and 1913 hidden. If you hold down alt (option on a Mac) while creating a cloze, Anki will automatically use the same number instead of incrementing it.

Cloze deletions don’t need to fall on word boundaries, so if you select “anberra” rather than “Canberra” in the above example, the question would appear as “C[…] was founded in 1913”, giving you a hint.

You can also give yourself hints that don’t match the text. If you replace the original sentence with:

Canberra::city was founded in 1913

…and then press […] after selecting "Canberra::city", Anki will treat the text after the two colons as a hint, changing the text into:

{{c1::Canberra::city}} was founded in 1913
When the card comes up for review, it will appear as:
[city] was founded in 1913.

For information on testing your ability to type in a cloze deletion correctly, please see the section on [typing answers](https://apps.ankiweb.net/docs/manual.html#typinganswers).

Please note that overlapping clozes are not supported. For example, the following field is invalid:

{{c1::Canberra was {{c2::founded}}}} in 1913

If you need to create clozes from overlapping text, add another Text field to your cloze, add it to the [template](https://apps.ankiweb.net/docs/manual.html#templates), and then when creating notes, paste the text into two separate fields, like so:

Text1 field: {{c1::Canberra was founded}} in 1913
Text2 field: {{c2::Canberra}} was founded in 1913

The default cloze note type has a second field called Extra, that is shown on the answer side of each card. It can be used for adding some usage notes or extra information.

The cloze note type is treated specially by Anki, and cannot be created based on a regular note type. If you wish to customize it, please make sure to clone the existing Cloze type instead of another type of note.

### Inputting Foreign Characters and Accents

All modern computers have built in support for typing accents and foreign characters, and multiple ways to go about it. The method we recommend is using a keyboard layout for the language you want to learn.

Languages with a separate script like Japanese, Chinese, Thai and so on have their own layouts specifically for that language.

European languages that use accents may have their own layout, but can often by typed on a generic "international keyboard" layout. These work by typing the accent, then the character you want accented - eg an apostrophe (') then the letter a (a) gives á.

To add the international keyboard on Windows machines, please seehttps://support.microsoft.com/en-au/kb/306560

To add it on Macs, please seehttp://www.macworld.com/article/1147039/os-x/accentinput.html

Keyboards for a specific language are added in a similar way, but we can not cover them all here. For more information, please try searching Google for "input Japanese on a mac", "type Chinese on Windows 10", and so on.

If you’re learning a right to left language, there are lots of other things to consider. Please see[this page](http://dotancohen.com/howto/rtl_right_to_left.html) for more information.

|     |     |
| --- | --- |
| Note | The toolkit Anki is built on has trouble dealing with a few input methods, such as holding down keys to select accented characters on Mac OS X, and typing characters by holding down the alt key and typing a numeric code on Windows. |

## Cards and Templates

As mentioned in the [basics](https://apps.ankiweb.net/docs/manual.html#cardtypes) section, Anki creates cards automatically, based on the notes you add. (Please read the basics section if you have not done so already, as the rest of this section assumes that you have read it.)

You can configure the cards Anki should create and what should be shown on them when adding or editing material by clicking on the “Cards…” button. At the top of the window you’ll see a set of tabs, one for each card type. You can click the plus on the right if you’d like to add another card type to the current note type. Similarly, if you’d like to delete one, you can do so by clicking the X on the tab.

On the top left is the front template, on the bottom left is the back template, and in between them is the card styling section.

In Anki, templates are written in HTML, which is the language that web pages are written in. The styling section is CSS, which is the language used for styling web pages.

On the right is a preview of the front and back of the currently selected card. If you opened the window while adding notes, the preview will be based on the text you had typed into the Add Notes window. If you opened the window while editing a note, the preview will be based on the content of that note. If you opened the window from Tools → Manage Note Types, Anki will display each field’s name in parentheses in place of content.

At the top right of the window is an Options button that gives you options to rename or reorder the cards, as well as the following two options:

- The *Deck Override* option allows you to change the deck that cards generated from the current card type will be placed into. By default, cards are placed into the deck you provide in the Add Notes window. If you set a deck here, that card type will be placed into the deck you specified, instead of the deck listed in the Add Notes window. This can be useful if you want to separate cards into different decks (for instance, when studying a language, to put production cards in one deck and recognition cards in another). You can check which deck the cards are currently going to by choosing Deck Override again.
- The *Browser Appearance* option allows you to set different (perhaps simplified) templates for display in the Question and Answer columns of the browser; see[browser appearance](https://apps.ankiweb.net/docs/manual.html#columntemplates) for more information.

### Reverse Cards

You can watch [a video about reversing cards](http://www.youtube.com/watch?v=DnbKwHEQ1mA&yt:cc=on) on YouTube.

If you want to create cards that go in both directions (e.g., both “ookii”→“big” and “big”→“ookii”), you have several options. The simplest is to select the “Basic (and reversed card)” built-in note type. This will generate two cards, one in each direction.

If you want to generate reverse cards for only some of your material (perhaps you only want to take the time to study reverses for the most important material, or some of your cards don’t make sense reversed), you can select the “Basic (optional reversed card)” note type. This note type generates a forward-only card when you fill in only the first two fields; if you additionally enter something in the “Add Reverse” field (like a *y*), Anki will generate a reverse card as well. The contents of this field will never be displayed on a card.

If you later decide you don’t want a reverse card that you added, you can delete it by removing the text from the “Add Reverse” field. Similarly, if you want to add a reverse card, you can add text to the “Add Reverse” field. If you didn’t select the optional reverse note type to begin with, you can use Edit → Change Note Type in the browser to change it.

|     |     |
| --- | --- |
| Note | To avoid loss of scheduling information if you make an editing mistake, Anki does not automatically delete cards after you remove the text from the “add reverse” field. To complete the deletion, run Tools → Empty Cards from the main window. |

If you’re using a more complex note type (for instance, one with three cards) and you wish to generate specific cards only in certain situations, please see the [conditional replacement](https://apps.ankiweb.net/docs/manual.html#conditionalreplacement) section.

### Basic Templates

The most basic template looks something like this:
{{Front}}

When you place text within curly brackets, Anki looks for a field by that name, and replaces the text with the actual content of the field. You can include as many fields as you wish.

|     |     |
| --- | --- |
| Note | Field names are case sensitive. If you have a field named *Front*, writing *{{front}}* will not work properly. |

Your templates are not limited to a list of fields. You can also include arbitrary text on your templates. For example, if you’re studying capital cities, and you’ve created a note type with a “Country” field, you might create a front template like this:

What's the capital city of {{Country}}?
The default back template will look something like this:
{{FrontSide}}
<hr id=answer>
{{Back}}

This means “show me the text that’s on the front side, then a divider line, and then the Back field”.

The *id=answer* part tells Anki where the divider is between the question and the answer. This allows Anki to automatically scroll to the spot where the answer starts when you press *show answer* on a long card (especially useful on mobile devices with small screens). If you don’t want a horizontal line at the beginning of the answer, you can use another HTML element such as a paragraph or div instead.

### Checking Your Answer

You can watch [a video about this feature](http://www.youtube.com/watch?v=5tYObQ3ocrw&yt:cc=on) on YouTube.

If you’d like to type in the answer and have Anki compare your input to the real answer, you can do so by changing your template. Imagine your front and back templates look like:

{{Native Word}}
{{FrontSide}}
<hr id=answer>
{{Foreign Word}}

To type in the foreign word and check if you are correct, you need to edit your front template so that it looks like this:

{{Native Word}}
{{type:Foreign Word}}

Note that we have added *type:* in front of the field we want to compare. Since FrontSide is on the back of the card, the type answer box will appear on the back as well. (If you don’t have FrontSide on the back of your card, you will need to add the type directive to the answer side as well.)

When reviewing, Anki will display a text box where you can type in the answer, and upon hitting enter or showing the answer, Anki will show you which parts you got right and which parts you got wrong. The text box’s font size will be the size you configured for that field (via the “Fields” button when editing).

This feature does not change how the cards are answered, so it’s still up to you to decide how well you remembered or not.

|     |     |
| --- | --- |
| Note | Only one typing comparison can be used on a card. If you add the above text multiple times, it will not work. It also only supports a single line, so it is not useful for comparing against a field that is comprised on multiple lines. |

Anki uses a monospaced font for the answer comparison so that the “provided” and “correct” sections line up. If you wish to override the font, you can put the following at the bottom of your styling section:

code#typeans { font-family: "myfontname"; }

Advanced users can override the default type-answer colours with the css classes *typeGood*, *typeBad* and *typeMissed*. AnkiMobile supports *typeGood*and *typeBad*, but not *typeMissed*.

It is also possible to type in the answer for cloze deletion cards. To do this, add {{type:cloze:Text}} to both the front and back template, so the back looks something like this:

{{cloze:Text}}
{{type:cloze:Text}}
{{Extra}}

Note that since the cloze type does not use FrontSide, this must be added to both sides on a cloze note type.

If there are multiple sections elided, you can separate the answers in the text box with a comma.

|     |     |
| --- | --- |
| Note | Type answer boxes will not appear in the ["preview" dialog](https://apps.ankiweb.net/docs/manual.html#currentnote-preview) in the browser. When you review or look at the preview in the card types window, they will display. |

### Newlines

The template language needs a special command to create a new line. For example, if you wrote the following in the template:

one
two
In the preview, you’d actually see:
one two
To add a new line, you need to add a <br> code to the end of a line, like so:
one<br>
two
The br code stands for "(line) br(eak)".

The same applies for fields. If you want to display two fields, one on each line, you would use

{{Field 1}}<br>
{{Field 2}}

### Card Styling

You can watch [a video about styling cards](http://www.youtube.com/watch?v=F1j1Zx0mXME&yt:cc=on) on YouTube. The video shows Anki 2.0’s interface, but the concepts are largely the same.

In between the front and back template is the card styling. Here you can change the background colour of the card, the default font, the text alignment, and so on.

|     |     |
| --- | --- |
| Note | This is *not* where you change the font for type answer comparisons, type answer textboxes, or editing textboxes; to learn how to change these fonts, please see the [checking your answer](https://apps.ankiweb.net/docs/manual.html#typinganswers) and[customizing fields](https://apps.ankiweb.net/docs/manual.html#fields) sections. |

The standard options available to you are:
font-family

The name of the font to use on the card. If your font has spaces in it like "MS Unicode", then you need to surround the font name in double quotes as in this sentence. It is also possible to use multiple fonts on one card; for information on that, please see below.

font-size

The size of the font in pixels. When changing it, make sure you leave px at the end.

text-align
Whether the text should be aligned in the center, left, or right.
color

The color of the text. Simple color names like *blue*, *lightyellow*, and so on will work, or you can use HTML color codes to select arbitrary colors. Please see [this webpage](http://htmlcolorcodes.org/) for more information.

background-color
The color of the card background.

Any CSS can be placed in the styling section – advanced users may wish to do things like add a background image or gradient, for example. If you’re wondering how to get some particular formatting, please search the web for information about how to do it in CSS, as there is a great deal of documentation available.

The styling is shared between all cards, which means that when you make an adjustment it will affect all cards for that note type. It is also possible to specify card-specific styling, however. The following example will use a yellow background on all cards except the first one:

.card { background-color: yellow; }
.card1 { background-color: blue; }

One other thing to note is that Anki shrinks images to fit the screen by default. You can change this by adding the following to the bottom of your styling section:

img { max-width: none; max-height: none; }

If you try to change the style for images and find that the star that appears on marked cards is affected (for instance, it becomes way too large), you can target it with the following:

img#star { ... }

### Field Styling

The default styling applies to the whole card. You can also make certain fields or part of the card use a different font, color, and so on. This is particularly important when studying foreign languages, as Anki will sometimes be unable to correctly display characters unless an appropriate font has been chosen.

Say you have an “Expression” field, and you want to give it the OSX Thai font “Ayuthaya”. Imagine your template already reads:

What is {{Expression}}?
{{Notes}}

What we need to do is wrap the text we want to style in some HTML. We will put the following in front of the text:

<div class=mystyle1>
And the following behind it:
</div>

By wrapping the text like the above, we tell Anki to style the wrapped text with a custom style called “mystyle1”, which we will create later.

Thus if we wanted the entire “What is …?” expression to use the Thai font, we would use:

<div class=mystyle1>What is {{Expression}}?</div>
{{Notes}}

And if we wanted only the expression field itself to use the Thai font, we’d use:

What is <div class=mystyle1>{{Expression}}</div>?
{{Notes}}

After we’ve edited the template, we now need to move to the Styling section between the templates. Before editing it, it should look something like:

.card {
font-family: arial;
font-size: 20px;
text-align: center;
color: black;
background-color: white;
}
Add your new style to the bottom, so it looks like:
.card {
font-family: arial;
font-size: 20px;
text-align: center;
color: black;
background-color: white;
}
.mystyle1 {
font-family: ayuthaya;
}

You can include any styling you want in the style. If you wanted to increase the font size too, you’d change the mystyle1 section to look like:

.mystyle1 {
font-family: ayuthaya;
font-size: 30px;
}

It’s also possible to bundle custom fonts with your deck, so you don’t need to install them on your computer or mobile device. Please see the[installing fonts](https://apps.ankiweb.net/docs/manual.html#installingfonts) section for more info.

Please see the [card styling](https://apps.ankiweb.net/docs/manual.html#cardstyling) section for more information on the styling options you can use here.

### Hint Fields

It’s possible to add a field to the front or back of a card, but make it hidden until you explicitly show it. We call this a *hint field*. Before adding a hint, please bear in mind that the easier you make it to answer a question in Anki, the less likely you are to remember that question when you encounter it in real life. Please have a read about the *minimum information principle* on http://www.supermemo.com/articles/20rules.htm before proceeding.

First, you’ll need to add a field to store the hint in if you have not already. Please see the [fields](https://apps.ankiweb.net/docs/manual.html#fields) section if you’re not sure how to do this.

Assuming you’ve created a field called MyField, you can tell Anki to include it on the card but hide it by default by adding the following to your template:

{{hint:MyField}}

This will show a link labeled “show hint”; when you click it, the content of the field will be displayed on the card. (If MyField is empty, nothing will be shown.)

If you show the hint on the question and then reveal the answer, the hint will be hidden again. If you want to have the hint always revealed when the answer is shown, you will need to remove {{FrontSide}} from your back template and manually add the fields you wish to appear.

|     |     |
| --- | --- |
| Note | It is not currently possible to use a hint field for audio — the audio will play regardless of whether you’ve clicked on the hint link. |

If you want to customize the appearance or behaviour, you’ll need to implement the hint field yourself. We can not provide any support for doing so, but the following code should get you started:

{{#Back}}
﻿<a class=hint href="#"

onclick="this.style.display='none';document.getElementById('hint4753594160').style.display='inline-block';return false;">

Show Back</a><div id="hint4753594160" class=hint style="display: none">{{Back}}</div>

{{/Back}}

### Special Fields

There are some special fields you can include in your templates:
The note's tags: {{Tags}}
The type of note: {{Type}}
The card's deck: {{Deck}}
The card's subdeck: {{Subdeck}}
The type of card ("Forward", etc): {{Card}}
The content of the front template (only valid in back template): {{FrontSide}}

FrontSide will not include any audio that was on the front side of the card. If you wish to have the same audio play on both the front and back of the card, you’ll need to manually include the audio fields on the back as well.

As with other fields, special field names are case sensitive.

### Card Generation & Deletion

Anki will not create cards with empty front sides. Thus if “My Field” was empty, and one card’s front template included only that field, the card would not be created.

If no cards can be created because all of the cards would have empty front sides, then the Add Notes window will warn you and not allow the note to be added until at least one card would be generated.

When you edit a previously added note, Anki will automatically create extra cards if they were previously blank but no longer are. If your edits have made some cards blank when they previously were not, however, Anki will not delete them immediately, as that could lead to accidental data loss. To remove the empty cards, go to Tools → Empty Cards in the main window. You will be shown a list of empty cards and be given the option to delete them.

Because of the way that card generation works, it is not possible to manually delete individual cards (they would just end up being recreated the next time the note was edited). Instead, you should make the relevant conditional replacement fields empty and then use the Empty Cards option. (If you don’t have fields set up to control card generation, please see the sections on[reversed cards](https://apps.ankiweb.net/docs/manual.html#reversingcards) and [selective card generation](https://apps.ankiweb.net/docs/manual.html#selectivegeneration).) If you need to do this for many notes at once, you can use the[find and replace](https://apps.ankiweb.net/docs/manual.html#findreplace) feature in the browser.

Anki does not consider special fields or non-field text for the purposes of card generation. Thus if your front template looked like the following, no card would be generated if Country was empty:

Where is {{Country}} on the map?

### Selective Card Generation

Please read the previous section on [card generation and deletion](https://apps.ankiweb.net/docs/manual.html#cardgeneration) before you read this.

Sometimes you may want to generate extra cards for only some of your material, such as testing your ability to recall the most important words of a set. You can accomplish this by adding an extra field to your note, and adding some text into it (such as "1") on the notes you want the extra card. Then in the card template, you can make the card’s creation depend on that field being non-empty. For more information on this, please see the conditional replacement section below.

### Media & LaTeX References

Anki does not scan templates for media references, because it is slow to do so. This has implications for including media on the template.

#### Static Sounds/Images

If you wish to include images or sounds on your cards that are the same for every card (eg, a company logo at the top of each card):

1. Rename the file so it starts with an underscore, eg "_logo.jpg". The underscore tells Anki that the file is used by the template and it should be exported when sharing the deck.

2. Add a reference to the media on your front or back template, like:
<img src="_logo.jpg">

#### Field References

Media references to fields are not allowed. They may or may not display during review, and will not work when checking for unused media, importing/exporting, and so on. Examples that won’t work:

<img src="{{Expression}}.jpg">
[sound:{{Word}}]
[latex]{{Field 1}}[/latex]

Instead, you should include the media references in the field. Please see the [importing](https://apps.ankiweb.net/docs/manual.html#importing) section for more information.

### Conditional Replacement

It is possible to include certain text, fields, or HTML on your cards only if a field is empty or not empty. An example:

This text is always shown.
{{#FieldName}}
This text is only shown if FieldName has text in it
{{/FieldName}}
{{^FieldName}}
This text is only shown if FieldName is empty
{{/FieldName}}
A real life example is only showing a label if the field is not empty:
{{#Tags}}Tags: {{Tags}}{{/Tags}}

Or say you want to display a specific field in blue on the front of your card if there are extra notes on the back (perhaps the fact that there are notes serves as a reminder that you should spend more time thinking about the answer). You can style the field as follows:

{{#Notes}}<span style="color:blue;">{{/Notes}}
{{FieldToFormat}}
{{#Notes}}</span>{{/Notes}}

You can also use conditional replacement to control which cards are generated. This works since Anki will not [generate cards](https://apps.ankiweb.net/docs/manual.html#cardgeneration) which would have a blank front side. For example, consider a card with two fields on the front:

{{Expression}}
{{Notes}}

Normally a card would be generated if either the expression or notes field had text in it. If you only wanted a card generated if expression was not empty, then you could change the template to this:

{{#Expression}}
{{Expression}}
{{Notes}}
{{/Expression}}

And if you wanted to require both fields, you could use two conditional replacements:

{{#Expression}}
{{#Notes}}
{{Expression}}
{{Notes}}
{{/Notes}}
{{/Expression}}

Keep in mind that, as mentioned in the [card generation](https://apps.ankiweb.net/docs/manual.html#cardgeneration)section, this only works when you place the conditional replacement code on the*front* of the card; if you do this on the back, you will simply end up with cards with a blank back side. Similarly, since this works by checking if the front field would be empty, it is important to make sure you wrap the *entire* front side in the conditional replacement; for instance, the following would not work as expected:

{{#Expression}}
{{Expression}}
{{/Expression}}
{{Notes}}

The default behaviour can be thought of as an "OR" condition - cards are created if the first field is non-empty, OR the second field is non-empty, and so on. The behaviour above can be thought of as an "AND" condition - cards are created if the first field is non-empty AND the second field is non-empty, and so on.

A caveat: Anki is not currently able to mix AND and OR conditions. Thus the following template, which says "require expression and notes, or field 3", would not work:

{{#Expression}}
{{#Notes}}
{{Expression}}
{{Notes}}
{{/Notes}}
{{/Expression}}
{{Field 3}}

Another caveat is that negated expressions can not be used to control card generation. That is, wrapping a template in {{^Field}} will not do what you expect.

### Cloze Templates

Please see the [cloze deletion](https://apps.ankiweb.net/docs/manual.html#cloze) section for background info.

The cloze note type functions differently from regular note types. Instead of a customizable number of card types, it has a single type which is shared by all cloze deletions on a note.

As mentioned in the card generation section above, generation of regular cards depends on one or more fields on the question being non-empty. Cloze deletion note types are generated differently:

- Anki looks on the front template for one or more cloze replacements, like {{cloze:FieldName}}.
- It then looks in the FieldName field for all cloze references, like {{c1::text}}.
- For each separate number, a card will be generated.

Because card generation functions differently for cloze deletion cards, {{cloze:…}} tags can not be used with a regular note type - they will only function properly when used with a cloze note type.

Conditional generation provides a special field so you can check which card you are rendering. If you wanted to display the "hint1" field on the first cloze, and "hint2" field on the second cloze for example, you could use the following template:

{{cloze:Text}}
{{#c1}}
{{Hint1}}
{{/c1}}
{{#c2}}
{{Hint2}}
{{/c2}}

### Other HTML

Your templates can contain arbitrary HTML, which means that all the layout possibilities used on internet web pages can also be used on your cards. Things like tables, lists, images, links to external pages and so on are all supported. With tables for example, you could change the layout so that the front and back of a card appear on the left and right instead of the top and bottom.

Covering all of HTML’s features is outside the scope of this manual, but there are plenty of good introductory guides to HTML available on the web if you’d like to learn more.

### Dictionary Links

You can also use field replacement to create dictionary links. Imagine you’re studying a language and your favourite online dictionary allows you to search for text using a web URL like:

http://example.com/search?q=myword
You could add an automatic link by doing the following in your template:
{{Expression}}
<a href="http://example.com/search?q={{Expression}}">check in dictionary</a>

The template above would allow you to search for each note’s expression by clicking on the link while reviewing. There is a caveat however, so please see the next section.

### HTML Stripping

Like templates, fields are stored in HTML. In the dictionary link example above, if the expression contained the word "myword" without any formatting, then the HTML would be the same: "myword". But when you include formatting in your fields, extra HTML is included. If "myword" was bolded for example, the actual HTML would be "<b>myword</b>".

This can present a problem for things like dictionary links. In the above example, the dictionary link would end up being:

<a href="http://example.com/search?q=<b>myword</b>">check in dictionary</a>

The extra characters in the link would likely confuse the dictionary site, and you’re likely not to get any matches.

To solve this, Anki provides the ability to strip formatting from fields when they are replaced. If you prefix a field name with text:, Anki will not include any formatting. So a dictionary link that worked even with formatted text would be:

<a href="http://example.com/search?q={{text:Expression}}">check in dictionary</a>

### Browser Appearance

If your card templates are complex, it may be difficult to read the question and answer columns (called "Front" and "Back") in the [card list](https://apps.ankiweb.net/docs/manual.html#cardlist). The "browser appearance" option allows you to define a custom template to be used only in the browser, so you can include only the important fields and change the order if you desire. The syntax is the same as in standard card templates.

### RTL (right to left) text

If you’re learning a language that reads from right to left, you’ll need to adjust the template like so:

<div dir=rtl>{{FieldThatHasRTLTextInIt}}</div>

If you were linked directly here, please see the start of this section for more information.

### Platform-Specific CSS

Anki defines some special CSS classes that allow you to define different styling for different platforms. The example below shows how to vary the font depending on where you’re reviewing:

.win .jp { font-family: "MS Mincho"; }
.mac .jp { font-family: "Hiragino Mincho Pro"; }
.linux .jp { font-family: "Kochi Mincho"; }
.mobile .jp { font-family: "Hiragino Mincho ProN"; }
And in the template:
<div class=jp>{{Field}}</div>
For different iOS devices, you can use *.iphone* and *.ipad*.

You can also use properties like .gecko, .opera, and .ie to select particular browsers when using AnkiWeb. Please seehttp://rafael.adm.br/css_browser_selector/ for a full list of options.

### Installing Fonts

If you’re using Anki on a work or school computer where you don’t have permission to install new fonts, or you’re using Anki on a mobile device, it’s possible to add fonts directly to Anki.

To add a font to Anki, it must be in the TrueType format. TrueType fonts have a filename ending in .ttf, such as "Arial.ttf". Once you’ve located a TrueType font, we’ll need to add it to the media folder:

1. Rename the file, adding an underscore at the start, so it becomes like "_arial.ttf". Adding an underscore will tell Anki that this file will be used on a template, and should not be deleted when checking for unused media.

2. In your computer’s file browser, go to your [Anki Folder](https://apps.ankiweb.net/docs/manual.html#files), and then a folder called "User 1" (or your profile name if you’ve renamed/added profiles).

3. Inside the folder, you should see a folder called collection.media. Drag the renamed file to that folder.

After that, we need to update the template:

1. Click **Add** at the top of the main screen, and then select the note type you want to change with the top left button.

2. Click **Cards**.

3. In the styling section, add the following text to the bottom (after the last "}" character), replacing "_arial.ttf" with the name of the file you copied into your media folder:

@font-face { font-family: myfont; src: url('_arial.ttf'); }

|     |     |
| --- | --- |
| Note | Only change the "arial" part, not the "myfont" part. |

After that, you can either change the font for the entire card, or for individual fields. To change the font for the entire card, simply locate the font-family: line in the .card section and change the font to "myfont". To change the font for only certain fields, please see the [Field Styling](https://apps.ankiweb.net/docs/manual.html#fieldstyling) instructions above.

|     |     |
| --- | --- |
| Note | Please make sure the filenames match exactly. If the file is called arial.TTF and you write arial.ttf in your card templates, it will not work. |

#### Fonts on a Mac

Embedded fonts currently do not work on OS X. It is still possible to use custom fonts, but they need to be installed system wide.

To install a font on your system, please see http://support.apple.com/kb/HT2435?viewlocale=en_US&locale=en_US

You can set up Anki to use the system font on a Mac computer, and an embedded font elsewhere.

On your front or back template, wrap the field you want to style in the following code, replacing "FieldName" with the name of your field.

<span class="mystyle">{{FieldName}}</span>

In the styling section, in addition to the font-face line described above, add the following:

.mystyle { font-family: myfont; }
.mac .mystyle { font-family: Helvetica; }

Replace "Helvetica" with the name of the font you installed on your system. Keep "myfont" as is, as it references the font you embedded.

### Night Mode

You can customize the way templates appear when night mode is enabled in the preferences screen.

If you wanted a grey background instead of black, you could use something like:
.card.nightMode { background-color: #555; }

If you have a *myclass* style, the following would show the text in yellow when night mode is enabled:

.nightMode .myclass { color: yellow; }

### Javascript

As Anki cards are treated like webpages, it is possible to embed some Javascript on your cards via inline script tags in the template (loading external files using src= is not supported).

Because Javascript is an advanced feature and so many things can go wrong,**Javascript functionality is provided without any support or warranty**. We can not provide any assistance with writing Javascript, and can not guarantee any code you have written will continue to work without modification in future Anki updates. If you are not comfortable addressing any issues you encounter on your own, then please avoid using Javascript.

Each Anki client may implement card display differently, so you will need to test the behaviour across platforms. A number of clients are implemented by keeping a long running webpage and dynamically updating parts of it as cards are reviewed, so your Javascript will need to update sections of the document using things like document.getElementById() rather than doing things like document.write().

Functions like window.alert are also not available. Anki will write javascript errors to the terminal, so if you’re running on a Mac or Windows computer, you’ll need to manually catch the errors and write them to the document to see them. There is no debugger available, so to figure out problems you’ll need to break down your code until you discover which parts are causing problems.

## Profiles & Preferences

### Profiles

If more than one person wants to use Anki on your computer, you can set up a separate profile for each user. Each user profile has their own collection, and own program settings. Profiles are configured by going to the File menu and choosing "Switch Profile".

|     |     |
| --- | --- |
| Note | Profiles are intended to be used by different people, and each AnkiWeb account can only keep one profile in sync. For dividing up your own content, you should use separate decks rather than separate profiles, except when using extra profiles for experimenting with changes you don’t plan to sync to other devices. |

### Preferences

The preferences are available from the Tools menu on Windows/Linux, or the Anki menu on a Mac. If you have multiple profiles, any changes you make will apply only to the current profile.

**Basic**

By default Anki pastes images on the clipboard as JPG files, to save disk space. You can use the **Paste clipboard images as PNG** option to paste as PNG images instead. PNG images support transparent backgrounds and are lossless, but they usually result in much larger file sizes.

When **night mode** is enabled, Anki will show cards as white text on a black background. Some card templates may need to be modified to work properly with this option enabled - please see [night mode styling](https://apps.ankiweb.net/docs/manual.html#nightmode)for more information.

The **experimental V2 scheduler** is documented here:https://anki.tenderapp.com/kb/anki-ecosystem/experiment-scheduling-changes-in-anki-21

The first drop-down box controls how note types and decks interact. The default of "When adding, default to current deck" means that Anki saves the last-used note type for each deck and selects it again then next time you choose the deck (and, in addition, will start with the current deck selected when choosing Add from anywhere). The other option, "Change deck depending on note type," saves the last-used deck for each note type (and opens the add window to the last-used note type when you choose Add). This may be more convenient if you always use a single note type for each deck.

The second drop-down box controls when new cards are shown: either mixed with, before, or after all reviews.

The **Next day starts at** option controls when Anki should start showing the next day’s cards. The default setting of 4AM ensures that if you’re studying around midnight, you won’t have two days' worth of cards shown to you in one session. If you stay up very late or wake up very early, you may want to adjust this to a time you’re usually sleeping.

The **Learn ahead limit** tells Anki how to behave when there is nothing left to study in the current deck but cards in learning. The default setting of 20 minutes tells Anki that cards should be shown early if they have a delay of less than 20 minutes and there’s nothing else to do. If you set this to 0, Anki will always wait the full delay, showing the congratulations screen until the remaining cards are ready to be reviewed.

Timeboxing is a technique to help you focus by dividing a longer activity (such as a 30 minute study session) into smaller blocks. If you set the**timebox time limit** to a non-zero number of minutes, Anki will periodically show you how many cards you’ve managed to study during the prescribed time limit.

## Deck Options

Deck options are accessed by selecting a deck on the *Decks* screen, and then clicking *Options* at the bottom of the screen.

Anki allows you to share options between different decks, to make updating options in many decks at once easy. To do this, options are grouped into an*options group*. By default, all newly created decks use the same options group, and decks imported from previous versions of Anki have separate option groups. If you’d like to alter the settings on one deck but not other decks, click the gears icon in the top right and add a new options group.

Please only change options that you fully understand, as inappropriate adjustments may render Anki less effective.

|     |     |
| --- | --- |
| Note | Options are not retroactive. For example, if you change an option that controls the delay after failing a card, cards that you failed prior to changing the option will have the old delay, not the new one. |

### New Cards

**Steps** controls the number of learning repetitions, and the delay between them. Please see the [learning](https://apps.ankiweb.net/docs/manual.html#learning) section for an overview of how the steps work.

Steps over a day (1440 minutes) are supported as well - if you want, you can define a schedule like 10 minutes, 1 day, 3 days and then finally 7 days before the card becomes a review card.

|     |     |
| --- | --- |
| Note | If there’s nothing else to study, Anki will show cards up to 20 minutes early by default. The amount of time to look ahead is configurable in the[preferences](https://apps.ankiweb.net/docs/manual.html#preferences). One thing to be aware of is that the due counts will differ between the deck screen and study screens in this case. The deck screen will not count cards that are not ready, but the study screen will. This is done so that you can tell which decks need your attention. |

|     |     |
| --- | --- |
| Note | Anki treats small steps and steps that cross a day boundary differently. With small steps, the cards are shown as soon as the delay has passed, in preference to other waiting cards like reviews. This is done so that you can answer the card as closely to your requested delay as possible. In contrast, cards that cross a day boundary are scheduled on a per-day basis like reviews are. When you return to study the next day, the per-day learning cards will not be shown first, as that can make the first half of a review session frustratingly difficult. Instead, the cards will be shown after reviews are completed. They are included in the review count rather than the learning count, due to the way they are handled internally. |

**Order** controls whether Anki should add new cards into the deck randomly, or in order. When you change this option, Anki will re-sort the decks using the current option group. One caveat with random order mode: if you review many of your new cards and then add more new cards, the newly added material is statistically more likely to appear than the previously remaining cards. To correct this, you can change the order to ordered mode and back again to force a re-sort.

|     |     |
| --- | --- |
| Note | When you select random order, Anki will randomize your notes, keeping the cards of a given note close together. The cards of a given note are shown in the order their card types appear in, so that siblings are introduced consistently - otherwise you could end up in a state where some notes had all their cards introduced and other notes had only one or two. Please see the "bury related" option below for more info. |

**New cards/day** tells Anki how many new cards you’d like introduced on each day you open the program. Missed days will not cause the cards to pile up. The limit applies to the current deck and subdecks. This means if "French" has a limit of 20 cards and "French::Lesson 1" and "French::Lesson 2" both have limits of 15 cards, you’ll get 15 cards from lesson 1 but only 5 cards from lesson 2.

|     |     |
| --- | --- |
| Note | Studying new cards will temporarily increase the number of reviews you need to do a day, as freshly learnt material needs to be repeated a number of times before the delay between repetitions can increase appreciably. If you are consistently learning 20 new cards a day, you can expect your daily reviews to be roughly about 200 cards/day. You can decrease the reviews required by introducing fewer new cards each day, or by turning off new card display until your review burden decreases. More than one Anki user has excitedly studied hundreds of new cards over their first few days of using the program, and then become overwhelmed by the reviews required. |

**Graduating interval** is the delay between answering *Good* on a card with no steps left, and seeing the card again.

**Easy interval** is the delay between answering *easy* on a learning card and seeing it in review mode for the first time.

**Starting ease** controls the easiness that cards start out with. It is set when a card graduates from learning for the first time. It defaults to 250%, meaning that once you’ve finished learning a card, answering "Good" on subsequent reviews will increase the delay by approximately 2.5x (eg if the last delay was 10 days, the next delay would be 25 days). Based upon how you rate the card in subsequent reviews, the easiness may increase or decrease from what it starts out as.

Turning off **bury related…** will prevent Anki from [burying siblings](https://apps.ankiweb.net/docs/manual.html#siblings), and instead Anki will just try to avoid showing siblings directly after one another in the same session. For this to work, your new cards/day setting needs to be large enough for the cards of multiple notes to be included.

### Reviews

**Maximum reviews/day** allows you to set an upper limit on the number of reviews to show each day. When this limit is reached, Anki will not show any more review cards for the day, even if there are some waiting. If you study consistently, this setting can help to smooth out occasional peaks in due card counts, and can save you from a heart attack when returning to Anki after a week off. When reviews have been hidden due to this option, a message will appear in the congratulations screen, suggesting you consider increasing the limit if you have time.

**Easy bonus** allows you to set the difference in intervals between answering*Good* and *Easy* on a card. For instance, with the default value of 130%, Easy will give an interval that is 1.3 times the Good interval.

**Interval modifier** allows you to apply a multiplication factor to the intervals Anki generates. At its default of 100% it does nothing; if you set it to 80% for example, intervals will be generated at 80% of their normal size (so a 10 day interval would become 8 days). You can thus use the multiplier to make Anki present cards more or less frequently than it would otherwise, trading study time for retention or vice versa.

For moderately difficult material, the average user should find they remember approximately 90% of mature cards that come up for review. You can find out your own performance by opening the graphs/statistics for a deck and looking at the Answer Buttons graph - mature retention is the correct% on the right side of the graph. If you haven’t been studying long you may not have any mature cards yet. As performance with new cards and younger cards can vary considerably, it’s a good idea to wait until you have a reasonable amount of mature reviews before you start drawing conclusions about your retention rate.

On the SuperMemo website, they suggest that you can find an appropriate multiplier for a desired retention rate. Their formula boils down to:

log(desired retention%) / log(current retention%)

Imagine we have a current retention rate of 85% and we want to increase it to 90%. We’d calculate the modifier as:

log(90%) / log(85%) = 0.65

You can use Google to [calculate it](https://www.google.com/search?q=log(90%25)+%2F+log(85%25)) for you.

If you plug the resulting 65% into the interval modifier, you should find over time that your retention moves closer to your desired retention.

One important thing to note however is that the tradeoff between time spent studying and retention is not linear: we can see here that to increase our retention by 5 percentage points, we’d have to study 35% more frequently. If the material you are learning is very important then it may be worth the extra effort – that’s something you’ll need to decide for yourself. If you’re simply worried that you’re forgetting too much, you may find investing more time into the initial learning stage and/or making mnemonics gives you more gain for less effort.

One final thing to note is that Anki forces a new interval to be at least 1 day longer than it was previously so that you don’t get stuck reviewing with the same interval forever. If your goal is to repeat a card once a day for multiple days, you can do that by setting more learning mode steps instead of by adjusting this modifier.

**Maximum interval** allows you to place an upper limit on the time Anki will wait to reshow a card. The default is 100 years; you can decrease this to a smaller number if you’re willing to trade extra study time for higher retention.

**Hard interval** specifies what the next interval will be when you press the Hard button. The percentage is relative to the previous interval, eg with a default 120%, a card with a 10 day interval will be given 12 days. This option is only available when the experimental scheduler is enabled in the preferences.

Turning off **bury related…** will prevent Anki from [burying siblings](https://apps.ankiweb.net/docs/manual.html#siblings), and instead Anki will just try to avoid showing siblings directly after one another in the same session.

|     |     |
| --- | --- |
| Note | Review cards are always shown in random order. If you wish to see them in a different order, you can use a [filtered deck](https://apps.ankiweb.net/docs/manual.html#filtered). More specifically, Anki randomizes reviews by grabbing batches of 50 cards in the order that they exist in the database, randomizing each batch, then putting them together. This means that there is a slight bias towards older cards being shown first, but it prevents individual cards from showing up in a predictable order. |

### Lapses

When you forget a review card, it is said to have *lapsed*. The default behaviour for lapsed reviews is to reset the interval to 1 (ie, make it due tomorrow), and put it in the learning queue for a refresher in 10 minutes. This behaviour can be customized with the options listed below.

If you leave the steps blank, Anki will not place the card back in the learning queue, and it will be rescheduled as a review with its new interval determined by the settings below.

|     |     |
| --- | --- |
| Note | The new interval is determined when you answer "Again" to a review card, not when the card finishes its relearning steps. For this reason, the "Good" and "Easy" buttons during relearing do not alter the interval again - they only control which step you are on. If there is only a single step (the default), the "Easy" button will be hidden, since it would accomplish the same thing as the "Good" button. If you have 2 or more steps, "Easy" is not hidden, to allow you to graduate cards from the queue before all of their steps are finished. |

*New interval* controls how much Anki should reduce the previous interval. It reduces the previous interval to the percentage you specify. If a card had a 200 day interval, the default of 0% would reduce the interval to 0 (but see the next option). If you set this option to 50%, the card would have its interval reduced to 100 days instead.

*Minimum interval* allows you to apply a minimum limit to the above option. The default setting says that lapses should be reviewed one day later. The interval must be 1 day or more.

The leech options control the way Anki handles leeches. Please see the leech section for more information.

### General

Anki monitors how long it takes you to answer each question so that it can show you how long was spent studying each day. The time taken does not influence scheduling. If you take longer than 60 seconds, Anki assumes you have walked away from your computer or have been distracted, and limits the recorded time to 60 seconds, so that you don’t end up with inaccurate statistics. The *ignore answer times…* option allows you to adjust the cutoff threshold. The minimum cutoff is 30 seconds.

If *show answer timer* is checked, Anki will display the current time taken for each card in the study area.

By default, Anki automatically plays audio on the front and back of cards. If you uncheck *automatically play audio*, Anki will not play audio until you press the replay audio key, r or F5.

The *when answer shown, replay both question and answer audio* option controls what happens when you choose to replay audio while the answer is shown. Please note that it does not control what happens when you show the answer; for that please see [this section](https://apps.ankiweb.net/docs/manual.html#specialfields).

### Description

This section allows you to edit the deck description, which is shown in the study overview. The description is automatically set when downloading shared decks. You can delete all the text in the description if you no longer want to see it in the study overview area.

You can also use HTML in the description—anything that works on a note should be valid.

## AnkiWeb and Synchronization

AnkiWeb is a service that allows you to keep your collection synchronized across multiple devices, and to study online. Please sign up for a [free account](https://ankiweb.net/) before following the steps below.

### Setup

To start syncing your collection across devices, click the sync button (the top right one on the main screen), or press *y* on your keyboard. You’ll be prompted for your AnkiWeb ID and password, which you created in the signup process.

When you synchronize your collection for the first time, Anki will ask you if you want to upload or download. If you have cards on your computer and your AnkiWeb account is empty, choose "upload" to send your data to AnkiWeb. If you have cards on AnkiWeb from another device, and no cards on your computer, choose "download" to replace the empty local collection with the cards that are on AnkiWeb. If you have different cards on both devices,[more work is required](https://apps.ankiweb.net/docs/manual.html#mergingconflicts) to avoid losing data.

Once the initial one way sync is completed, Anki will be able to merge changes from multiple locations with a few exceptions.

|     |     |
| --- | --- |
| Note | If you have multiple people using Anki on one machine and have created a profile for each user, each user will need to create their own AnkiWeb account to sync with. If you attempt to synchronize multiple profiles with a single AnkiWeb account, you will lose data. |

### Automatic Syncing

Once syncing is enabled, Anki will automatically sync each time your collection is closed or opened. If you would prefer to synchronize manually, you can disable automatic syncing in Anki’s preferences.

### Media

Anki will synchronize any sounds and images used by your notes. It will notice when media has been added or removed from your media folder, but will not notice if you have edited some existing files without adding or removing any. To get your edits noticed, you need to add or remove a file as well.

|     |     |
| --- | --- |
| Note | If you’re running Anki off a USB flash drive, you should use an NTFS file system, as Anki may not be able to detect media changes on a FAT32 filesystem. |

### Conflicts

Reviews and note edits can be merged, so if you review or edit on two different devices before syncing, Anki will preserve your changes from both locations. If the same card has been reviewed in two different locations, both reviews will be marked in the revision history, and the card will be kept in the state it was when it was most recently answered.

There are certain changes that Anki is unable to merge. These mainly relate to the format of notes: things like adding a new field, or removing a card template. When you perform an operation that can’t be merged, Anki will warn you, and give you the option of aborting the operation. If you choose to continue, you’ll be asked to choose whether to keep the local copy or the copy on AnkiWeb when your collection is next synchronized.

If you choose Upload to make the content on AnkiWeb a copy of the content on your local device, you then need to sync any other devices you use, and choose Download, so they too have the same content. Once all devices have the same content, future syncs will be able to merge again.

If you wish to force a full upload or download (for example, because you accidentally deleted a deck on one side and want to restore the deck rather than having its deletion synchronized), you can check the "On next sync, force changes in one direction" box in Tools>Preferences>Network, then sync as usual. (You’ll be given the option to choose which side you want to use.)

|     |     |
| --- | --- |
| Note | Forcing a one way sync only affects card syncing - media is synced as normal. If you have files that you want to remove from AnkiWeb, please ensure your client is fully in sync first. After syncing is up to date, any files you remove (eg via the Check Media function) will be removed from AnkiWeb on the following sync. |

### Merging Conflicts

Because the [first sync](https://apps.ankiweb.net/docs/manual.html#syncingsetup) can only sync changes in one direction, if you have added different content to different devices or profiles before setting syncing up, content on one device will be lost if you overwrite it with the content from the other device. With some work, it is possible to manually merge data into a single collection.

Start by taking a backup on each device/profile, in case something goes wrong. With the computer version you can use File>Export to export "all decks" with scheduling information and media files included, and save the file somewhere safe. In AnkiMobile, the Add/Export button on the decks list screen will let you export all decks with media.

Next, if one of your devices is a mobile device, synchronize it first. If there’s a conflict, choose "upload" to overwrite any existing data on AnkiWeb with the data from your mobile device. If both devices/profiles are on your computer, synchronize the device/profile with the most number of decks first.

Now return to the other device/profile. If automatic syncing is enabled, a message may pop up asking if you want to upload or download. Click the cancel button - we don’t want to sync yet.

Once you’re looking at the deck list, click the cog icon next to the first deck, and choose "export". Export the content with scheduling information and media included, and save the .apkg file somewhere. Now you’ll need to repeat this for each top-level deck.

Once all top-level decks have been exported, click the sync button at the top right, and choose "download", which will overwrite the local content with the content you synced from your other device.

You can now use File>Import to import the .apkg files you exported earlier, which will merge the exported content with the existing content, so everything will be in one place.

### Firewalls

Anki needs to be able to make outbound HTTPS connections to sync. At a minimum it must be able to connect to ankiweb.net, sync.ankiweb.net and syncN.ankiweb.net, where N is number between 3 and 6. These domains may change over time, and the IP addresses they point to may also change, so we recommend you allow wildcard access to *.ankiweb.net to reduce the chance of the firewall rules needing to be updated in the future.

If you have a firewall on your machine, you should add an exception for Anki. If you are on a work or school network, please contact your network administrator for assistance - it is not something we can help you with.

### Proxies

If you need a proxy to access the internet, Anki should automatically pick up your system proxy settings if you’re on Windows or OS X, and will honour the HTTP_PROXY environment variable if you’re on another platform.

Please note that advanced proxy setup via .pac or .wpad files is not supported in Anki.

To override the system proxy settings on Windows or OS X, define a HTTP_PROXY environmental variable that points to the proxy server. It will look like:

http://user:pass@proxy.company.com:8080

If your username or password contains an @ (eg [user@workdomain.com](https://apps.ankiweb.net/docs/manual.html#intro-videosmailto:user@workdomain.com)), you need to change it to %40, like so:

http://user%40workdomain.com:pass@proxy.company.com:8080

|     |     |
| --- | --- |
| Note | Anki 2.1 expects to find HTTPS_PROXY instead of HTTP_PROXY. |

To set environmental variables on Windows, please seehttps://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/sysdm_advancd_environmnt_addchange_variable.mspx?mfr=true

If you’re on a Mac, please see http://stackoverflow.com/questions/135688/setting-environment-variables-in-os-x

|     |     |
| --- | --- |
| Note | The toolkit Anki is built on is unfortunately not currently able to pick up your proxy username and password from your system settings. This means that if you use a proxy that requires authentication, syncing will fail. In this case, you will need to use an environmental variable that defines your proxy details as described above, or use a personal proxy server that you route traffic through, which in turn connects to the upstream proxy that requires authentication. |

|     |     |
| --- | --- |
| Note | Heavily locked down networks that intercept secure connections and present their own certificate instead may cause Anki to throw up SSL errors. We do not support using Anki in such environments. |

## Browser

The browser (which has nothing to do with web browsers such as Mozilla Firefox) allows you to search through your cards and notes and edit them. It is opened by clicking on *Browse* in the main window, or by pressing *b* on your keyboard. It is comprised of three sections: the *sidebar* on the left, the*card list* on the top right, and the *current note* on the bottom right. By positioning the mouse between two sections, it is possible to click and drag to expand one section and shrink another.

### Sidebar

The sidebar on the left allows quick access to common search terms. Various search terms as described below are listed, along with all deck names and tag names. Clicking on an item will search for it.

You can hold down Ctrl (command on a Mac) and click in order to append the clicked item to the current search with an AND condition, instead of starting a new search. If you wanted to show learning cards that were also in the German deck for instance, you could click on "Learning", then ctrl+click on "German".

You can hold down Shift to create an OR search instead of an AND. For example, you could click one deck, then shift-click another to show cards from either of the decks in the same view.

You can hold down Alt (option on a Mac) in order to reverse the search (prepend a *-*) – for instance, to show all cards in a current deck that do *not* have a certain tag. Alt/option can be combined with either Ctrl or Shift (e.g., Ctrl-Alt-clicking will result in adding a new search term that is negated).

To remove tags that are not used by any notes, use Tools>Check Database from the main window.

### Searching

Above the card list is a search box. You can type in various things there to search for cards. (If you’d rather select what you’re looking for in a list, please take a look at the [sidebar](https://apps.ankiweb.net/docs/manual.html#sidebar) section above.)

#### Simple searches

When you type some text into the search box, Anki finds matching notes and displays their cards. Anki searches in all fields of the notes, but does not search for tags (see later in this section for how to search for tags). Some examples:

dog
search for "dog" - will match words like "doggy" and "underdog" too
dog cat
finds notes with both "dog" and "cat", such as "a dog and cat"
dog or cat
finds notes with either "dog" or "cat"
dog (cat or mouse)
finds notes with dog and cat, or dog and mouse
-cat
finds notes without the word "cat".
-cat -mouse
finds notes with neither "cat" nor "mouse".
-(cat or mouse)
same as the above.
"a dog"
finds notes with the exact phrase "a dog" on them
-"a dog"
finds notes without the exact phrase "a dog"
d_g
finds notes with d, <a letter>, g, like dog, dig, dug, and so on.
d*g
finds notes with d, <zero or more letters>, g, like dg, dog, dung, etc.
Things to note from the above:

- Search terms are separated by spaces.
- When multiple search terms are provided, Anki looks for notes that match all of the terms.
- You can use "or" if you only need one of the terms to match.
- You can prepend a minus sign to a term to find notes that don’t match.
- If you want to search for something including a space or parenthesis, enclose it in quotes.
- You can group search terms by placing them in parentheses, as in the **dog (cat or mouse)** example. This becomes important when combining OR and AND searches — in the example, with the parentheses, it matches either *dog cat* or *dog mouse*, whereas without them it would match either *dog and cat* or *mouse*.
- Anki is only able to search within formatting in the [sort field](https://apps.ankiweb.net/docs/manual.html#fields) you’ve configured. For example, if you add "**exa**mple" to one of your fields, this will not be matched when searching for "example" unless that field is the sort field. If a word is not formatted, or the formatting does not change in the middle of the word, then Anki will be able to find it in any field.

#### Limiting to a field

You can also ask Anki to match only if a particular field contains some text. Unlike the searches above, searching on fields requires an *exact match* by default.

front:dog

find notes with a Front field of exactly "dog". A field that says "a dog" will not match.

front:*dog*
find notes with Front field containing dog somewhere
front:
find notes that have an empty Front field
front:_*
find notes that have a non-empty Front field
front:*
find notes that have a Front field, empty or not

#### Tags, decks, cards and notes

tag:animal
find notes with the tag "animal"
tag:none
find notes with no tags
tag:ani*
find notes with tags starting with ani
deck:french
find cards in a French deck, or subdecks like French::Vocab
deck:french -deck:french::*
find cards in French, but not subdecks
deck:"french vocab"
searching when a deck has a space
"deck:french vocab"
also ok
deck:filtered
filtered decks only
-deck:filtered
normal decks only
card:forward
search for Forward cards
card:1

search for cards by template number - eg, to find the second cloze deletion for a note, you’d use card:2

note:basic
search for cards with a Basic note type

#### Card state

is:due
review cards and learning cards waiting to be studied
is:new
new cards
is:learn
cards in learning
is:review
reviews (both due and not due) and lapsed cards
is:suspended
cards that have been manually suspended
is:buried

cards that have been buried, either [automatically](https://apps.ankiweb.net/docs/manual.html#siblings) or manually

Cards that have lapsed fall into several of these categories, so it may be useful to combine them to get more precise results:

is:learn is:review
cards that have lapsed and are awaiting relearning
-is:learn is:review
review cards, not including lapsed cards
is:learn -is:review
cards that are in learning for the first time

#### Card properties

prop:ivl>=10
cards with interval of 10 days or more
prop:due=1
cards due tomorrow
prop:due=-1
cards due yesterday that haven’t been answered yet
prop:due>-1 prop:due<1
cards due between yesterday and tomorrow
prop:reps<10
cards that have been answered less than 10 times
prop:lapses>3
cards that have moved into relearning more than 3 times
prop:ease!=2.5
cards easier or harder than default

Note that due only matches review cards and learning cards with an interval of a day or more: cards in learning with small intervals like 10 minutes are not included.

#### Recently added

added:1
cards added today
added:7
cards added in last week

The check is made against card creation time rather than note creation time, so cards that were generated within the time frame will be included even if their notes were added a long time ago.

#### Recently answered

rated:1
cards answered today
rated:1:2
cards answered Hard (2) today
rated:7:1
cards answered Again (1) over the last 7 days
rated:31:4
cards answered Easy (4) in the last month
For speed, rating searches are limited to 31 days.

#### Object IDs

nid:123
all cards of the note with note id 123
cid:123
the card with card id 123
mid:123
find note types with note type id 123

Note and card IDs can be found in the [card info](https://apps.ankiweb.net/docs/manual.html#stats) dialog in the browser. Note type IDs can be found by clicking on a note type in the Browse screen. These searches may also be helpful when doing add-on development or otherwise working closely with the database.

|     |     |
| --- | --- |
| Note | Object IDs will not work in the mobile clients, and are not intended to be used in filtered decks at the moment. |

### Card List

The card list displays cards that match the current search.

The columns are configurable: right click on one (or ctrl+click on a Mac) to choose which columns you’d like to see. You can drag columns to reorder them. Clicking on a column will sort by that column; click again to reverse the sort order. Not all columns can be sorted on.

|     |     |
| --- | --- |
| Note | The due column behaves differently for different types of cards. New cards show a number rather than a due date, which indicates the order the new cards will be presented in. Cards in (re)learning and reviews will both show a due date, but when sorting they are first grouped by type and then sorted by date. |

|     |     |
| --- | --- |
| Note | The "edited" and "changed" columns sound the same but track different things. "Edited" tracks the last time changes were made to the *note* (e.g., when the content of a field was edited), while "changed" tracks the last time changes were made to the *card* (e.g., when you reviewed the card and the review history and interval were updated). |

When you click on a card, its note will be shown in the bottom section. If you drag the mouse or hold ctrl or command to select multiple cards, the editor will be temporarily hidden. Various operations (such as changing the deck) can operate on multiple cards at once.

The background colour will change depending on the card. Marked cards are a shade of purple. Suspended cards are a shade of yellow. For more information about marked and suspended cards, please see [editing and more](https://apps.ankiweb.net/docs/manual.html#editmore).

One of the available columns is called the *sort field*. Anki allows you to choose one field from each type of note to be used for sorting. You can change the sort field by clicking on "Fields…" in the current note section.

The question and answer columns display what you’d see on the question and answer while reviewing, except the answer column will strip the question part for clarity. You can also choose a [custom format](https://apps.ankiweb.net/docs/manual.html#columntemplates) in the card type editor instead of showing what would be seen during review.

### Current Note

The bottom right area displays the currently selected card’s note. For more information about cards and notes, please see [the basics](https://apps.ankiweb.net/docs/manual.html#basics). For more information on formatting buttons, please see [editing](https://apps.ankiweb.net/docs/manual.html#editor).

You can see a preview of what the currently selected card would look like when reviewing by clicking the "preview" button next to the search box. Note that this will not display any type answer fields on your cards, which makes it easier to preview cards quickly.

### Toolbar

Up the top of the browser window is the toolbar.

*Info* shows various information about the currently selected card, including its review history. For more information, see the [statistics](https://apps.ankiweb.net/docs/manual.html#stats) section.

*Mark* and *Suspend* are documented in [editing and more](https://apps.ankiweb.net/docs/manual.html#editmore).

*Change Deck* allows you to move cards to a different deck. Cards can be placed in different decks, so if you want to move all cards in a note, you should first use Edit > Select Notes.

*Add Tags* and *Remove Tags* allow you to add or remove tags from notes in bulk. To remove unused tags from the list on the left, use Tools>Check Database from the main window.

*Delete* removes the selected card(s) and their notes. It is not possible to remove individual cards, as individual cards are controlled by the[templates](https://apps.ankiweb.net/docs/manual.html#templates).

### Find and Replace

This option (Edit→Find and Replace…) allows you to replace text in the notes you have selected. The regular expression option allows you to perform complex replacements. For example, given the following text in a field:

<img src="pic.jpg" />
Searching for:
<img src="(.+?)" />
And replacing with the regexp:
\1
Will change the card to:
pic.jpg

A full discussion on regular expressions is outside the scope of this document. There are a number of tutorials available on the web. Please seehttp://docs.python.org/library/re.html for the particular format Anki uses.

### Finding Duplicates

You can use the Edit>Find Duplicates option to search for notes that have the same content. When you open the window, Anki will look at all of your note types and present a list of all possible fields. If you want to look for duplicates in the "Back" field, you’d select it from the list and then click "Search".

Unlike the check that happens when you add cards manually, the duplicate finding feature is not limited to a single note type. This means that by default, it will search in all note types that have the field you provided.

The *optional limit* text box allows you to narrow down where Anki will look for duplicates. If you only want to search for duplicates in the "French Vocab" and "French Verbs" note types, you would enter:

note:'french vocab' or note:'french verbs'

Or you might want to look only for duplicates in a particular deck, so you could use:

deck:'myDeck'

The search syntax is the same as used when searching in the browser. Please see the [searching](https://apps.ankiweb.net/docs/manual.html#searching) section for more information.

You can click one of the links in the search results list to display the duplicate notes in that set. If the search brings up a large number of duplicates, you may wish to instead click the Tag Duplicates button, which will tag all matching notes with "duplicate." You can then search for this tag in the browser and handle them all from the same screen.

### Other Menu Items

Some other items in the Edit menu:

*Reschedule* allows you to move cards to the end of the new card queue, or reschedule them as a review card on a given date. The second option is useful if you have imported already-learnt material, and you want to start it off with higher initial intervals. For example, choosing 60 and 90 will give all the imported cards an initial interval of 2 to 3 months.

The card’s revision history is not cleared when rescheduling: rescheduling changes the current state of a card, but not its history. If you want to hide the history, you will need to export your notes as a text file, delete the notes, and then import the text file again, creating new notes.

*Reposition* allows you to change the order new cards will appear in. You can find out the existing positions by enabling the *due* column, as described in the card list section above. If you run the reposition command when multiple cards are selected, it will apply increasing numbers to each card in turn. By default the number increases by one for each card, but this can be adjusted by changing the "step" setting. The *Shift position of existing cards* option allows you to insert cards between currently existing ones, pushing the currently existing ones apart. For instance, if you have five cards and you want to move 3, 4, and 5 between 1 and 2, selecting this setting would cause the cards to end up in the order 1, 3, 4, 5, 2. By contrast, if you turn this option off, 2 and 3 will get the same position number (and it will thus be random which one comes up first).

*Change Note Type* allows you to convert the selected notes from one type to another. For example, imagine you have a Russian note type and a Computer note type, and you accidentally added some computer-related text into a Russian note. You can use this option to fix that mistake. The scheduling of cards is not affected.

*Select Notes* takes the currently selected cards, finds their notes, and then selects all cards of those notes. If your notes have only one card, this does nothing.

The *Go* menu exists to provide keyboard shortcuts to jump to various parts of the browser, and to go up and down the card list.

## Filtered Decks & Cramming

When you study a regular deck in Anki, only a limited number of cards are shown: the cards Anki thinks you’re about to forget, and a daily limit of new cards. This is generally useful, as it ensures you don’t spend more time studying than necessary. But sometimes it can be useful to step outside of these normal limits, such as when you need to revise for a test, focus on particular material, and so on. To make this possible, Anki provides a different type of deck called a *filtered deck*.

Filtered decks offer a lot of possibilities. They can be used for previewing cards, cramming cards before a test, studying particular tags, catching up on a backlog with a particular sort order, reviewing ahead of schedule, going over the day’s failed cards, and more.

### Custom Study

The easiest way to create a filtered deck is with the Custom Study button, which appears at the bottom of the screen when you click on a deck. It offers some convenient presets for common tasks like reviewing the cards you’ve failed that day. It will create a filtered deck called "Custom Study Session" and automatically open it for you.

If an existing "Custom Study Session" deck exists, it will be emptied before a new one is created. If you wish to keep a custom study deck, you can rename it from the deck list.

Here is a summary of each of the options:
Increase today’s new card limit

Add more new cards to the deck you are currently studying. Note that unlike other options, this does *not* create a new filtered deck, it modifies the existing deck.

Increase today’s review card limit

If not all reviews due today were shown due to the daily review limit, this option allows you to show more of them. Like with the new cards option, this modifies the existing deck.

Review forgotten cards

Show all cards that you’ve answered Again (1) to within a number of days you specify.

Review ahead

Show cards that will be due in the near future (a number of days you specify). This is useful for working through some of your older cards before a vacation, but it will not help with cards you have learnt recently. Please see the [reviewing ahead](https://apps.ankiweb.net/docs/manual.html#reviewingahead) section below for more info.

Preview new cards

Show cards that you have recently added, without converting them to review cards as they are answered.

Study by card state or tag

Select a certain number of cards from the current deck to study. You can choose to select new cards only, due cards only, or all cards; after you click "Choose Tags", you can also limit the selected cards by tags. If you wish to see all the cards in the deck (for instance, to study before a big test), you can set the number of cards to more than the number of cards in the deck.

### Home Decks

When a card is moved to a filtered deck, it retains a link to the deck it was in previously. That previous deck is said to be the card’s *home deck*.

Cards automatically return to their home deck after they are studied in the filtered deck. This can be after a single review, or after multiple reviews, depending on your settings.

It is also possible to move all cards back to their home decks at once:

- The "Empty" button in the study overview moves all cards in the filtered deck back to their home deck, but does not delete the empty filtered deck. This can be useful if you want to fill it again later (using the Rebuild button).
- Deleting a filtered deck does the same thing as "Empty" does, but also removes the emptied deck from the deck list. No cards are deleted when you delete a filtered deck.

|     |     |
| --- | --- |
| Note | In the current implementation, if you create, rebuild, empty or delete a filtered deck while cards are still in learning, they will be turned back into new cards. In the case of failed reviews in relearning, any remaining relearning steps will be skipped. This has been fixed in the[experimental scheduler](https://anki.tenderapp.com/kb/anki-ecosystem/experiment-scheduling-changes-in-anki-21). |

### Creating Manually

Advanced users can create filtered decks with arbitrary search strings, instead of relying on set presets. To create a filtered deck manually, choose Create Filtered Deck from the Tools menu.

When you click the Build button, Anki finds cards that match the settings you specified, and temporarily moves them from their existing decks into your new filtered deck for study.

If you wish to fetch cards again using the same filter options (for instance, if you want to study all cards with a particular tag every day), you can use the Rebuild button at the bottom of the deck’s overview screen.

The **search** area controls what cards Anki will gather. All of the searches possible in the browser are also possible for filtered decks, such as limiting to tags, finding cards forgotten a certain number of times, and so on. Please see the [searching](https://apps.ankiweb.net/docs/manual.html#searching) section of the manual for more information on the different possibilities.

|     |     |
| --- | --- |
| Note | Filtered decks can not include cards that are suspended, buried, or already in a different filtered deck. For this reason, a search in the browser may reveal cards that don’t end up in the filtered deck. |

The **limit** option controls how many cards will be gathered into the deck. The order you select controls both the order cards are gathered in, and the order they will be reviewed in. If you select "most lapses" and a limit of 20 for example, then Anki will show you only the 20 most lapsed cards.

For efficiency reasons, if your cram deck contains more than 1000 cards, only 1000 cards will be shown as due on the deck list and study screens.

### Order

The "cards selected by" option controls the order that cards will appear in. If the maximum number of cards you select is lower than the number of cards that match the filter criteria, Anki will exclude the cards at the end of this sorted list first.

Oldest seen first
Display cards that you haven’t seen in reviews for the longest time first.
Random

Randomize the order of all cards that match the filter criteria (use no set order).

Increasing intervals
Display cards that have the smallest interval first.
Decreasing intervals
Display cards that have the largest interval first.
Most lapses
Display cards that you have failed the most times first.
Order added
Display cards that you added first (have the earliest creation date) first.
Order due
Display cards with the earliest due date first.
Latest added first

Display cards that you’ve most recently added to the deck first. (This is the opposite of *Order added*.)

Relative overdueness

Display cards that are most overdue in relation to their current interval first (for instance, a card with a current interval of 5 days overdue by 2 days displays before a card with a current interval of 5 years overdue by a week). This is useful if you have a large backlog that may take some time to get through and want to review the cards you’re most in danger of forgetting first.

### Steps & Returning

Please see the section on [learning](https://apps.ankiweb.net/docs/manual.html#learning) as a reminder of how steps work.

By default, Anki will use the steps of a card’s home deck. If a new card would normally be reviewed twice when being learnt, the same thing will happen when you study it in a filtered deck.

Cards return to their home deck when (re)learning is complete. Thus if you have 3 learning steps, a new card will return to its home deck upon three presses of "Good" or a single press of "Easy".

The **custom steps** option allows you to override the home deck’s steps and provide your own steps instead. The provided steps apply to both cards being learnt, lapsed reviews, and reviews ahead of time.

### Counts

In a filtered deck, reviews that were already due are displayed in the review count as normal. Learning cards and non-due reviews are counted in the new card count, due to how the underlying implementation works. Reviews that were not due are not scheduled like new cards however - Anki uses a special algorithm that takes into account how close they were to their normal due time when reviewed.

### Due Reviews

If the filtered deck includes cards that were due for review, they will be shown like they would have been in their original deck - they appear in the review card count at the bottom of the screen, and there are four choices for how well you remembered. Upon a correct answer, the card will be moved back to its home deck, and its next delay adjusted using the home deck’s settings. If you forget the card, it will be shown according to the relearning steps defined in the home deck.

### Reviewing Ahead

If your search included cards that are not due, Anki will show the reviews ahead of time.

Anki uses a special algorithm for these reviews that takes into account how early you are reviewing. If the cards were almost due to be shown, they will be given a new delay similar to what they would have received if you had reviewed them on time. If the cards are reviewed soon after they were scheduled however, their new delay will be similar to their previous delay. This calculation works on a sliding scale.

|     |     |
| --- | --- |
| Note | Because reviewing a card shortly after it is scheduled has little impact on scheduling (eg, a card due tomorrow with a one day interval will remain due tomorrow if reviewed early), **the "review ahead" custom study setting is not appropriate for repeated use**. If used to go through a week’s worth of cards before a trip, the mature cards will be rescheduled into the future and the new cards will remain at small intervals, because you don’t know them well enough for them to be rescheduled further. If you review ahead again the next day, all you’ll end up doing is going through those same new cards again, to little benefit. |

Early reviews are included in the new card count rather than the review count, and will be shown according to the number of relearning steps defined in the home deck (unless you have provided custom steps). This means that if you have customized the number of relearning steps in the home deck, the non-due card may be shown more than once.

If you have multiple steps, Anki will only consider the first answer when deciding the next delay, and like relearning in normal decks, "Good" and "Easy" differ only in the step change and not the resulting delay.

### Rescheduling

By default, Anki will return cards to their home decks with altered scheduling based on your performance in the filtered deck. If you disable the **reschedule cards based on my answers** option, Anki will return the cards in the same state they were in when they were moved into the filtered deck. This is useful for quickly flipping through material.

If you have disabled rescheduling, the "Good" and "Easy" buttons will display no time above them when pressing them would cause the card to return to its home deck with its original scheduling.

Please note that new cards are returned to the end of the new card queue, rather than the start of it.

### Catching Up

Filtered decks can be useful for catching up when you’ve fallen behind in your reviews. One Anki user describes the way they use the filtered decks to catch up as follows:

*

I did this for a backlog of 800 cards with filtered subdecks. Worked very well for me.

1. Just Due filter with: "is:due prop:due>-7"
2. Over Due filter with: "is:due prop:due<=-7"

The Just Due deck will then contain cards that became due in the past week. That's the deck you should study every day as it gets the cards that become due regularly. With this you can study as if there wasn't any backlog.

The Over Due deck will contain your backlog, cards which you didn't study in time. You can study them the same way you would study new cards. They go back into the regular cards, so the number of overdue will never grow as long as you keep your Just Due deck in check.

*

*How long it takes depends on how many overdue cards you study each day in addition to the ones that become due regularly. You can still motor through them when you feel like it - or you can do a specific number per day like you would for new cards. Up to you.*

## Leeches

Leeches are cards that you keep on forgetting. Because they require so many reviews, they take up a lot more of your time than other cards.

Anki can help you identify leeches. Each time a review card *lapses* (is failed while it is review mode), a counter is increased. When that counter reaches 8, the note is tagged as a leech, and the card is suspended. The threshold, and whether to suspend or not, can be adjusted in the [deck options](https://apps.ankiweb.net/docs/manual.html#deckoptions).

Anki will continue to issue leech warnings periodically for a difficult card. The warning interval is half the initial leech threshold. That is, if you have Anki configured to warn at 8 lapses, future warnings will happen every 4 lapses. (12, 16, etc)

Once a leech is found, there are a number of ways you can handle it.

### Waiting

Some leeches are caused by *interference*. For example, an English learner may have recently learnt the words "disappoint" and "disappear". As they look similar, the learner may find themselves confusing the two when trying to answer. In these situations, it’s often productive to concentrate on just one idea. When that idea is firmly ingrained in your mind, you can then return to learning the other idea. So in these situations, you may want to leave one of the words suspended until you have learnt the other one well, and then unsuspend it in the browser.

### Deleting

Another way to manage leeches is to delete them. Consider if the material you’re struggling with is important enough to make it worth your while. By selectively deleting difficult and obscure items, you can dedicate more time to learning other material, and studying becomes a lot more fun.

### Editing

Another approach is to change the way the information is presented. Perhaps the cards you have created have too much information on them, or perhaps you’re trying to memorize something without fully understanding it. Sometimes spending some time changing the way the card is phrased can help. It’s also a good time to think about making a mnemonic to help you remember.

## Importing

Anki can import text files, packaged Anki decks created by the export feature, Mnemosyne 2.0 .db files, and SuperMemo .xml files. To import a file, click the File menu and then "Import".

### Importing text files

Any **plain text** file that contains fields separated by commas, semicolons or tabs can be imported into Anki, provided some conditions are met.

- The files must be plain text (myfile.txt). Other formats like myfile.xls, myfile.rtf, myfile.doc must be saved as a plain text file first.
- The files must be in UTF-8 format (see below).
- Anki determines the number of fields in the file by looking at the first (non-commented) line. Any lines in the file which have a different number of fields will be ignored.
- The first line also defines the separating character – if Anki finds a *;* on the first line it will use that, if it finds a comma it’ll use that, etc.

Fields in your text file can be mapped to any field in your notes, including the tags field. You can choose which field in the text file corresponds to which field in the note when you import.

When you import a text file, you can choose what deck to put the cards in. Keep in mind that if you have the deck override option set for one or more of your templates, the cards will go to that deck rather than the one you’ve selected.

This is an example of a valid file:
foo bar; bar baz; baz quux
apple; banana; grape
There are two ways to include newlines in fields.

**Escape the multi-lines by placing the contents of the field in quotation marks**:

hello; "this is
a two line answer"
two; this is a one line one

Because quotes are used to mark where a field begins and ends, if you wish to include them inside your field, you need to replace a single doublequote with two doublequotes to "escape" them from the regular handling, like so:

field one;"field two with ""escaped quotes"" inside it"

When you use a spreadsheet program like Libreoffice to create the CSV file for you, it will automatically take care of escaping double quotes.

**Use HTML new lines**:
hello; this is<br>a two line answer
two; this is a one line one

You need to turn on the "allow HTML in fields" checkbox in the import dialog for HTML newlines to work.

|     |     |
| --- | --- |
| Note | Escaped multi-lines will not work correctly if you are using cloze deletions that span multiple lines. In this case, please use HTML newlines instead. |

You can also include tags in another field and select it as a tags field in the import dialog:

first field; second field; tags
This is an example of a valid file where the first line is ignored (#):

# this is a comment and is ignored

foo bar; bar baz; baz quux
field1; field2; field3

### Spreadsheets and UTF-8

If you have non-Latin characters in your file (such as accents, Japanese and so on), Anki expects files to be saved in a *UTF-8 encoding*. The easiest way to do this is to use the free LibreOffice spreadsheet program instead of Excel to edit your file, as it supports UTF-8 easily, and also exports multi-line content properly, unlike Excel. If you wish to keep using Excel, please see[this forum post](https://docs.google.com/document/d/12YE_FS6A9ANLTESJNtPP116ti4nNmCBghyoJBRtno_k/edit?usp=sharing) for more information.

To save your spreadsheet to a file Anki can read with LibreOffice, go to File>Save As, and then select CSV for the type of file. After accepting the default options, LibreOffice will save the file and you can then import the saved file into Anki.

### HTML

Anki can treat text imported from text files as HTML (the language used for web pages). This means that text with bold, italics and other formatting can be exported to a text file and imported again. If you want to include HTML formatting, you can check the "allow HTML in fields" checkbox when importing. You may wish to turn this off if you’re trying to import cards whose content contains angle brackets or other HTML syntax.

If you wish to use HTML for formatting your file but also wish to include angle brackets, you may write them differently:

- For "<", use "&lt;"
- For ">", use "&gt;"

### Importing Media

If you want to include audio and pictures from a text file import, copy the files into the [collection.media folder](https://apps.ankiweb.net/docs/manual.html#files). **Do not put subdirectories in the media folder, or some features will not work.**

After you’ve copied the files, change one of the fields in your text file as follows.

<img src="myimage.jpg">
or
[sound:myaudio.mp3]

Alternatively, you can use the [find and replace](https://apps.ankiweb.net/docs/manual.html#findreplace) feature in the browse screen to update all the fields at once. If each field contains text like "myaudio", and you wish to make it play a sound, you’d search for (.*) and replace it with "[sound:\1.mp3]", with the *regular expressions* option enabled.

|     |     |
| --- | --- |
| Note | When importing a text file with these references, you must make sure to enable the "Allow HTML" option. |

You might be tempted to do this in a template, like:
<img src="{{field name}}">

Anki doesn’t support this for two reasons: searching for used media is expensive, as each card has to be rendered, and such functionality isn’t obvious to shared deck users. Please use the find & replace technique instead.

#### Bulk media imports

Another option for importing large amounts of media at once is to use the[media import add-on](https://ankiweb.net/shared/info/1531997860). This add-on will automatically create notes for all files in a folder you select, with the filenames on the front (minus the file extension, so if you have a file named apple.jpg, the front would say *apple*) and the images or audio on the back. If you would like a different arrangement of media and filenames, you can[change the note type](https://apps.ankiweb.net/docs/manual.html#browsermisc) of the created cards afterwards.

### Adding Tags

If you want to add *tag1* and *tag2* to every line you’re importing, add the following to the top of the text file:

tags:tag1 tag2

### Duplicates and Updating

When importing text files, Anki uses the first field to determine if a note is unique. By default, if the file you are importing has a first field that matches one of the existing notes in your collection and that existing note is the same type as the type you’re importing, the existing note’s other fields will be updated based on content of the imported file. A drop-down box in the import screen allows you to change this behaviour, to either ignore duplicates completely, or import them as new notes instead of updating existing ones.

|     |     |
| --- | --- |
| Note | The duplicate check is done for your *entire collection*, not just in the current deck. If Anki is indicating that notes have not changed when you expected them to be imported, please check that the notes are not already in your collection somewhere. |

If you have updating turned on and older versions of the notes you’re importing are already in your collection, they will be updated in place (in their current decks) rather than being moved to the deck you have set in the import dialog. If notes are updated in place, the existing scheduling information on all their cards will be preserved.

For info on how duplicates are handled in .apkg files, please see the[Deck Packages](https://apps.ankiweb.net/docs/manual.html#apkg-export) section below.

## Exporting

Exporting allows you to save part of your collection as a text file or packaged Anki deck. To export, click the File menu and choose *Export*.

### Exporting Text

If you choose "Notes in Plain Text", Anki will write the contents of the notes into a text file. Each field is separated by a tab. If you edit the resulting file and don’t modify the first field, you can later import that file back into Anki and Anki will update your notes based on your edits, provided you import back into the same note type.

If you find yourself needing to edit the first field as well, you’ll need to change the format of your note type so that the first field is an ID number rather than actual text. (You can install the "Add note id" plugin to make this easier.)

In order for formatting to be preserved when you import text back in, the text is exported with all the HTML formatting embedded in it.

### Exporting Packaged Decks

A *packaged deck* consists of cards, notes, note types and any sounds or images bundled up into a file ending with .apkg or .colpkg. You can use packaged decks to transfer cards between people, or for backing up parts of your collection.

There are two different kinds of packaged decks.

#### Collection Package

When you export all decks with scheduling included, this is called a*collection package*. Anki will copy your entire collection into a file ending in .colpkg, and place it on your desktop. A collection package is used to back up your collection, or copy it to another device.

Collection packages created with previous versions of Anki were called collection.apkg.

When this file is later imported, Anki will delete all the current cards in the collection, and replace the collection with the items in the file. This is useful for copying your collection back and forth between devices.

|     |     |
| --- | --- |
| Note | Existing media in your collection is not deleted when you import a collection package. To delete unused media, use Tools>Check Media. |

#### Deck Package

Deck packages contain a single deck (and any child decks it may have). They have a filename ending with .apkg, but a filename other than collection.apkg. When you import a deck package, Anki will add the contents into your collection, rather than overwriting your collection.

If some notes in the deck package have previously been imported, Anki will keep the version with the most recent modification time. So if you download an updated deck, the edits that have been made in the updated version will be made in your collection as well, but if you re-import an unchanged deck after making edits in your collection, the changes in your collection will be kept.

If you choose not to include scheduling information, Anki will assume that you are sharing the deck with other people, and will remove marked and leech tags so that they will have a clean copy of it.

## Managing Files and Your Collection

### Checking Your Collection

It’s a good idea to occasionally check your collection file for problems. You can do this via the Tools>Check Database menu item. Checking the database ensures the file is not corrupted, rebuilds some internal structures, and optimizes the file.

When you check the database, your tag list is also rebuilt. When you delete individual decks or cards, Anki does not update the list of used tags, as it’s inefficient to do so. If you want to clear old tags out from the list that are no longer in use, checking your database is the way to do it.

Please note that Anki will automatically optimize your collection once every 2 weeks. This optimization ensures the collection performs well, but it does not check for errors or rebuild the tag list when automatically optimizing.

### File Locations

On **Windows**, the latest Anki versions store your Anki files in your appdata folder. You can access it by opening the file manager, and typing%APPDATA%\Anki2 in the location field. Older versions of Anki stored your Anki files in a folder called Anki in your Documents folder.

On **Mac** computers, recent Anki versions store all their files in the~/Library/Application Support/Anki2 folder. The Library folder is hidden by default, but can be revealed in Finder by holding down the option key while clicking on the Go menu. If you’re on an older Anki version, your Anki files will be in your Documents/Anki folder.

On **Linux**, recent Anki versions store your data in ~/.local/share/Anki2, or$XDG_DATA_HOME/Anki2 if you have set a custom data path. Older versions of Anki stored your files in ~/Documents/Anki or ~/Anki.

Within the Anki folder, the program-level and profile-level preferences are stored in a file called prefs.db.

There is also a separate folder for each profile. The folder contains:

- Your notes, decks, cards and so on in a file called collection.anki2
- Your audio and images in a collection.media folder
- A backups folder
- Some system files

|     |     |
| --- | --- |
| Warning | You should never copy or move your collection while Anki is open. Doing so could cause your collection to become corrupted. Please don’t move or modify the other files in the folder either. |

### Startup Options

If you have made a destructive change on one computer and have an undamaged copy on another computer, you may wish to start Anki without syncing in order to use the full sync option without first downloading the changes. Similarly, if you are experiencing problems with Anki, you might want to (or might be instructed to) disable add-ons temporarily to see if one might be causing the problem. You can do both of these things by holding down the Shift key while starting Anki.

It is possible to specify a custom folder location during startup. This is an advanced feature that is primarily intended to be used with portable installations, and we recommend you use the default location in most circumstances.

The syntax to specify an alternate folder is as follows:
anki -b /path/to/anki/folder

- If you have multiple profiles, you can pass -p <name> to load a specific profile.
- To change the interface language, use -l <iso 639-1 language code>, such as "-l ja" for Japanese.

If you always want to use a custom folder location, you can modify your shortcut to Anki. On Windows, right-click on the shortcut, choose Properties, select the Shortcut tab, and add "-b \path\to\data\folder" after the path to the program, which should leave you with something like

"C:\Program Files\Anki\anki.exe" -b "C:\AnkiDataFolder"

You can also use this technique with the -l option to easily use Anki in different languages.

|     |     |
| --- | --- |
| Note | On Windows, you should use a backslash (\) not a forward slash (/). |

On a Mac there is no easy way to alter the behaviour when clicking on the Anki icon, but it is possibile to start Anki with a custom base folder from a terminal:

open /Applications/Anki.app --args -b ~/myankifolder

### DropBox and File Syncing

We do not recommend you sync your Anki folder directly with a third-party synchronization service, as it can lead to database corruption when files are synced while in use.

If you just want to synchronize your media, you can link external folders into services like DropBox. Please seehttp://www.dropboxwiki.com/tips-and-tricks/sync-other-folders for more info.

If you wish to keep your collection in sync as well, it is strongly recommended that you create a script that copies your files from your synced folder to a local folder, launches Anki, and then copies the files back when Anki is closed. This will ensure that the files are never synchronized while they are open.

### Network Filesystems

We strongly recommend you have Anki store your files on a local hard disk, as network filesystems can lead to database corruption. If a network filesystem is your only option, regular use of Tools>Check Database to detect corruption is recommended.

### Running from a Flash Drive

On Windows, Anki can be installed on a USB / flash drive and run as a portable application. The following example assumes your USB drive is drive G.

- Copy the \Program Files\Anki folder to the flash drive, so you have a folder like G:\Anki.
- Create a text file called G:\anki.bat with the following text:

g:\anki\anki.exe -b g:\ankidata

If you would like to prevent the black command prompt window from remaining open, you can instead use:

start /b g:\anki\anki.exe -b g:\ankidata

- Double-clicking on anki.bat should start Anki with the user data stored in G:\ankidata.

|     |     |
| --- | --- |
| Note | The full path including drive letter is required - if you try using\anki\anki.exe instead you will find syncing stops working. |

|     |     |
| --- | --- |
| Note | Media syncing with AnkiWeb may not work if your flash drive is formatted as FAT32. Please format the drive as NTFS to ensure media syncs correctly. |

### Backups

Each time your collection is closed (when closing Anki, switching profiles, or synchronizing your deck), Anki exports your collection into the backups folder. By default Anki will store up to 30 backups; you can adjust this in the [preferences](https://apps.ankiweb.net/docs/manual.html#preferences).

Automatic backups do not protect against disk or computer failure, and do not extend to your media. To keep your collections safe, please consider making manual backups too.

The easiest way to make a manual backup is to use the File>Export menu item to export all decks with scheduling and media information included, which will save your data to a .colpkg file.

If you want to back up multiple profiles and your add-ons as well, you can make a complete copy of your [Anki folder](https://apps.ankiweb.net/docs/manual.html#files). Please make sure you close Anki first, as backups may be corrupt if run while Anki is open.

To restore from an automatic backup:
1. From the File menu, select Switch Profile to show the Profiles window.
2. Select the profile you wish to restore on the left.
3. Click the Open Backup… button.
4. Choose Yes and the available backups will appear.
5. Open a backup based on the date you wish to restore to.

6. Check that that the backup that was restored was the one you intended. If you wish to try a different backup, return to step 1.

7. Anki has disabled automatic syncing and backups while you check the backup. When you’re happy with the backup you’ve selected, quit Anki and start it again to return to the normal behaviour.

Anki also logs deleted notes to a text file called deleted.txt in your profile folder. These notes are in a text format that can be read by File>Import, though please note the import feature only supports a single note type at one time, so if you have deleted notes from different note types, you’ll need to split the file into separate files for each note type first.

### Inaccessible Harddisk

If Anki can’t write to files in the [Anki folder](https://apps.ankiweb.net/docs/manual.html#files), a message will be displayed on startup saying that Anki can’t write to the harddisk, and Anki will close. If you’re unsure how to fix the permissions, please contact someone near you who is knowledgable about computers and can help you out.

### Permissions of Temp Folder

Anki uses the system’s temporary folder to store temporary data. If the permissions of this folder have been changed from the default settings by a rogue app or buggy antivirus app, Anki will not function properly.

If you’re on a Windows 7 machine, the general steps to fix the problem are listed below. As this is somewhat complicated, please ask someone knowledgeable about Windows if you are not sure.

1. Click on the start bar, and type in %temp% (including the percents), then hit enter.

2. Go up one folder, and locate the temp folder. Right click on it, and choose Properties.

3. In the security tab, click on Advanced.

4. Click on the Owner tab. If you’re not listed as the owner, click the button to take ownership.

5. On the permissions tab, ensure that you have full control. On a default W7 install the control will actually be inherited from c:\users\your-username.

### Corrupt Collections

Anki uses a file format that is robust against program and computer crashes, but it’s still possible for your collection to become corrupt if the files are modified while Anki is open, stored on a network drive, or corrupted by a bug.

When you run Tools>Check Database, you will receive a message if Anki detects the file has been corrupted. **The best way to recover from this is to restore from the most recent [automatic backup](https://apps.ankiweb.net/docs/manual.html#backups)**, but if your backup is too old, then you can attempt to repair the corruption instead.

On Linux, make sure sqlite3 is installed. On a Mac, it should be installed already. On Windows, download http://www.sqlite.org/sqlite-3_6_23.zip.

Next, create a backup of your collection.anki2 file, in case something goes wrong with the steps below.

**Linux/OSX**
Open a terminal, change to the folder your collection is located in, and type:
sqlite3 collection.anki2 .dump > dump.txt

Open the resulting dump.txt file in a text editor, and look at the final line. If it reads "rollback;", change it to "commit;"

Then run the following in a terminal:
cat dump.txt | sqlite3 temp.file

Make sure you use temp.file - do not put collection.anki2 on the right, or you will blank out the file. When you’re done, proceed to the final step.

**Windows**

Copy the sqlite3.exe program and your deck to your desktop. Then go to**Start>Run** and type in cmd.exe.

If you’re on a recent Windows, the command prompt may not start on your desktop. If you don’t see desktop displayed in the command prompt, type something like the following, replacing *administrator* with your login name.

cd C:\Users\Administrator\Desktop
Then type:
sqlite3 collection.anki2 .dump > dump.txt

Open the resulting dump.txt file in a text editor, and look at the final line. If it reads "rollback;", change it to "commit;"

Then run the following in a terminal:
type dump.txt | sqlite3 temp.file

Make sure you use temp.file - do not put collection.anki2 on the right, or you will blank out the file. When you’re done, proceed to the final step.

**Final Step**

Check that you didn’t get an error message, and that temp.file is not empty. The procedure optimizes the collection in the process, so it’s normal for the new file to be somewhat smaller than the old one.

When you’ve confirmed the file is not empty:

- rename the original collection.anki2 file to something else
- rename temp.file to collection.anki2
- move collection.anki2 back into your collection folder, overwriting the old version
- start Anki and go to Tools>Check Database to make sure the collection has been successfully restored.

## Graphs and Statistics

### Card Info

You can display information about a card by clicking the Info button in the toolbar while browsing. Most of the displayed information should be self-explanatory. A few notes:

Position

Only shown when the card is new, it shows the order the card will appear in relative to other new cards. The position can be changed in the browser.

Interval

The delay from one review to the next. Times are abbreviated; "0s, 1m, 3h, 4d, 5mo, 6y" refers to seconds, minutes, hours, days, months and years respectively.

Ease

The approximate amount the interval will grow when you answer a review card with the "Good" button.

### Statistics

The statistics window is accessed by clicking on the graphs icon in the top right of the main window, or by pressing Shift+S. The statistics window will show statistics from the currently selected deck and any subdecks. If you click on "collection" on the bottom left, statistics will be shown for your entire collection instead.

By default Anki will show you statistics for the previous month. You can change this to a year scope or deck life scope at the bottom. (The "today" section at the top is of course unaffected by this selection.)

Clicking on "Save Image" will save an image of the statistics to a file on your desktop to make it easy to share your statistics with others.

|     |     |
| --- | --- |
| Note | When you delete notes, their review history is maintained in Anki. It will not be included when looking at statistics for a specific deck (as Anki has no way of knowing which deck the deleted cards belonged to), but will be included when you look at statistics for the whole collection. |

### Types of Cards

The stats window uses some terms that you may not be familiar with:
Mature
A mature card is one that has an interval of 21 days or greater.
Young

A young card is one that has an interval of less than 21 days, but is not in learning.

Learn

A learning card is one that is still in learning mode (using whatever steps may be defined in the deck’s options).

Relearn

A relearning card is a card that you have failed in review mode, thus returning it to learning mode to be relearned.

Unseen

An unseen card is one that has been added to your collection but has not yet entered learning mode. Unseen cards are sometimes referred to as "new" cards, especially when they are in the "new" queue to be shown for the first time.

### Today

At the top of the statistics window is a brief list of textual statistics about the reviews that you have completed today. A “review” in this context is *one answering of a card*, so a card might count as multiple reviews if it needed to be seen multiple times, and a learning card answered also counts as a “review.” A couple of the stats whose meaning may not be immediately obvious:

Again count

This is the number of reviews that you have failed (i.e., pressed Again on). The correct percentage listed afterwards is the number of cards you did *not* fail divided by the total number of cards you studied.

Learn, Review, Relearn, Filtered

The number of reviews that were learning cards, review cards, relearning cards, or studied in a filtered deck when not due.

The stats for the current day are not a good overall indicator of your learning progress; everyone has bad days and good days, and seeing that you got a lower percentage correct on a particular day should not be cause for concern. The remainder of the stats, which take longer periods of time into account, will give more useful information if you wish to try to change your study habits or scheduling settings based on your performance.

The “today” statistics are unaffected by the time period selected at the bottom of the window.

### The Graphs

Forecast

This graph shows an estimated number of reviews that will be due on a given day in the future if you learn no new cards and fail no cards. The bars and the left axis show the number of cards due on each day if you study all cards each day, while the line and the right axis show the number of cards due on that day if you don’t study at all until then. Note that the forecast graph does not count reviews that are currently overdue, so if you have a large backlog, the overdue cards will not be displayed.

Review Count

This graph counts the number of card reviews you have done. The bars may correspond to days, weeks, or months, depending on the time period you’ve selected at the bottom of the screen. The differently colored blocks show how many of the cards you answered on each day were [mature](https://apps.ankiweb.net/docs/manual.html#cardtypedefinitions), young, relearning, or learning cards. There is also a separate group for cards answered in a filtered/cram deck while they were not due. The line and the right axis shows the cumulative total for each type of review as time progresses across the graph (so at 0 days, it would display the number for the entire time period displayed on the graph).

Review Time

This graph works exactly like Review Count, except that it deals with the amount of time you spent on each card rather than the number of cards answered.

Intervals

This graph displays the number of cards that have a given interval (the delay between two reviews). The line and the right axis tell you what percentage of your cards have an interval of less than or equal to the time below that point. The time scope has a different effect on this graph than other graphs: rather than changing which cards or period of studying is included, it limits how far out the intervals are displayed to (so 14-month intervals are not displayed at all on a 1-year graph).

Hourly Breakdown

This graph shows what percentage of total reviews you have passed (i.e., not pressed Again on) during given hours. The larger, darker bars and left axis show the success rate; the thinner, lighter bars and right axis show the number of reviews you’ve made at that hour (so you know how significant the results are).

Answer Buttons

This graph shows how many times you’ve chosen the Again, Hard, Good, or Easy button while studying learning/new, young, and [mature](https://apps.ankiweb.net/docs/manual.html#cardtypedefinitions) cards. Anki also displays the percentage of correct reviews for each type of card.

Cards Types

This pie chart shows what percentage of your deck or collection consists of mature, unseen, young/learn, and suspended cards. If you wish to calculate a more precise percentage, the key shows the exact number of cards in each section, and the total number of cards is displayed to the side.

### Manual Analysis

If you’re interested in getting information from your statistics other than what Anki provides, it is possible to access the data directly. Because of the complexity involved, this is not something we can provide any support for.

One option is to [write an add-on](https://apps.ankiweb.net/docs/manual.html#add-ons) that adds another graph or more details to the statistics window. There are several add-ons of this sort on AnkiWeb already, which you can look at to get an idea of how it works.

A more powerful and more complex option is to extract the review log information directly from Anki’s database and analyze it in an external program. Anki uses a database format called SQLite. There are many tools available for working with SQLite databases; one of the easiest to start with is called[SQLite Browser](http://sqlitebrowser.org/), which will allow you to look around the database as well as export a CSV version of tables for import into another program.

The most important table for statistics is the *revlog* table, which stores an entry for each review that you conduct. The columns are as follows:

id

The time at which the review was conducted, as the number of milliseconds that had passed since midnight UTC on January 1, 1970. (This is sometimes known as *Unix epoch time*, especially when in straight seconds instead of milliseconds.)

cid

The ID of the card that was reviewed. You can look up this value in the id field of the *cards* table to get more information about the card, although note that the card could have changed between when the revlog entry was recorded and when you are looking it up. It is also the millisecond timestamp of the card’s creation time.

usn

This column is used to keep track of the sync state of reviews and provides no useful information for analysis.

ease
Which button you pressed at the end of the review (1 for Again, 4 for Easy).
ivl

The new interval that the card was pushed to after the review. Positive values are in days; negative values are in seconds (for learning cards).

lastIvl

The interval the card had before the review. Cards introduced for the first time have a last interval equal to the Again delay.

factor

The new ease factor of the card in permille (parts per thousand). If the ease factor is 2500, the card’s interval will be multiplied by 2.5 the next time you press Good.

time

The amount of time (in milliseconds) you spent on the question and answer sides of the card before selecting an ease button.

type

This is 0 for learning cards, 1 for review cards, 2 for relearn cards, and 3 for "cram" cards (cards being studied in a filtered deck when they are not due).

## Media

Anki stores the sounds and images used in your notes in a folder next to the collection. For more on the folder location, please see the [file locations](https://apps.ankiweb.net/docs/manual.html#files) section. When you add media within Anki, either by using the paperclip icon in the [editor](https://apps.ankiweb.net/docs/manual.html#editor) or by pasting it into a field, Anki will copy it from its original location into the media folder. This makes it easy to back up your collection’s media or move it to another computer.

You can use the Tools>Check Media menu option to scan your notes and media folder. It will generate a report of files in the media folder that are not used by any notes, and media referenced in notes but missing from your media folder. It does not scan question or answer templates, which is why you can’t place media references to fields in the template. If you need a static image or sound on every card, name it with a leading _ (e.g., *_dog.jpg*) to tell Anki to ignore it when checking for media. If you delete media using the unused media check, Anki will move it into your operating system’s trash folder, so you can recover if you accidentally delete media that shouldn’t have been deleted.

Anki uses a program called mplayer in order to support sounds and videos. A wide variety of file formats are supported, but not all of these formats will work on AnkiWeb and the mobile clients. MP3 audio and MP4 video seems to be the most universally supported.

## MathJax support

[MathJax](https://www.mathjax.org/) is a modern, browser-based typesetting system, useful for mathematical and chemical equations. It does not require the installation of any extra software.

MathJax is supported out of the box on Anki 2.1+ and AnkiMobile - AnkiDroid does not yet have built in support for it.

To try it out:
1. Type the following in a field:
\sqrt{x}
2. Select the text you just typed.

3. Click the rightmost button in the editor, and choose "MathJax inline" from the menu. Anki will change the text so it reads:

\(\sqrt{x}\)

4. If you click the Cards… button, you’ll see a preview of how the equation will appear when the card is reviewed.

Anki’s MathJax support expects content in TeX format. If you’re not familiar with TeX formatting, please see [this cheatsheet](https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference). Please note that point 2 does not apply in Anki - Anki uses \( and \) for inline equations, and \[ and \] for display equations.

|     |     |
| --- | --- |
| Note | If you want to use newlines in a MathJax expression, please use Shift+Enter instead of just Enter, as a normal newline will prevent MathJax from working correctly. |

## LaTeX support

LaTeX is a powerful typesetting system, useful for entering mathematical formulas, chemical formulas, musical notation and so on. Anki provides some support for LaTeX, allowing you to enter LaTeX code in your notes. When you review a card, Anki will call LaTeX and display the generated image instead.

LaTeX is more work to set up, and images can only be generated with the computer version of Anki - though once generated, the images can be displayed by mobile clients. LaTeX does offer better support for advanced formatting however - if your needs are complicated, MathJax may not meet them.

### Installing and Assumed Knowledge

Anki’s LaTeX support is not turn-key: it is assumed that you know how to use LaTeX already, and that you have it installed. If you have no experience with LaTeX, please consult one of the many guides available on the internet. If you are having trouble with markup, please ask on a LaTeX forum.

To install LaTeX, on Windows use MiKTeX; on OSX use MacTex, and on Linux use your distro’s package manager. Dvipng must also be installed.

|     |     |
| --- | --- |
| Note | On Windows, go to Settings in MikTek’s maintenance window, and make sure "Install missing packages on the fly" is set to "No", not to "Ask me first". If you continue to have difficulties, one user reported that running Anki as an administrator until all the packages were fetched helped. |

|     |     |
| --- | --- |
| Note | On OSX, LaTeX has only been tested with MacTex and BasicTex. If you use BasicTex, you need to install dvipng separately, with the following command: |

sudo tlmgr update --self; sudo tlmgr install dvipng

The command may not be on the path, so you may need to provide the full path, eg /usr/local/texlive/2014basic/bin/x86_64-darwin/tlmgr.

|     |     |
| --- | --- |
| Note | If you are not using the above LaTeX packages, you will need to use the "edit LaTeX" add-on to specify the full path to latex and dvipng. |

### LaTeX on Web/Mobile

When you review a card with LaTeX on it, Anki will generate an image for that LaTeX and place the image in your collection’s media folder for future use. The web & mobile clients will display these images if they already exist, but can not generate the images on their own.

To avoid having to review all your cards at least once before you can study on the other clients, Anki can generate the images in bulk for you. To generate all the images, please go to Tools>Check Media. After that, syncing should upload the generated media to AnkiWeb and the other clients.

### Example

The most general way to input LaTeX content is to surround it with [latex][/latex] tags. There’s a shortcut button for this documented in the[editor](https://apps.ankiweb.net/docs/manual.html#editor) section.

|     |     |
| --- | --- |
| Warning | [latex] tags must be used inside a field - placing them in the card template will [cause problems](https://apps.ankiweb.net/docs/manual.html#mediarefs). |

For example, entering the following on the front of an Anki flashcard:

Does [latex]\begin{math}\sum_{k = 1}^{\infty}\frac{1}{k}\end{math}[/latex] converge?

will produce this when the flashcard is viewed:
![](../_resources/72fa7936b1c7c9f14a3c7a050893e6b8.png)

The formula in the example above is called a *text formula*, because it is displayed right within the non-mathematical text. In contrast, the following example shows a *displayed formula*:

Does the sum below converge?

[latex]\begin{displaymath}\sum_{k = 1}^{\infty}\frac{1}{k}\end{displaymath}[/latex]

![](../_resources/1da0d56fe077be4240b11c0379d49182.png)

*Text formulas* and *display formulas* are the most common type of LaTeX expressions, so Anki provides abbreviated versions of them. Expressions of the form:

[latex]\begin{math}...\end{math}[/latex]
can be shortened to
[$]...[/$]
and expressions of the form
[latex]\begin{displaymath}...\end{displaymath}[/latex]
can be shortened to
[$$]...[/$$]
For example, the two LaTeX snippets shown before are equivalent to
Does [$]\sum_{k = 1}^{\infty}\frac{1}{k}[/$] converge?
and
Does the sum below converge?
[$$]\sum_{k = 1}^{\infty}\frac{1}{k}[/$$]
respectively.

### LaTeX packages

Anki allows you to customize the LaTeX preamble so you can import custom packages for chemistry, music and so on. For example, imagine you find an example file for chemtex on the internet:

\documentclass[a4paper,12pt]{report}
\usepackage{chemtex}
\begin{document}
\initial
\begin{figure}[h]\centering
\parbox{.3\textwidth}{\ethene{H}{H$_3$C}{CH$_3$}{Br}}
\hfil
\parbox{.3\textwidth}{\cbranch{H}{S}{H}{S}{C}{S}{}{S}{H}
\xi=-200 \cright{}{Q}{C}{D}{O}{S}{OH}}
\hfil
\parbox{.3\textwidth}{\hetisix{Q}{Q}{Q}{Q}{Q}{Q}{O}{Q}{O}
\xi=-171 \fuseup{Q}{Q}{Q}{Q}{D}{Q}{D}{Q}{D}}
\caption{Chemie mit {\tt CHEMTEX}\label{a1}}
\end{figure}
\end{document}

Firstly, follow the documentation of the package and MiKTeX/MacTex in order to install the package. To check the package is working, you’ll want to put code like the above into a .latex file and test you can compile it from the command line. Once you’ve confirmed that the package is available and working, we can integrate it with Anki.

To use the package with Anki, click "Add" in the main window, then click the note type selection button. Click the "Manage" button, then select the note type you plan to use and click "Options". The LaTeX header and footer are shown. The header will look something like:

\documentclass[12pt]{article}
\special{papersize=3in,5in}
\usepackage{amssymb,amsmath}
\pagestyle{empty}
\setlength{\parindent}{0in}
\begin{document}

To use chemtex, you’d add the usepackage line in the earlier example, so it looks like:

\documentclass[12pt]{article}
\special{papersize=3in,5in}
\usepackage{amssymb,amsmath}
\usepackage{chemtex}
\pagestyle{empty}
\setlength{\parindent}{0in}
\begin{document}

After that, you should be able to include lines like the following in your Anki cards:

[latex]\ethene{H}{H$_3$C}{CH$_3$}{Br}[/latex]

### LaTeX Conflicts

It’s not uncommon for {{ and }} to pop up in LaTeX code when writing mathematical equations. To ensure that your LaTeX equations don’t conflict with Anki’s field replacements, it’s possible to change the separator to something else.

For example, if you have a template:
{{latex field}}

Changing it to the following will make it unlikely that the LaTeX will conflict:

{{=<% %>=}}
<%latex field%>

While this most commonly occurs with LaTeX, the solution presented here will work in any situation where you need to include {{ }} on cards, regardless of whether LaTeX is used or not.

When using cloze deletions, you cannot change the double braces used to mark cloze deletions; instead, you can put a space between any double closing braces that do not indicate the end of the cloze, so

{{c1::[$]\frac{foo}{\frac{bar}{baz}}[/$] blah blah blah.}}
will not work, but
{{c1::[$]\frac{foo}{\frac{bar}{baz} }[/$] blah blah blah.}}

will (and LaTeX ignores spaces in math mode, so your equation will render the same).

### Unsafe commands

Anki prohibits certain commands like \input or \def from being used on cards or in templates, because allowing them could allow malicious shared decks to damage your system. (To be on the safe side, these commands are prohibited even in comments, so if you’re getting this error but don’t think you’ve used one, please double-check any comments you have in your headers, templates, and cards.) If you need to use these commands, please add them to a system package and import that package as described in the previous section.

## Miscellanea

### Menu Shortcuts

On Windows/Linux you can hold down the alt key and press a highlighted letter to activate a particular menu.

OS X doesn’t support this feature, but it does allow you to assign shortcuts to specific menu items instead. Please seehttp://lifehacker.com/343328/create-a-keyboard-shortcut-for-any-menu-action-in-any-programfor more information.

### Debug Console

Sometimes you may be asked to use the debug console to change a setting or check something. Unless asked to enter text in the "debug console", you will probably not need this. Advanced users may like to read more about it in the add-ons page, linked below.

When asked to enter text into the "debug console", please start Anki, and in the main window, press

Ctrl+Shift+;
(the control key, shift key, and semi-colon key at the same time)
On a Mac, press
Command+Shift+;
(the command key, shift key, and semi-colon key at the same time)
On some non-English keyboards, you may need to press ":" or "+" instead of ";".

In the window that has popped up, please paste the text you were asked to paste in the top section. When you’ve done so, please press Ctrl+Return (Command+Return on a Mac), and some text should appear in the bottom section. If you’ve been asked to paste the resulting output, please copy it from the bottom area, and paste it back to the support person.

If you press Ctrl+Shift+Return instead of just Ctrl+Return, Anki will try to print the result rather than doing what you asked it to. If you are getting unexpected errors, please make sure you’re not holding down the Shift key.

### Add-ons

Anki’s capabilities can be extended with add-ons. Add-ons can provide features like extra support for specific languages, extra control over scheduling, and so on.

To browse the list of available add-ons, select the Tools>Add-ons menu item, then click on Get Add-ons.

Many add-on authors include their email address in the add-on, so if you need to get in touch with the author, editing the add-on and looking at the top of the file may help.

If you have downloaded an add-on that is not working properly, or if you accidentally made a mistake when editing an add-on, you can use the "Delete" option in the menu to remove it.

To learn how to write your own add-ons, please see the [add-on writing guide](https://apps.ankiweb.net/docs/addons.html).

## Contributing

### Sharing Decks Publicly

To share decks with the general public, [synchronize](https://apps.ankiweb.net/docs/manual.html#syncing) them with AnkiWeb, then log into AnkiWeb and click on "Share" from the menu next to the deck you wish to share.

If you shared a deck previously (including with previous versions of Anki), you can update it by clicking "Share" as above. Please ensure the name of the deck in your account exactly matches the name shown in the shared deck listing, or you’ll end up creating a new shared deck rather than updating the old one. Updating a shared deck will not reset the download counts or ratings. You can delete a shared deck that you have uploaded using the Delete button on the shared deck’s page.

When you update a shared deck, users who downloaded the deck previously will not automatically receive updates. If they download the deck again and re-import it, newly added material will be imported without altering their existing study progress, provided neither you nor the user has altered the note type since the first import.

|     |     |
| --- | --- |
| Note | When updating a deck, AnkiWeb expects the deck to be at the same location as before. If you shared a deck when it was called "Korean Verbs" for example, and then renamed it to "Korean::Korean Verbs", resharing will not be able to update the existing copy. |

### Sharing Decks Privately

If you’d like to share decks with a limited group of people (such as a study group or class) rather than the general public, you can do so by sharing them outside of AnkiWeb.

To share a deck privately, go to the File menu and choose Export. Select a single deck (not "All Decks"), and turn off "include scheduling information". This will produce an .apkg file which you can share with others.

You can share the .apkg file by emailing it to people, placing it on a website or shared folder, or using a free file sharing service like Dropbox or Google Drive and sending people a link.

Both the computer version and mobile clients make it easy to import from an apkg file simply by clicking or tapping on it. AnkiWeb does not have the ability to import apkg files however, so the recipients of your deck will need to have the computer version or Anki on their mobile device.

When a user imports an .apkg file, cards that already exist in their collection will be ignored and any new cards will be added. As long as they use the same note type, modified cards will also be updated. To prevent data loss, cards that have been deleted in the new apkg file will not be deleted in the user’s collection, so if you need to delete cards from users' decks for whatever reason, you will need to contact them about it.

### Sharing Add-ons

Please see the add-on documentation above.

### App Translations

Translations can be done directly from the[translation website](https://translations.launchpad.net/anki/trunk).

Launchpad will guess which languages you can translate based on the country you’re connecting from. If the language you want to translate to doesn’t appear, sign up for a launchpad account, and in your profile, click the *!*next to preferred languages to the language you want to translate.

There are some special markers in text that you need to be aware of, and careful when translating:

- A string like Cards: %d or Error: %s means that the %d/%s part will be replaced with some other value. The characters must remain the same in the translation, so a translation may look like カード: %d.
- The same applies to text like %(a)d of %(b)d - it would be translated like %(a)d von %(b)d. If you need to reverse A and B in your language, that’s fine as long as the text remains the same.
- Menu items have an & to indicate which character is the shortcut key, such as &File. In languages that use roman text, you can place the & over a different character such as &Datei; in other languages there may be a different convention. Japanese for example includes the roman character afterwards instead, like ファイル (&F)
- Some strings have plural support, so that "0 cards", "1 card", "5 cards" can be represented properly in your language. In these instances you’ll need to enter the 2 or 3 different forms.

Sometimes it will not be clear what a string refers to, and you may want to see the context. Below every string to be translated, you’ll see a line like this:

Located in ../dtop/aqt/deckbrowser.py:299

If you strip off the first "../dtop" section, you’re left with something like "aqt/deckbrowser.py:299". You can then visit https://github.com/dae/anki/, locate the same filename, and click on it. The file will be displayed with line numbers on the left, and by matching up the line numbers (they may differ by a few lines sometimes), you may be able to get a better understanding of what the string refers to.

If you see *forms* in the string like the above example, the strings will generally be obvious. If you do need to understand the context however, things are a little more complicated, as those files are automatically generated from an interface description instead. Please go tohttps://github.com/dae/anki/tree/master/designer and locate the same filename and click on it. We can’t rely on line numbers in this case, so please use the browser’s find option to find the string in the file. The lines immediately surrounding the found text may give a clue as to its meaning.

If you find a string that you’re unsure how to translate, or would like to start a discussion with fellow native speakers on the best way to translate something, please feel free to start a thread in the Anki forums.

If the language already appears in Anki’s preferences screen, updates you make will automatically be included in future Anki releases.

If the language is not currently visible in Anki’s preferences screen, please post on our support site and request that the language you’ve translated be added to the list.

Any translations that were made at least a few hours before a new Anki release are automatically included in the next release. Entirely new languages need to be added manually, so please contact us if that applies to your translation. If you’d like to see your name in the About screen as a contributor, please drop Damien a line.

If you’d like to try out your translations without waiting for a new release, you can export a .mo file from the translation website. If you then move that .mo file into Anki’s installation folder, overwriting an existing .mo file with the same language code (in the locale folder), Anki will display the new translations when it is next started.

### Translating the Manual

If you’re a fairly technical user, you may want to translate the[source file](https://raw.github.com/dae/ankidocs/master/manual.txt) of the manual, and compile it yourself with asciidoc. You can also use that github repo to keep track of changes to the manual in the future.

If that sounds complicated, an easier way is to visit this page and use File>Save As to save the manual to disk. You can then import it into Microsoft Word or similar software, and translate it that way.

When you’re happy with the translation, you can either put it up on your website and I can link to it, or I can host the translated file on Anki’s website (but if you’re planning to make frequent updates, the former is a better choice). If you’d like, you can post it before you’re done and we can link to it in the list of in-progress translations below.

Another option is to put your translation on a wiki, so that other users can contribute to it. There are many sites such as [Wikia](http://www.wikia.com/) that will allow you to easily create your own wiki for free. (The English version once used a wiki; we found that we got too many unhelpful contributions and had to spend too much time correcting them, but your mileage may vary.)

The following translations are currently in progress:

- Hungarian
- Portuguese

If you would like to help with one of these translations, please contact us on TenderApp and we will put you in touch with the user(s) currently working on it.

### Contributing Code

Anki’s source code is available at https://github.com/dae/anki
Before contributing, please see the README.contributing file in that repo.

## Frequently Asked Questions

### I haven’t studied for a while, and now the next due times are too big!

When you use Anki every day, each time a card is answered correctly, it gets a bigger interval. Let’s assume that *good* about doubles the interval. Thus you have a 5 day wait, then a 10 day wait, 20 days, 40 days, and so on.

When people return to their deck after weeks or months of no study, they’re often surprised by the length intervals have grown to. This is because Anki considers the actual time the card was unseen, not just the time it was scheduled for. Thus if the card was scheduled for 5 days but you didn’t study for a month, the next interval will be closer to 60 days than 10 days.

This is a good thing. If you have successfully remembered a card after a one month wait, chances are you’ll remember it again after a longer wait, too. The same principles which make SRS effective in normal use apply when you’re studying after a delay, too. It also makes little sense to schedule a card for 10 days in the future if you were able to easily answer it after a whole month’s wait - you’d be going backwards.

Resetting the deck is an even worse solution. When returning to a deck after a long absence, you may have forgotten many of your cards, but chances are you haven’t forgotten them all. Resetting the entire deck means you have to waste time studying material you already know.

Now you may find overdue cards that you were able to recall, but not comfortably, since they were not reviewed when they should have been. To counter this, Anki treats the delay differently depending on your answer. If you find a card easy, the last interval plus the full delay are added together, and then used to calculate the next interval. When you answer good, only half the delay is used. And when you answer hard, only a quarter of the delay is used, or 0 if you are using the experimental scheduler. So if a card was due in 5 days, and it’s answered 20 days late, the next times you’d end up with are approximately:

- Hard: (5 + 20/4) * 1.2 = 12 days (or 6 days with the experimental scheduler)
- Good: (5 + 20/2) * 2.5 = 37.5 days
- Easy: (5 + 20) * 3.25 = 81.25 days

(the factors will actually vary depending on your performance in the deck)

If you find a card hard, the next interval is quite conservative and is less than the last wait (25 days). If you find it good, the next interval is only about 50% higher. And easy increases the interval aggressively as usual.

So it is recommended that you study as normal when you return to Anki after a period of absence. But if you absolutely must reset the deck, you can select the cards to reset in the browser, and use Edit>Reschedule.

### Can I do multiple-choice questions?

Multiple choice questions are a poor review tool for a number of reasons. The reason they are commonly used in an academic setting is because they are easy to mark, and they allow the person studying to demonstrate their ability to recognize the correct answer even if they can’t produce it themselves.

Furthermore, good multiple choice questions have well chosen "distractors" - answers that are similar to the correct answer. A computer can look for similarly spelt words, but it is not capable of choosing good distractors for more complicated topics.

If you are studying for a test and you have a sample test with a multiple choice question like the following:

Q: What animal has a really long neck?
A: 1. A monkey. 2. A giraffe. 3. A donkey. 4. A snail.
Then that question should be rewritten in Anki as follows:
Q: What animal has a really long neck?
A: A giraffe.
Or you can add your own choices:
Q: What animal has a really long neck? (dog/cat/giraffe/penguin)
A: A giraffe.

### Can I link cards together? Add dependencies? How should I handle synonyms?

Anki supports links between cards of a note, but not between unrelated cards. Imagine are you studying Japanese and aiming to be able to both recognize and reproduce the Japanese. You may enter the word "ookii", which means "big", and tell Anki to generate two cards - ookii→big and big→ookii.

In the above situation Anki can space reviews of those two sibling cards out so that they don’t appear one after the other (see [sibling spacing](https://apps.ankiweb.net/docs/manual.html#siblings) in the link at the top of this document).

Some people want to extend this link between arbitrary cards. They want to be able to tell Anki "after showing me this card, show me that card", or "don’t show me that card until I know this card well enough". This might sound like a nice idea in theory, but in practice it is not practical.

For one, unlike the sibling card case above, you would have to define all the relations yourself. Entering new notes into Anki would become a complicated process, as you’d have to search through the rest of the deck and assign relationships between the old and new material.

Secondly, remember that Anki is using an algorithm to determine when the optimum time to show you material again is. Adding constraints to card display that cause cards to display earlier or later than they were supposed to will make the spaced repetition system less effective, leading to more work than necessary, or forgotten cards.

The most effective way to use Anki is to make each note you see independent from other notes. Instead of trying to join similar words together, you’ll be better off if you can determine the differences between them. Synonyms are rarely completely interchangeable - they tend to have nuances attached, and it’s not unusual for a sentence to become strange if one synonym is replaced with another.

Continuing with the Japanese example earlier, imagine you want to learn the word "dekai", which also roughly translates to "big", but is a more colloquial expression. If you still want to review in both directions, you might make the English prompt of this word "big (more casual)". The further you progress in your language studies though, the more of a burden it becomes to define the differences between similar words, which is why cards asking you to produce a particular word are best left to the early stage of your studies. With a strong base vocabulary, moving towards recognition-based study makes more sense, as we all have a much larger passive vocabulary than our active vocabulary.

As for ensuring that difficult material is introduced after easier material, a number of existing tools are available. New cards are by default introduced in the order they are added to the deck, so as long as the learning materials or sources of information you are using are adequately graded for your level, material should appear in order of easiness.

### Can I give my notes an arbitrary number of fields?

Notes are designed to represent *closely* related information, and to make it easy to reorganize where that information appears on a card. In the context of language learning, notes are useful for representing things like a phrase-translation pair, a phrase-translation-reading triplet, and so on. All of these relationships are 1:1 - a given phrase has only one reading, and one translation. (1)

Because of their ability to tie related pieces of information together, some people try to use notes to tie less closely related information in their deck together. For example, if they come across two sentences with the word "completely":

- He was completely confused.
- That was completely uncalled for.

Then they put those two sentences in the same note, under the rationale that since they share a word, they are related. But what if the user comes across another example sentence?

- The book confused her.

That sentence shares the word "confused" with a previous sentence. So should it be in the note for "confused"? Or the note for "completely"? Or both?

Unlike the phrase-translation pairs mentioned above, if you say sentences are related if they share a word, then sentences have a many:many relationship. That is, sentence A may be related to sentence B and C, sentence B may be related to A and D, and so on. Because the relationships are complex and overlapping, notes are not a good way to represent them.

There seem to be two main reasons people try to represent such relationships in notes:

- "Because it’s neater to keep all the information in one place". This may seem to be the case, but in reality you really don’t save much. If you want to see all example sentences that contain the word "completely" and each sentence is in a different note, all you have to do is search for "completely".
- "Because I want Anki to separate reviews of cards that share the same word". This is related to the previous FAQ question. Defining the links between cards is time consuming, and if it were done automatically and every card that shared a word were separated from other cards that shared a word, it would be both computationally prohibitive, and would likely lead to a situation where nothing could be shown because it was all related to something else. Yes, it’s not ideal for two sentences containing the same word to be shown right after each other, but if you add new cards in a random order such a situation is unlikely, and the downsides of trying to prevent such a situation aren’t worth it. And even if such a solution were introduced, it wouldn’t stop you from encountering the words in the real world.

(1) It is possible for different people to translate the same phrase in different ways, and different dialects may read the same word differently, but that is not relevant to the discussion.

### Can I host my own AnkiWeb?

Sorry, AnkiWeb is only available as a hosted service.

### Why is the Android version free when the iPhone version isn’t?

Working on Anki desktop, AnkiWeb and AnkiMobile is my full time job, and I need some way of paying the bills. Since I make the desktop & web versions available for free, I rely on sales of the iPhone app in order to finance development.

AnkiDroid is written by a separate group of volunteers. Since they based it on the free desktop version I make available (and rely on AnkiWeb in order to synchronize decks), they decided to make it freely available as well.

### What spaced repetition algorithm does Anki use?

Anki’s algorithm is based on the SuperMemo 2 algorithm. For info on SM-2, please see http://www.supermemo.com/english/ol/sm2.htm

Anki’s algorithm differs from SM-2 in some respects. Notably:

- SM-2 defines an initial interval of 1 day then 6 days. With Anki, you have full control over the length of the initial learning steps. Anki understands that it can be necessary to see a new card a number of times before you’re able to memorize it, and those initial "failures" don’t mean you need to be punished by being shown the failed card many times over the course of a few days. Performance during the learning stage does not reflect performance in the retaining stage.
- Anki uses 4 choices for answering review cards, not 6. There is only one *fail* choice, not 3. The reason for this is that failure comprises a small amount of total reviews, and thus adjusting a card’s ease can be sufficiently done by simply varying the positive answers.
- Answering cards later than scheduled will be factored into the next interval calculation, so you receive a boost to cards that you were late in answering but still remembered.
- Like SM-2, Anki’s failure button resets the card interval by default. But the user can choose to have the card’s interval reduced instead of being reset completely. Also, you can elect to review failed mature cards on a different day, instead of the same day.
- *Remembered easily* not only increments the ease factor, but adds an extra bonus to the current interval calculation. Thus, answering *remembered easily* is a little more aggressive than the standard SM-2 algorithm.
- Successive failures while cards are in learning do not result in further decreases to the card’s ease. A common complaint with the standard SM-2 algorithm is that repeated failings of a card cause the card to get stuck in "low interval hell". In Anki, the initial acquisition process does not influence a card’s ease.

You can also check out *sched.py* in Anki’s source code for the scheduling code. Here is a summary (see the [deck options](https://apps.ankiweb.net/docs/manual.html#deckoptions) section for the options that are mentioned in *italics*).

If you press…
Again

The card is placed into relearning mode, the ease is decreased by 20 percentage points (that is, 20 is subtracted from the *ease* value, which is in units of percentage points), and the current interval is multiplied by the value of *new interval* (this interval will be used when the card exits relearning mode).

Hard

The card’s ease is decreased by 15 percentage points and the current interval is multiplied by 1.2.

Good
The current interval is multiplied by the current ease. The ease is unchanged.
Easy

The current interval is multiplied by the current ease times the *easy bonus* and the ease is increased by 15 percentage points.

For Hard, Good, and Easy, the next interval is additionally multiplied by the*interval modifier*. If the card is being reviewed late, additional days will be added to the current interval, as described [here](https://apps.ankiweb.net/docs/manual.html#duetimestoobig).

There are a few limitations on the scheduling values that cards can take. Eases will never be decreased below 130%; SuperMemo’s research has shown that eases below 130% tend to result in cards becoming due more often than is useful and annoying users. Intervals will never be increased beyond the value of *maximum interval*. Finally, all new intervals (except Again) will always be at least one day longer than the previous interval.

|     |     |
| --- | --- |
| Note | After you select an ease button, Anki also applies a small amount of random “fuzz” to prevent cards that were introduced at the same time and given the same ratings from sticking together and always coming up for review on the same day. This fuzz does not appear on the interval buttons, so if you’re noticing a slight discrepancy between what you select and the intervals your cards actually get, this is probably the cause. |

### Why doesn’t Anki use SuperMemo’s latest algorithm?

The simple answer is that SuperMemo’s latest algorithm is proprietary, and requires licensing. As Anki is an open source application, it can only make use of algorithms that have been made freely available.

We’re inclined to believe SuperMemo when they say their newer algorithms are more efficient, but feel that to a certain extent, it is a case of diminishing returns. The gains achieved by moving from a traditional study routine to SM-2 are already great, and by sticking with an open algorithm, your learning data is not locked into a single product.

Ultimately it’s up to you to decide - if access to the latest and greatest scheduler is a higher priority than the things that Anki brings to the table, you may want to check out SuperMemo to see if it is a good fit for you.

### What about SM-5?

Anki’s scheduler was originally based on[SM-5](https://www.supermemo.com/english/ol/sm5.htm). Anki’s default of showing the next interval above each ease button revealed problems with the implementation - harder cards could end up with greater interval increases than easy ones, and the ease factors sometimes grew to the point where a single review could result in a 20-30x increase in interval.

An attempt was made at the time to correct this by smoothing the optimal factors matrix - applying a cap on the maximum factor and enforcing a minimum difference between adjacent ease factors. This addressed the above problems, but resulted in an optimal factors matrix that had very little room to move, and the conclusion drawn at the time was that SM-5 was not an improvement over SM-2.

While SM-5 clearly wasn’t working for Anki, in hindsight, it may not have been fair to assume the issues we encountered were due to fundamental problems with the algorithm. SuperMemo have subsequently stated that the description of the SM-5 algorithm listed on their website is incomplete, so it is possible the problems we encountered do not exist in SuperMemo’s proprietary implementation.

## Resources

The SuperMemo site has a lot of good information about spaced repetition and memory: http://www.supermemo.com/

Michael Nielsen has written a [thorough piece](http://augmentingcognition.com/ltm.html) about long term memory and how he uses Anki. He also provides a[condensed version](https://twitter.com/michael_nielsen/status/957763229454774272) as a series of tweets.