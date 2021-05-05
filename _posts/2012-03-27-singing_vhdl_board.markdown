---
comments: true
date: 2012-03-27 13:59:57
layout: post
title: The singing VHDL board
description: Ein Muskspieler mt Kartenleser programmiert
wordpress_id: 1781
tags:
- FPGA
- HPI
- SD
- Spartan 3
- VHDL
- XILINX
---

Nach 6 Monaten warten ist es so weit! Es lebt.

Vor etwas mehr als 6 Monaten habe ich mit einem [Kommilitonen](https://www.kaifabian.de/) angefangen an einem Musikplayer in VHDL zu arbeiten. Dadurch, dass wir im letzten Semester kaum Zeit gefunden haben, hat sich die Entwicklung etwas verzögert. Nichtsdestotrotz waren wir unheimlich stolz, als wir zum ersten Mal etwas hörten, was eine Melodie sein könnte und nach ein paar Bitoperationen auch richtige Musik hörten.

Was ist denn nun sooooo toll an dem Player? Naja, einerseits ist alles in VHDL implementiert, das heißt, dass alles in Hardware läuft und wir uns wirklich um jedes Bit kümmern müssen. Andererseits haben wir wirklich alles selber implementieren müssen und konnten nicht auf ein Betriebssystem oder Programmbibliotheken zurückgreifen.

Das Ganze haben wir auf einem Spartan 3 [FPGA](http://en.wikipedia.org/wiki/Fpga) Board aufgebaut, an das wir über eine Schnittstelle einen SD/MMC Slot und einen [DAC](http://en.wikipedia.org/wiki/Digital-to-analog_converter) mit einem Kopfhörerausgang angeschlossen haben. Die Musik ist liegt als unkomprimiertes [WAV/RIFF](http://en.wikipedia.org/wiki/Wav) auf der Karte.

<iframe width="560" height="315" src="//www.youtube.com/embed/qsjFVgriZzY" frameborder="0" allowfullscreen></iframe>

Der Player besteht aus vier Hauptkomponenten. Als erstes gibt es einen MMC/SD Kartenleser, welcher das [SPI](http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus) Protokoll zur Kommunikation mit der Karte implementiert. Dazu mussten wir uns durch die Dokumentation der Karten arbeiten und die verschiedenen Schritte zur Initialisierung der Karte, dem Senden von Befehlen und Empfangen von Datenblöcken implementieren. Da die Karte immer 512 Byte Blöcke auf einmal liefert und wir diesen nicht auf dem FPGA Chip speichern können (das sind immerhin 512*8 = 4096 Bit!) nutzen wir eine Blockram Fifo, die auf dem Board verbaut ist. Die Ausgangsseite der Fifo ist an eine weitere Komponente angeschlossen, die auch wieder per (dieses Mal sehr einfachen) SPI mit dem DAC kommuniziert. Der DAC wandelt dann eine digitale 12 Bit Zahl, die von der Karte durch die Fifo kam, in eine analoge Spannung um. Und das ist dann das, was der Kopfhörer oder Lautsprecher ausgibt.

Besonders interessant fand ich bei der Entwicklung den MMC Kartenleser. Dabei hat uns besonders das Datenblatt von Samsung geholfen, dass du [hier](http://html.alldatasheet.com/html-pdf/141187/SAMSUNG/MC2GH512NMCA-2SA00/616/2/MC2GH512NMCA-2SA00.html) finden kannst. Der Sourcecode ist auf [Github](https://github.com/domoritz/S76D). Wer also auch einen SD/MMC Kartenleser in VHDL bauen will, kann sich dann inspirieren lassen.

Das Programm ist noch nicht ganz fertig und wir arbeiten gerade noch an der Tastatursteuerung per PS/3 Tastatur. Stay tuned.
