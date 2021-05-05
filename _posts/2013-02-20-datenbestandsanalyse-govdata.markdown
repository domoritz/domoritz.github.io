---
layout: post
title: "Datenbestandsanalyse GovData"
description: "Was wir jetzt schon über die Daten im neuen Datenportal sagen können."
date: 2013-02-20 00:18
comments: true
categories:
tags:
-  opendata
---

Die neue [Datenplattform des <abbr title="Bundesministerium des Innern">BMI</abbr>](http://www.govdata.de) ist heute mit ein paar Startschwierigkeiten online gegangen. Der Datenbestand umfasst zur Zeit 1123 Datensätze. Ich habe mir mal ein Script geschrieben, dass etwas aggregiert, was für Daten auf der neuen Plattform zu finden sind.

Die Rohdaten habe ich über die [CKAN API](http://docs.ckan.org/en/latest/api.html) erhalten. Einen Dump aller `packages` (Datensätze) mit `resources` gibt es mit `curl http://www.govdata.de/ckan/api/3/action/current_package_list_with_resources -d '{}' > data.json`{:lang="bash"}.

Da GovData gerade offline ist, hier der [Link zum Datendump](https://dl.dropbox.com/u/12770094/govdata/data-19-2-2013.json)

# Datensätze

Auf der GovData Plattform gibt es neben Datensätzen auch Dokumente und Apps. In dieser Zusammenfassung betrachte ich jedoch nur Datensätze.

## Unter welchen Lizenzen stehen die Daten?

Aggregiert aus `result.license_id`.

```
     dl-de-by-1.0: 759
            cc-by: 265
           odc-by: 82
             None: 4
     other-closed: 4
         cc-by-sa: 3
          cc-zero: 2
official-work: 2
            cc-nc: 1
             gfdl: 1
```

* **odc-by:** Open Data Commons Namensnennung
* **cc-zero:** Creative Commons Zero
* **cc-by:** Creative Commons Namensnennung (CC-BY)
* **cc-by-sa:** Creative Commons Attribution Weitergabe unter gleichen Bedingungen (CC-BY-SA)
* **cc-nc:** Creative Commons Nicht-Kommerziell (CC-NC)
* **gfdl:** GNU Free Documentation License
* **bsd:** BSD Lizenz
* **dl-de-by-1.0:** Datenlizenz Deutschland Namensnennung
* **official-work:** Amtliches Werk, lizenzfrei nach §5 UrhG
* **other-closed:** Andere eingeschränkte Lizenz

## Von wem stammen die Daten?

Hier die Top-10 Liste der Datenbereitsteller, sortiert nach der Anzahl der bereitgestellten Datensätze.

Aggregiert aus `result.author`.

```
                                   'Statistisches Bundesamt': 729
'Senatorin für Finanzen, Zentrales IT-Management und E-Government': 89
'Hansestadt Rostock – Kataster-, Vermessungs- und Liegenschaftsamt': 34
                                        'Gemeinde Wennigsen': 30
                                               'Stadt Moers': 27
   'Senatsverwaltung für Wirtschaft, Technologie und Frauen': 24
                            'Statistisches Landesamt Bremen': 19
                  'Hansestadt Rostock – Hauptverwaltungsamt': 17
                      'Amt für Statistik Berlin-Brandenburg': 15
             'VBB - Verkehrsverbund Berlin-Brandenburg GmbH': 12
```

# Ressourcen

Ein Datensatz kann mehrere Ressourcen besitzen. Es gibt insgesamt 2551 Ressourcen.

## In welchen Formaten liegen die Daten vor?

Dies ist eine Top-20 Liste der am öftesten verwendeten Formate. Formate sind dabei Ressourcen und nicht Datensätzen  zugeordnet, da ein Datensatz Ressourcen in unterschiedlichen Formaten besitzen kann.

Aggregiert aus `result.resources.format`.

```
       'csv': 957
       'xls': 815
       'xml': 116
      'json': 114
       'wms': 88
       'kml': 83
       'gml': 78
   'geojson': 72
       'pdf': 37
       'txt': 28
      'html': 24
       'kmz': 21
 'shapefile': 19
       'gpx': 18
      'jrss': 13
       'rss': 13
     'gjson': 10
       'shp': 4
       'doc': 3
       'tms': 3
```
