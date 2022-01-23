---
comments: true
date: 2021-09-18 19:25:54
layout: post
slug: making_AI_work
title: Making AI work for you
tags:
- machine learning
- Learnings
- AI Trenches
- making AI work

---

I am often asked why is AI is a hard technology? (both in terms of time and money). There are multiple reasons for it: 

1) Finding the right use case: finding a problem that is important to its users and can be solved well by AI. I talked earlier on this here (https://lnkd.in/eiAYU9eq)

2) Having the right data: most companies have tonnes of data but seldom have the data for the problem at hand. In AI its not just the quantity of data that matters but also the quality of data. Do you have the training data that resembles the production data very closely? Does it have enough data points that represent various outliers, mean data points, data points near the actual decision boundary etc 

3) Labeling cost - If you need to get your data manually labeled, this will need lots of time and money. The process of labeling itself might not be straightforward. How do you benchmark the quality of labeling? If your labelers are making mistakes this can jeopardize the entire project.  

4) Compute cost - the cost of the compute needed for training the model and for inference. This is especially crucial if your solution uses deep learning. 

5) Going from a solution to the solution: In AI there is no one way to solve a problem. There are multiple ways and each will give you a different accuracy. Getting from the point where you have a model that gives you an acceptable performance to getting to a model that gives you fabulous performance is often a very long journey.

6) Fitting model into the product to get AI-driven feature: Its not just a simple API integration. One needs to figure out the best UX to serve the predictions, should this UX be intrusive or soft suggestions, UX should be able to gracefully handle the scenarios when the model makes mistakes, a mechanism to let the human take over when it is going all wrong for the end-user, instrumentation to collect data to continuously evaluate the performance of the model on prod data, instrumentation to collect data for future modeling efforts. 

7) Need to retrain model: many times AI systems require one to retrain the model after every 15-30 days on the latest data. 

8) Talent: DS/ML team alone cannot pull off all the above. You need good and diverse talent for this - ML/DS folks who can evaluate the various approaches depending on the situation and can take the most suitable one to build the right model (and not blindly apply DL), Data engineers to build data pipelines to collect all data, a product manager who can figure out right use case, build instrumentation, UX to handle mistakes, a AI leader who understands this entire life cycle and work very closely with business and speak their language. This talent doesn't come cheap.

For AI effort to fail - going wrong on just one of the above is enough. 
