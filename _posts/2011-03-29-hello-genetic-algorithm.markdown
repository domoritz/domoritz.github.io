---
comments: true
date: 2011-03-29 22:44:57
layout: post
title: Hello Genetic Algorithm
wordpress_id: 1557
tags:
- AI
- Python
---

Hier mal ein Optimierungsalgorithmus, mit dem sich verschiedenste Probleme lassen können. Hier soll es einfach nur darum gehen, den Text "Hello World!" zu finden. das Problem ist insofern nicht so schwer, weil es keine lokalen Maxima gibt, in denen der Algorithmus hängen bleiben kann und es lässt sich einfach feststellen, dass das Optimum erreicht worden ist.

An sich kann ein genetischer Algorithmus aber auch solche Probleme lösen, bei denen es lokale Maxima gibt oder nicht die optimale, sondern nur eine sehr gute Lösung gefunden werden soll. Ein andere Algorithmus für diese Art von Problemen ist die simulierte Abkühlung ([passender Blogeintrag](http://www.dmoritz.bplaced.de/2011/01/informaticup-2011/)).

Genug der Worte, hier der Code. Ich muss dazu sagen, dass ich ich ihn auf einer Bahnfahrt zusammengehackt habe und das Prinzip des genetischen Algorithmus aus den Gedächtnis herleiten musste, wobei dies das erste Mal ist, dass ich überhaupt einen genetischen Algorithmus geschrieben habe. Kommentare willkommen, aber bitte nicht über den Stil, es ging nicht um schönen Code, sondern einfach mal den Versuch, zur Lösung zu kommen.

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

def bewertung(individuum):
	#return sum( abs(ord(individuum[i])-ord(z)) for i,z in enumerate(ziel))
	return sum(1 for i,x in enumerate(ziel) if individuum[i] != x)

def mutation(individuum):
	pos = int(random.random()*len(individuum))
	ran = moegl[int(random.random()*len(moegl))]
	indivliste = list(individuum)
	indivliste[pos]=ran
	individuum = "".join(indivliste)
	return individuum

def paarenLassen(individuum1, individuum2):
	individuum1 = list(individuum1)
	individuum2 = list(individuum2)
	for i,x in enumerate(individuum1):
		if random.random() >= 0.5:
			individuum1[i] = individuum2[i]
	return "".join(individuum1)

def findLooser(population):
	gewichte = map(bewertung,population)
	max = gewichte[0]
	maxpos = 0
	for i,x in enumerate(gewichte):
		maxpos, max = (maxpos, max) if x < max else (i,x)
	return maxpos

def findMinMax(anz,reverse):
	liste = []
	for individuum in population.keys():
		liste.append((individuum,population[individuum][1]))
	liste.sort(cmp = lambda a,b: cmp(a[1],b[1])*(-1 if reverse else 1))
	liste = liste[:anz]
	return [a for a,b in liste]

def printAll():
	for individuum in population.keys():
		print individuum, population[individuum][0], population[individuum][1]
	print "###############"

ziel = "Hello World!"
moegl = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !@$%^&*()=+-?<>"
population = {}

#Anfangspopulation
for x in range(0,30):
	individuum = "".join([moegl[int(random.random()*len(moegl))] for x in range(0,len(ziel))])
	population[individuum] = [bewertung(individuum),0]

print "Ausgangspopulation:"
printAll()

anzahl = 0
while ziel not in population:
	anzahl += 1

	#print 'neue Generation'

	#Bewertung
	for individuum in population.keys():
		population[individuum] = [bewertung(individuum),0]
		population[individuum][1] = population[individuum][0]*random.randrange(9,11)*0.1
	#print 'Bewertung'
	#printAll()

	#Selektion
	selektion = findMinMax(6,False)
	#print 'selektion', selektion

	#Rekombination, Crossover
	kinder = []
	selektion2 = selektion[:]
	random.shuffle(selektion2)
	random.shuffle(selektion)
	while selektion:
		kinder.append(paarenLassen(selektion.pop(), selektion.pop()))
		kinder.append(paarenLassen(selektion2.pop(), selektion2.pop()))
	#print 'kinder', kinder

	#Mutation
	for index, kind in enumerate(kinder):
		while True:
			mutant = mutation(kind)
			if not mutant in population.keys() and not mutant in kinder:
				break
		kinder[index] = mutant
	#print 'mutierte Kinder', kinder

	#sterben lassen
	maxima = findMinMax(6,True)
	for maximum in maxima:
		population.pop(maximum)

	#neue Population
	for individuum in kinder:
		population[individuum] = [0,0]

print "Letzte Population:"
printAll()
print "Benötigte Generationen:", anzahl

```


### Ausblick (was man noch verbessern sollte):

  * Objektorientiert
  * Kommentare
  * variable Parameter
    * Größe der Population
    * Anzahl der Kinder
    * Stärke der Mutation
    * mehr/weniger Zufall bei der Auswahl für Rekombination
    * am besten neu schreiben, so unsauber, wie das ist :-)

### Noch zwei ganz nette Seiten zum Thema


[http://www.obitko.com/tutorials/genetic-algorithms/index.php](http://www.obitko.com/tutorials/genetic-algorithms/index.php)
[http://www.ai-junkie.com/ga/intro/gat1.html](http://www.ai-junkie.com/ga/intro/gat1.html)
