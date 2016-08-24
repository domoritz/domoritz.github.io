---
comments: true
date: 2011-04-03 23:13:22
layout: post
title: Asteroids auf beliebiger Website spielen
wordpress_id: 1568
tags:
- Asteroids
- JavaScript
---

Für alle, sie gerne mal eine website zerstören, kann ich dieses kleine Javascript Stückchen empfehlen. Einfach auf einer beliebigen Seite in die URL-Leiste oder die Javascriptkonsole kopieren und bestätigen und los gehts. Viel Spaß.

```js
javascript:var%20s%20=%20document.createElement('script');s.type='text/javascript';document.body.appendChild(s);s.src='http://erkie.github.com/asteroids.min.js';void(0);
```

Dank geht an [Erik Rothoff Andersson](http://erkie.github.com/)
