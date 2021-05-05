---
layout: post
title: How fast is fast enough?
description: Rule of thumb for latency in interactive visualization.
---

To support effective exploration, visualization systems need to be fast. Liu and Heer showed [in their paper](https://idl.cs.washington.edu/papers/latency/) that an additional latency of 500ms negatively affects the user's behavior. They even found that the negative effects continue even after the delay is removed. Unfortunately, some system designers misunderstood the 500ms as a threshold that should be met. However, the paper only talks about the difference of low vs high latency and the goal should be low-latency.

The paper also found that some interactions are more latency sensitive than others. For example, zooming is not as latency sensitive as panning. Sending a query through a form [should return results quickly](https://services.google.com/fh/files/blogs/google_delayexp.pdf) but 60fps (16ms) is probably not quite necessary. So when you are designing a system, what latency should you aim for? Until we have further evidence for particular thresholds, we could use a guideline.

As a rule of thumb, I am proposing that we require that **latency should be lower than the shortest time between any two user queries**. This rule is motivated by the fact that responses arrive before the user can send the next query. As an extreme example, in [crossfiltering](https://vega.github.io/vega/examples/crossfilter-flights/) every movement of the brush fires a new query and delayed responses would display outdated information.

I think this rule could provide a reasonable upper bound but not necessarily a lower bound. For example, just because it takes me a ten seconds to write a search query on Google, I would not want to wait ten seconds.
