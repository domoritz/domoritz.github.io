---
comments: true
date: 2021-08-20 10:05:24
layout: post
slug: UseCases
title: Hobbiton - Uses cases where AI can deliver great returns
tags:
- machine learning
- uses cases
- returns
---

One often comes across organizations trying to apply AI to problems when it is really not needed. Such organizations often end up doing so because either someone in the org wants to look cool or a CXO in the company wants to start doing AI (mostly out of FOMO or ill-informed media articles with lofty claims). AI is just a tool to solve problems (though a powerful one), just like other problem-solving tools such as engineering, or operations. Today AI can solve some problems quickly & very well which was not possible until even a decade ago. But that doesn’t mean AI is a sledgehammer for every difficult problem. Despite crazy advances in the last decade, AI is a very nascent, fragile and expensive technology and must be applied after due thought and not as a go-to approach for every problem in the world.

One of my favorite examples of this is Google's approach to “searching for special characters in Google Docs”. Here is the problem statement: Most users who create docs or decks once in a while use special characters. But it is very hard to find the right special character when you need it. Given the large number of special characters that exist, one cannot show all of them to the user. To facilitate quick accessibility, one requires the ability to search for them. However, there is one particular problem with special characters - most users cannot remember them by name (try recalling names of 10 or more special characters yourself). This renders “textual search” useless. So, how does one solve this? Visual search!


<picture>
<img src="{{ 'images/Google-Doc-Draw-Characters.gif' | relative_url }}" width="500" alt="Special Characters Search in Google Docs" align="center">
</picture>


Google used a very simple but powerful observation - most users can very easily recall how the special character that they need looks like, unlike their name. So, they provided a small sketch pad for users to draw what they remember and use the concepts from computer vision (Sketch-RNN) to suggest a few closest options based on the visual match. The same concept was later used to power Auto draw [https://experiments.withgoogle.com/autodraw]

I often use this example to drive home the point that one often needs to think from first principles when thinking of AI-powered use cases. For the above-mentioned example, the more you think the more you will realize:

- The problem could not have been solved by traditional engineering approaches. 
- It is a very well-defined narrow problem statement.
- The core AI concept (Sketch-RNN) was just right to solve this problem statement well.
- The solution (powered by AI in this case) really helped to solve the user’s pain point and deliver happiness.

Having said that - it is not that this application of AI changed the fate of google docs. More on changing the trajectory of products using AI in a separate post. Stay tuned!