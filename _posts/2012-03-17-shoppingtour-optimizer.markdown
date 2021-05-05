---
comments: true
date: 2012-03-17 15:17:39
layout: post
title: Shopping tour Optimizer
description: Unser Beitrag zum InformatiCup 2012
wordpress_id: 1772
tags:
- anser set programming
- KI
- Python
---

Wie schon im letzten Jahr habe ich mit einigen Kommilitonen am InformatiCup teilgenommen. Dieses Mal ging es darum ein Programm zu schreiben, dass eine Einkaufstour optimiert. Gegeben ist eine Menge von Läden, in denen man Produkte kaufen kann und eine Einkaufsliste. Ziel ist es, möglichst günstig die Einkaufsliste abzuarbeiten. Problem ist dabei, dass es nicht alle Produkte überall gibt, die Preise für gleiche Produkte verschieden sind und die Läden an verschiedenen Orten liegen, sodass Fahrtkosten entstehen.

Die Aufgabe gibt es [hier](http://www.gi.de/wir-ueber-uns/wettbewerbe/informaticup/informaticup-2012.html).

Da wir in diesem Jahr ziemlich viel mit der Uni beschäftigt waren, haben wir das Projekt praktisch in drei Wochen vor der Abgabe schreiben müssen. Aber dafür ist es doch ganz cool geworden.

Wir nutzen für die Lösung des Problems zwei Algorithmen. Einerseits benutzten wir einen genetischen Algorithmus, welcher schnell zu einer guten Lösung kommt. Diese ist jedoch nicht notwendigerweise optimal. Um eine optimale Lösung zu finden, wird das Problem als Answer Set Programming Problem kodiert und dann von Clasp gelöst.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/HSMU7a_TlgI" frameborder="0" allowfullscreen></iframe>

Code is [auf GitHub](https://github.com/domoritz/informaticup-2012).
