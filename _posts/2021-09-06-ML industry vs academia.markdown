---
comments: true
date: 2021-09-06 21:15:14
layout: post
slug: sketchup
title: Why machine learning in industry is different from that in academia
wordpress_id: 27
tags:
- machine learning
- industry
- academia
---

The last decade has seen a crazy amount of advances in the field of AI. Equally astonishing is the speed with which these advances have made their way into industrial applications. Despite this there aren't a lot of successful AI systems around us.

The performance of a AI system stems from 2 key components: 
1) Algorithmic technique used to build the model. 
2) Dataset used to train the model. 
You change any one of them, the performance of the AI system will change. 

Academicians (owing to their bias for fundamental advances) keep the dataset constant and vary the algorithm. This allows them to compare 2 AI algorithms and establish which one is better seamlessly. Further, in academia, the test set is usually a chunk of the dataset itself. 

This approach doesn't work well in the industry. The industry works on the idea of Minimum Viable Product (MVP). The idea is never to build ‘THE model’ especially in the early days of an AI system. The idea is to build ‘a model’ that is good enough for various stakeholders to realize the value and deliver/estimate this value in the fastest possible manner. Further, the model should be able to do well on the production data and not on some benchmark dataset. 

Also, note that the value is delivered by a system and not just the model. Model is just a small part of it. One needs to answer the following: 
1) Does the AI system solve an important problem? a problem users deeply care about
2) Does the value proposition of AI system fit well within the larger Value proposition of the product? 
3) Does the AI system model and solve the problem (fairly) well? # of mistakes it makes? Is the cost of mistakes ok with your users or its catastrophic? 
4) Does one have the right type, quantity and quality of data to solve the problem at hand? If not, invest heavily in data collection and data plumbing first. 
5) Does the UI/UX deliver the predictions seamlessly and does it handle the mistakes gracefully? Does it allow the user to override a model especially when predictions are going wrong?
6) How well the system does on production data (which is often very different from training data) - drift in data, drift in labels, handle outliers etc 
7) What is the cost of running an AI system? Cost of getting the data labeled continuously to benchmark systems performance?
8) Does the (medium-long term) returns from the AI system >> overall investment in building and maintaining the AI system? [In short-medium most AI efforts are cost negative]

The success of AI system depends on all the above. It is this that makes building AI systems in industry an ‘Art’ unlike the science of building ‘models’ in academia. In industry, the science of model building is necessary but not sufficient. 