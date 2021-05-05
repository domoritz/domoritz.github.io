---
layout: post
title: UTC vs GMT vs London Local Time
description: Über die Verwirrungen durch Zeitstandards
date: 2012-04-09 20:15
comments: true
tags:
  - utc
  - gmt
---

Ich hab mich gerade gefragt, ob die GMT auch Sommerzeit mit einbezieht und wie denn die UTC dazu steht. Nach einiger Recherche konnte ich etwas Licht in das Dunkel bringen. Wen es also interessiert, hier die harten Fakten.

GMT (Greenwich Mean Time) ist der alte Zeitstandard, an dem alles Zeitzonen ausgerichtet wurden. GMT wurde als primäre Referenz für das Britische Empire eingeführt und wurde schnell zum allgemeinen Standard. Der BBC World Service arbeitet nach GMT. Nun kam es jedoch, dass die Sonne und die Erde nicht so regelmäßig sind und die Zeit von Zeit zu Zeit angeglichen werden muss. Dabei geht es nicht um Sommer- und Winterzeit, sondern Schaltsekunden.

GMT ist unabhängig von Sommer und Winterzeit.

**UTC (Coordinated Universal Time)** wurde am 1. Januar 1972 offizieller Standard und richtet sich, wie GMT, nach der Zeit bei Null Grad Longitudinal, was den Nullmeridian bezeichnet, der durch den Londoner Stadtteil Greenwich geht. Im Gegensatz zu GMT gibt es jedoch alle paar Jahre Schaltsekunden, um der verlangsamenden Erdrotation zu folgen. Da die Abweichung zu GMT sehr gering ist, wird die UTC teilweise auch als GMT bezeichnet (z.B. vom BBC).

**UTC** ist auch der Standard für alle Zeiten im Internet und im internationalen Handel.

London Local time ist die Zeit, welche in London gilt. Das heißt im Winter UTC und im Sommer die BST (Britisch Summer Time), welche UTC+01:00 entspricht.

**CET (Central European Time)** entspricht UTC+01:00 und gilt in Mitteleuropa in Winter. CET hat keine Sommerzeit.

Unix time richtet sich an der UTC aus und wird in Sekunden seit Donnerstag, 1. Januar 1970 angegeben. Die Umrechnung in UTC ist nicht trivial, da Schaltjahre, Schaltsekunden und eventuell die Sommerzeit mit eingerechnet werden müssen.

Also nun noch der ultimative Tipp, wenn man Zeiten ganz klar ausdrücken will. Zeit in Lokaler Zeit angeben oder auf UTC verweisen. Für die Umrechnung empfehle ich [Wolfram Alpha](http://www.wolframalpha.com).
