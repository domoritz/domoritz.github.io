---
comments: true
date: 2012-03-17 13:30:02
layout: post
title: Tagshot und andere Projekte
description: Fotoverwaltung im Browser
wordpress_id: 1763
tags:
- HPI
- jQuery
- Photos
- Tagshot
---

In diesem Artikel möchte ich das Fotoverwaltungstool vorstellen, was treffenderweise _Tagshot_ heißt.

Das Programm habe ich mit vier Kommilitonen im Rahmen eines Studienseminars erstellt und soll dabei helfen, die große Anzahl an Photos, die am HPI aufgenommen werden, zu verwalten. Verwalten heißt dabei suchen, taggen, bewerten, herunterladen, löschen und auch nur einfach ansehen um gute Bilder zu finden.

Wir haben das Tool bei uns am HPI bereits in Benutzung und haben etwa 10.000 Bilder in der Datenbank. Dabei ist beim Suchen keine Verzögerung spürbar.

Ein wenig zur Technik. Das Backend ist in [Ruby on Rails](http://rubyonrails.org/) geschrieben und sucht nach Bildern in einem bestimmten Verzeichnis. Die Metadaten der Bilder werden in eine Datenbank geschrieben (bei uns [postgreSQL](http://www.postgresql.org/)) und Thumbnails erzeugt. Das Frontend ist eine einzige Seite, auf der mit JavaScript die Website dynamisch aufgebaut wird. Auch die gesamte Navigation findet auf einer Seite statt. Als Grundframework für das Frontend haben wir [Backbone.js](http://backbonejs.org/) benutzt.

Coole Features von Tagshot sind:

  * Taggen und bewerten von Bildern
  * Bilder nach Bewertung und Tags durchsuchen. Dabei können Boolesche Operatoren benutzt werden
  * Schnellvorschau
  * Unendliches Scrollen und dynamisches Nachladen von Bildern
  * Tastaturnavigation für schnelles Bearbeiten
  * Vergrößern/ Verkleinern der Ansicht
  * Detailansicht
  * Verschiedene Auflösungen herunterlade
  * Bearbeiten von mehreren Bildern gleichzeitig
  * Getestet in Webkit und Firefox


Das Projektrepo (Git) und die Projektorganisation (Redmine) sind zur Zeit noch am HPI gehostet, werden aber bald auf [https://github.com/tagshot/tagshot](https://github.com/tagshot/tagshot) umziehen. Das Projekt ist immer noch in der Entwicklung und einige Features fehlen noch (drehen von Bildern...), aber Tagshot ist trotzdem schon gut benutzbar und schnell.

<update>Die Quellen sind online auf [https://github.com/tagshot/tagshot](https://github.com/tagshot/tagshot)</update>

Auf Youtube gibt es kleines Demovideo, dass die wichtigsten Grundfunktionen zeigt.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/nB3fcDLNk8g" frameborder="0" allowfullscreen></iframe>
