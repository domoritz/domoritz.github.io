---
layout: post
title: "Paper discussions on Bluesky at VIS 2026"
description: How VIS 2026 puts a Bluesky thread under every paper.
---

Every paper page at [IEEE VIS 2026](https://ieeevis.org/year/2026/) has a discussion under the abstract, and that discussion is a thread on [Bluesky](https://bsky.app) (or more correctly, on the [AT Protocol](https://atproto.com)). Anyone can read it on the page, and attendees can comment and like there too, whether or not they have a Bluesky account. I am on the organizing committee as part of the tech team, and I built the pieces behind this feature. This post explains why we are trying this at VIS and how it works. I hope that other conferences can learn from this writeup and get inspired to do something similar.

<figure>
<div class="flex-rows">
<figure><img src="{{ '/images/posts/vis-bluesky/discussion-embed.avif' | relative_url }}" alt="The discussion section of a paper page: the announcement post from @papers.ieeevis.org, a link to join the discussion on Bluesky, a sort toggle for most liked or newest, and replies from attendees with like counts"></figure>
<figure><img src="{{ '/images/posts/vis-bluesky/announcement-post.avif' | relative_url }}" alt="The same thread in the Bluesky app: the announcement post from IEEE VIS Papers with an author mention, the session time in three time zones, and a link to the paper page, followed by replies from a Bluesky user and from the IEEE VIS Discuss account"></figure>
</div>
<figcaption markdown="span">A dry-run thread on the paper page (left) and in the Bluesky app (right). Comments made on the page appear on Bluesky as replies from [@discuss.ieeevis.org](https://bsky.app/profile/discuss.ieeevis.org), prefixed with the commenter's name or pseudonym.</figcaption>
</figure>

## Why do we host conference discussions on Bluesky?

VIS this year is hybrid, spread across the main conference in Boston and [satellite locations in Paris and Tianjin](https://ieeevis.org/year/2026/satellites/). Not all discussions can happen in person, so we want a place where attendees can discuss asynchronously online. Another motivation is that traditional Q&A isn't working as well anymore. Sessions are so packed that the time for questions has shrunk to a few minutes (at best). Questions get cut off, answers can be rushed, and whatever exchange happened disappears after the conference. A discussion that is tied to the paper gives authors time to think about an answer. Answering on the spot is hard, especially for those with less practice in public speaking. Moreover, persistent discussions online can continue after the conference ends.

Instead of rolling our own commenting system (and running the infrastructure for it), I chose Bluesky because it is built on the [AT Protocol](https://atproto.com). The AT Protocol is open and federated: anyone can run a server that stores accounts and posts, and the servers talk to each other. Bluesky provides a lot of infrastructure that would be hard to replicate. They offer reliable storage, robust protocols/APIs, integrations, moderation, and native apps. Existing accounts and apps matter for discussions. For example, an author who is mentioned in an announcement sees the discussion in the notifications of the app they already use. And lastly, because anyone can build on the protocol, the conference can add its own pieces on top of it.

The other reason is the community. For years, "Vis Twitter" was where the visualization community hung out between conferences. Researchers and practitioners discussed charts, shared papers, and followed the VIS conference from afar. When Twitter started to be run by a fascist, people left, and some migrated to Mastodon, but Mastodon never felt the same. Recently, some of the community has moved to Bluesky, and I would like to help bring us back together there. The VIS conference is a good moment for that: for one week there are many new papers to discuss, and an online discussion includes both the people at the conference and the broader visualization community.

## Design goals and constraints

A few goals and constraints shaped most of the design. Other conferences probably face similar constraints, so the system could be a model for them.

**Running infrastructure is a big lift for conferences.** VIS keeps its setup simple, for example with a [website without dynamic content](https://github.com/ieee-vgtc/ieeevis.org). Comments are dynamic, so they have to live on some other server. Running and maintaining one ourselves is more work than we want to take on, so building on an existing system like Bluesky makes sense.

**The website is static and built before any post exists.** A page cannot know the URL of its own post. So each page carries only its paper id, and a small service resolves that id to the announcement when the page loads. Nothing needs a rebuild when a thread appears or is deleted. After the conference, the plan is to bake the mapping into the pages and let them read Bluesky directly, so that the service can be switched off. The conference then has nothing left to run or maintain.

**Nobody should need a Bluesky account, but a thread should still feel like a conversation between people.** Not everyone has a Bluesky account, and we cannot expect everyone to create one, but they should still be able to participate fully. Attendees without an account comment through a guest bridge, which is gated by the conference login. A bot account posts their comments to Bluesky. These comments show the attendee's real name by default, so the thread reads like a conversation between people. Attendees can hide their name behind a pseudonym, but the organizers always know who wrote what.

**Authors should get notified of replies.** The announcement mentions every author whose Bluesky handle the conference knows, so that they get a notification. Authors are attendees too, and they can add their handle to their conference profile. The paper announcement goes out shortly before the session.

**Moderation should be standard, attributable, and reversible.** Moderation is super important for conferences and Bluesky's own moderation labels provide a scalable approach. Beyond the [existing moderation](https://bsky.social/about/blog/03-12-2024-stackable-moderation), organizers can take two actions: hiding a reply posted on Bluesky and deleting a comment posted via the bot account. Hiding is reversible, and every action is logged with who took it. Attendees can remove their own comments, but the organizers keep the text in their log, so removing is not a way to make something harmful disappear before anyone has seen it.

**One person and part time.** As a tech chair, I help run the conference systems. The discussion service came on top of that and my two other jobs, so I built it in my free time and had to keep things simple. We wanted to run everything on the existing infrastructure. VIS keeps its conference database in a self-hosted [Supabase](https://supabase.com), so the discussion service runs on that same server as a few small functions and tables, in the way the tech team already does things. Attendees can only post for about a week, so we keep the protection against abuse simple: a sign-in with the conference account, a limit on how often one person can post, and a date about a week after the conference when guest posting closes, because nobody watches the discussion account after that. Reading continues to work, and anyone with a Bluesky account can keep replying on Bluesky.

All in all it took me 40 to 50 hours over six weeks to design and build the system described here. A coding agent wrote a lot of the code. Without it I could not have done this next to my day jobs. Anyone who copies this system should have an easier time, because the design is done.

## How the Bluesky posting service works

I was inspired by [a blog post by Emily Liu](https://emilyliu.me/blog/comments), who uses Bluesky threads as the comment section of her blog: put the URL of a post in the page, fetch its replies from the public API, and render them. To make this idea work for VIS, we need something that announces each paper at the right time, something that maps paper ids to posts (for the reason explained above), and a way for attendees to comment without an account. We implement a service for each of these: an announce bot, a read proxy, and a guest bridge. The website itself has code to render the discussion and to log in with Bluesky.

Besides the services, we also need accounts on Bluesky. VIS has three: the official one, [@ieeevis.org](https://bsky.app/profile/ieeevis.org), is run by people and stays that way (we don't need it for this system). A papers account, [@papers.ieeevis.org](https://bsky.app/profile/papers.ieeevis.org), is used by a bot to announce every paper, and each announcement is the root of that paper's discussion. A discussion account, [@discuss.ieeevis.org](https://bsky.app/profile/discuss.ieeevis.org), relays comments from attendees who have no Bluesky account. I call those guest comments below. An attendee who does have a Bluesky account posts as themselves, either by logging in on the paper page or by replying in the Bluesky app/website. Organizers monitor and moderate the threads from a dashboard (which we also use to monitor other aspects of the conference system).

<figure>
<img src="{{ '/images/posts/vis-bluesky/architecture.svg' | relative_url }}" alt="Architecture diagram with three columns. The conference website has a paper page that knows only its paper id and a conference login that provides a token. The discussion service has a program database feeding an announce bot, a read proxy that maps a paper id to its thread, and a guest bridge for comments and likes. Bluesky holds the @papers.ieeevis.org account for announcements, the @discuss.ieeevis.org account for guest comments, and readers' own accounts, which they can log in with from the page.">
<figcaption>The pieces and how they talk to each other.</figcaption>
</figure>

The **announce bot** checks the program every five minutes. Shortly before a session, it posts one announcement per paper from the papers account: title, authors, hashtag, and a link to the paper page, with the authors mentioned wherever their handles are known. The bot can announce other events as well. At VIS, panels, the keynote, and the capstone get announcements too.

The **read proxy** relays requests from the VIS website to the Bluesky API. When a page loads, it asks for the thread that belongs to its paper id. The proxy keeps the mapping from paper id to announcement [post id](https://atproto.com/specs/did), fetches the thread from Bluesky, caches it for a few seconds, and returns it in a simple format for the page. Before the bot has posted, the page says that the discussion opens shortly before the session.

Attendees with a Bluesky account do not need a bridge. They can log in with their account on the page and post from it (the login asks only for permission to post and like, nothing else), or reply in the Bluesky app, which is the better experience on a phone. Posting from their own account is better: the reply is theirs, shows their profile, and their followers see it. When an attendee logs in on the page, the site offers to save their handle to their conference profile, so that later announcements can mention them.

The **guest bridge** is for attendees without a Bluesky account. They sign in with their conference account instead (we require login so that only attendees can use the bridge). The sign-in requires a small service on the website server that can authorize requests to the guest bridge. The bridge posts the comment from the discussion account, signed with the attendee's name, or with a pseudonym if they tick "Hide my name" for that comment. Either way it is an ordinary reply on Bluesky, and both kinds appear in the same thread.

A shared Bluesky account can like a post only once, so guest likes cannot be stored on Bluesky. The bridge stores them itself, one per attendee per reply, and the read proxy adds them to the count from Bluesky, so a reply shows a single number wherever its likes came from.

Likes also help with the Q&A. VIS used to collect questions on Slido, where attendees upvote the ones they want asked. The discussion can take the place of Slido: replies can be sorted by most liked as well as by newest, and a session chair can pick the top questions from the thread. A small easter egg: the like button is a donut, which also appears in the VIS 2026 logo. This kind of whimsical detail is only possible because we render the discussion ourselves on the website.

Moderation is critical and mainly happens in the organizer dashboard. Bluesky's labels filter spam and abuse before a reply ever reaches the page. For everything else, an organizer can hide a reply, delete a guest comment, or look up who wrote an anonymous one. A student volunteer with no Bluesky experience can do all of this with a short guide.

Once the conference is over, the middle column in the architecture diagram above goes away. The post URLs get baked into the pages, the pages read Bluesky directly, and logging in on the page is switched off as well. The threads stay open on Bluesky, so anyone can keep replying there.

<figure>
<img src="{{ '/images/posts/vis-bluesky/architecture-after.svg' | relative_url }}" alt="Diagram of the setup after the conference: the paper page now knows the URL of its post and reads the thread from Bluesky directly, attendees keep replying from their own accounts in the Bluesky app, and the discussion service in the middle is switched off.">
<figcaption>After the conference. The discussions stay visible on the website and can continue on Bluesky, and the organizers have no service left to maintain.</figcaption>
</figure>

## An experiment

VIS is trying this for the first time in 2026, and we do not know whether people will use it. Will people ask questions on the paper pages, will authors answer, and will threads keep going after the conference? People are [glad to see VIS on Bluesky](https://bsky.app/profile/chezvoila.com/post/3mvnakgshxk2d) already. I will share what I learn and hope we continue this experiment in future years. Also, nothing here is specific to VIS. Any conference with a program database and a website can announce its papers and embed the threads, and I am happy to help others try.

Lastly, building this system was a team effort. The general chairs backed the experiment, the tech team opened their server and program database to it and helped with implementation, and the web team reviewed and merged the changes to the site. Thanks to everyone who is supporting this experiment, and I hope it leads to more persistent and engaging discussions at VIS and beyond.
