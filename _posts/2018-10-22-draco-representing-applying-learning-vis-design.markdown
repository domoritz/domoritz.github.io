---
layout: post
title: "Draco: Representing, Applying & Learning Visualization Design Guidelines"
description: Encoding visualization design guidelines as logical constraints so that they can be applied, tested, and learned.
---

*Originally published at [Medium](https://medium.com/@uwdata/draco-representing-applying-learning-visualization-design-guidelines-64ce20287e9d).*

From [academic courses](https://courses.cs.washington.edu/courses/cse512/18sp/) to [online articles](https://blog.datawrapper.de/better-charts/), discussions of visualization often abound with design guidelines: *Don’t use pie charts! Don’t use rainbow color maps! Ensure axes include zero!* When applied in a proper context, such guidelines help prevent misleading visualizations. However, such guidelines are not always well-known, and are themselves subject to debate among practitioners, in part because the “proper context” may not be obvious.

As a result, design guidelines can be challenging to apply, relying on people’s judgment and expertise. What guidelines does my design adhere to? Are there exceptions to the “rules”? For example, we are often told a chart’s axes should include zero, but what if we are using log scales, or using color encodings — are we breaking the rule if not using zero? An additional difficulty is that current guidelines are a bit like folklore: though often grounded in perceptual studies, guidelines are passed down in classes and writings largely as “folk wisdom” rather than concrete, contestable propositions. Furthermore, guidelines may be unfairly written off as “thou shalt not…” proscriptions of purists, rather than serving as resources that directly assist design.

The [**Draco**](https://uwdata.github.io/draco/) project aims to make design guidelines concrete, actionable, and testable. By encoding guidelines as *logical rules*, we can build computational knowledge bases for automatically assessing existing charts and generating new recommended charts. Draco can warn you if your chart violates design rules and provide design suggestions, even for ambiguous requests such as “visualize the horsepower of these cars using a bar chart.” By formalizing design guidelines as constraints, visualization researchers and practitioners can add their own design considerations and directly test the results, seeing how different rules and weightings change which visualizations are considered the most preferable.

In this article, we explain how to encode design guidelines in Draco, how Draco can be adapted quickly to incorporate new rules, and how we use machine learning to learn preference weights among guidelines. More details are available in our [InfoVis 2018 research paper about Draco](https://idl.cs.washington.edu/papers/draco/).

## How Draco Knows How to Create Visualizations

The first ingredient of Draco is a formal language to describe visualizations. Here we use [Vega-Lite](https://vega.github.io/vega-lite/), a high-level language for describing a variety of statistical graphics. With Vega-Lite, one can concisely describe a visualization as a set of encodings that map from data fields to the properties of graphical marks (such as *x*, *y*, *size*, or *color* properties). Vega-Lite includes data transformations such as filtering, sorting, binning, and aggregation along with visual operations including stacked layouts and faceting data into [small multiples](https://en.wikipedia.org/wiki/Small_multiple). By combining these basic building blocks, Vega-Lite users can construct an [expressive range of graphics](https://vega.github.io/vega-lite/examples/).

<figure>
<img src="{{ '/images/posts/draco/bar-chart-facts.avif' | relative_url }}" alt="An example of a bar chart, its Vega-Lite specification (in Vega-Lite JSON), and its equivalent specification using Draco constraints (in ASP)">
<figcaption><em>Figure 1: An example of a bar chart, its Vega-Lite specification (in Vega-Lite JSON), and its equivalent specification using Draco constraints (in ASP). The specification defines the marktype and encodings, which includes a specification of the fields, data type, and data transformations.</em></figcaption>
</figure>

Draco encodes these visualization building blocks as *logical facts*. Figure 1 shows how a Vega-Lite bar chart is expressed as logical facts in Draco. These statements formally describe properties of the input data, the specified visual encodings, and potentially even the user’s task. As we want to *automatically* reason about these logical facts, we express them using the notation of [Answer Set Programming (ASP)](https://en.wikipedia.org/wiki/Answer_set_programming), a standard format for constraint solvers.

The second ingredient of Draco is an encoding of design guidelines, realized as *constraints* over the logical facts. The constraints restrict which facts can appear together and which combinations we might prefer. For example, a constraint might express a preference that if a *bar* mark is used to encode quantitative data, the corresponding axis should include zero.

Draco has three different categories of constraints. First, there are constraints that restrict the domain of attributes to ensure a valid Vega-Lite program. For example, a visualization cannot use *bar* and *point* for the *mark* type at the same time. (Here we restrict ourselves to single charts without layering or composition.) A visualization can also not use an arbitrary undefined mark type such as *wiggly-surface*; we restrict the domain to valid mark types supported by Vega-Lite such as *bar*, *line*, *area*, and *point*. We have similar restrictions for the channel, field, aggregation, and encoding parameters.

Below is the ASP code for specifying restrictions to a mark type. Don’t worry too much about the exact syntax. The *:-* symbol can be read as “it cannot be the case that …”. A comma (*,*) indicates conjunction (logical and).

```prolog
% possible values of mark type
marktype(point;bar;line;area;text;tick;rect).
```

```prolog
% Do not allow the mark to be M when M is not a valid mark type.
:- mark(M), not marktype(M).
```

The second category of constraints limits which logical facts can appear together in a valid visualization specification. As a simple example, we never want two facts of the type *mark*. We can also define more nuanced rules. For example, we can specify that only continuous encodings can be aggregated, or that a bar chart requires an *x* or *y* encoding. Again, as we want to formally reason about the logical facts and constraints, we express them in ASP. Below we restrict the number of *mark* facts to be exactly one.

```prolog
% Allow exactly one mark type.
{ mark(M) : marktype(M) } = 1.
```

To specify that bar charts must use an *x* or *y* encoding, we write a constraint over the *mark* and *channel* facts. An underscore (*_*) indicates that we don’t care about the exact value at this location.

```prolog
% Point, tick, and bar require x or y channel.
:- mark(point;tick;bar), not channel(_,x), not channel(_,y).
```

In summary, constraints limit what logical facts can appear together. We can use them to ensure that the specified visualizations in Draco are valid encodings that we can render using Vega-Lite.

At this point, we might be tempted to start using these constraints to also describe design guidelines. However, if we treat all design guidelines as *hard* (non-negotiable) constraints, we would exclude a number of visualizations that we might want in special cases. For example, consider what would happen if we absolutely forbid quantitative axis scales that do not include zero: any time series of year-over-year values would always have to start at the year zero, we could never use log scales, and many other valid cases would be excluded. Instead of using constraints that *must* be satisfied, we can instead use *soft* constraints. Unlike hard constraints, it is acceptable for soft constraints to be violated. We instead apply a *penalty* (or *cost*) for each soft constraint that is not satisfied, allowing us to express *preferences* (rather than fixed rules) over the space of possible designs.

Here is the ASP code for a general guideline that indicates a preference to include zero within the domain of an axis scale:

```prolog
:~ encoding(E), not zero(E). [1]
```

Notice some changes to the syntax here. The starting segment switched from *:-* to *:~* and we added the number *[1]* at the end. You can read this soft constraint as “We prefer not to have an encoding E that also does not use zero. If we violate this rule, we incur a cost of 1.” Of course, this guideline is overly general, applying to all encodings; so we can use a more specific rule:

```prolog
:~ continuous(E), not zero(E). [1]
```

This rule says that we only want to apply the soft constraint to *continuous* quantitative fields. We then add some hard constraints specifically for log scales and bar or area charts, where not including zero would imply incorrect comparisons.

```prolog
% log and zero cannot be used together.
:- log(E), zero(E).
```

```prolog
% Bar and area marks require continuous scales to start at zero.
:- mark(bar;area), channel(E,x), orientation(horizontal), not zero(E).
:- mark(bar;area), channel(E,y), orientation(vertical), not zero(E).
```

While defining all of these constraints may seem cumbersome, the result is a thorough and formal specification of “design guidelines” that can be applied and tested automatically. As we will see, this opens up a number of benefits!

## Using Draco’s Knowledge Base for Critique and Recommendation

So far we have discussed how we can specify visualizations and design guidelines as facts and constraints over these facts in Draco. The beauty of using constraints is that we can now use existing constraint solvers to find violations and reason about visualization design.

For example, we can translate a Vega-Lite visualization specification into a set of Draco facts. We can then use a constraint solver to check the specification against all design rules and notify the user if the chart violates any particular guideline. We can use the soft constraint weights to determine the severity of any violations. This support is similar to spelling and grammar checkers in word processors, allowing us to automatically alert a visualization creator to potential issues that might hamper accurate chart reading.

<figure>
<img src="{{ '/images/posts/draco/encoding-search.avif' | relative_url }}" alt="Our implementation of the encoding search process using constraints">
<figcaption><em>Figure 2: Our implementation of the encoding search process using constraints. Draco compiles a user query (including the dataset, the partial specification, and the task) into a set of rules and combines them with the existing knowledge base to form an ASP program. Draco then calls Clingo to solve the program to obtain the optimal answer set. Finally, Draco translates the answer set into a Vega-Lite specification.</em></figcaption>
</figure>

Another powerful application of constraints is to help designers create more effective designs in the first place. Instead of asking the user to provide a complete specification, we can use the solver to auto-complete a partial specification, as illustrated in Figure 2. The solver uses the hard constraints to determine the *search space* of all valid visualization specifications, and then uses the soft constraints to find the more preferred encodings within that space: those that accrue the lowest overall penalty (sum of costs). The results can then be presented as a ranked list of charts for the user to examine.

In this way, Draco can serve as a “design assistant” that makes suggestions to the user. The user is then free to use or override the results as they see fit. We have used Draco to re-implement the [CompassQL recommender engine](http://idl.cs.washington.edu/papers/compassql) that powers our [Voyager exploratory visualization interfaces](http://idl.cs.washington.edu/papers/voyager2/). Not only does the Draco implementation require less code (declarative constraints rather than imperative JavaScript code!), the use of a modern, optimized solver means that the resulting system is also immensely more scalable.

## Improving Guideline Preferences via Machine Learning

Draco’s “knowledge” of visualization design is encoded in the hard and soft constraints. While it is comparatively easy for an expert to specify what visualizations are non-sensible and what design rules exist, trading off between potentially competing design rules is much more challenging. Moreover, in general such trade-offs are far from universal: particular domains or organizations may have different conventions or preferences.

<figure>
<img src="{{ '/images/posts/draco/learning-to-rank.avif' | relative_url }}" alt="Overview of Learning-to-Rank in Draco">
<figcaption><em>Figure 3: Overview of Learning-to-Rank in Draco. Given visualization pairs in which one chart is preferable to the other, we learn soft constraint weights that best match the observed pairs.</em></figcaption>
</figure>

The trade-offs between different design guidelines are determined by the weights of the soft constraints. Changes to the soft constraint weights can result in different recommendations from the Draco system. If using Draco for automated visualization design to support data analysis, we want Draco to produce *effective* visualizations that people are more likely to read quickly and accurately. Rather than fine-tuning the costs for all soft constraints by hand, we can determine weights that produce effective encodings by learning from experimental studies of visual encoding effectiveness.

In the Draco paper, we demonstrate this approach by learning soft constraint weights from data gathered from [two](https://idl.cs.washington.edu/papers/task-data-effectiveness) [separate](http://bahadorsaket.com/publication/peng-tvcg.pdf) studies on visualization design. We first build a training dataset of visualization pairs, where the experiment results strongly suggest that one visualization in a pair should be preferred to another. We then apply a *learning-to-rank* approach using a linear [Support Vector Machine](https://en.wikipedia.org/wiki/Support_vector_machine) (SVM), updating the weights until Draco correctly orders as many visualization pairs as possible (Figure 3). On a set of unseen test data, we achieve 96% ranking accuracy. Despite using a linear learning algorithm, Draco can implicitly express non-linear relationships as the soft constraints can be defined over multiple attributes of a visualization. Please see the [Draco paper](http://idl.cs.washington.edu/papers/draco/) and our [vision of using machine learning for visualization design](https://arxiv.org/pdf/1807.06641.pdf) if you are curious about the details!

## The Future of Draco

Though promising, Draco’s visualization language is still admittedly modest, and can only express single charts. We are now working on extending the language to support multi-view graphics and interactive charts. We see our current set of logical facts and constraints as the starting point for an evolving knowledge base that can be refined, extended, and tested by researchers and practitioners. To facilitate this extension, we are first developing tools to browse and experiment with Draco’s knowledge base. We will then go on to build tools to observe and collect user actions in order to continuously learn preference weights and adaptively improve Draco’s suggestions. An important aspect of this work will be to integrate Draco into popular visual analysis tools such as the Python [Altair](https://altair-viz.github.io) bindings for Vega-Lite.

<figure>
<img src="{{ '/images/posts/draco/draco-editor.avif' | relative_url }}" alt="An experimental Draco editor with which users can edit the logical facts that describe a partial query and browse the completions generated by the constraint solver">
<figcaption><em>Figure 4: An experimental Draco editor with which users can edit the logical facts that describe a partial query and browse the completions generated by the constraint solver.</em></figcaption>
</figure>

To get started using Draco, please visit the [Draco project website](https://uwdata.github.io/draco/). From there, you can read our research paper, browse the constraints, inspect our learning-to-rank implementation, and experiment with our [online editor](https://uwdata.github.io/draco-editor/) (Figure 4), where you can try Draco without installing anything.

We are just at the start of exploring and improving Draco’s capabilities, and welcome your thoughts and contributions!

*This article was authored by* [*Dominik Moritz*](https://www.domoritz.de/) *and* [*Jeffrey Heer.*](http://jheer.org/)

*Draco Project Website and Software:* [*https://uwdata.github.io/draco/*](https://uwdata.github.io/draco/)

*Draco InfoVis 2018 Paper:* [*http://idl.cs.washington.edu/papers/draco/*](http://idl.cs.washington.edu/papers/draco/)
