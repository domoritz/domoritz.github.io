---
layout: post
title: "Bluesky discussions at VIS 2026: a retrospective"
description: What worked, what did not, and what it takes to build a conference community online.
---

Now that I made it back to Pittsburgh after some delay because of the [nationwide ground stop in the United States](https://en.wikipedia.org/wiki/2026_FAA_nationwide_ground_stop), I wanted to reflect on how the discussions went during the [IEEE VIS 2026](https://ieeevis.org/year/2026/) conference.
For context, this is a follow-up to [my earlier blog post]({% post_url 2026-09-16-vis-bluesky-discussions %}) on why and how we built the integration---I recommend reading it first.

Judging by the number of posts, I think the Bluesky integration for VIS can be considered a success. John Guerra [collected and visualized some statistics](https://johnguerra.co/viz/influentials/ieeevis2026/recap.html), and I recommend that you check it out to explore the data. His analysis counts more than a thousand posts related to the conference, including almost 400 questions. The Q&A alone had 560 posts: 223 questions asked on Bluesky, 175 asked through the conference website, and 162 answers. Many people with Bluesky accounts posted from them directly, but more than a third of the replies in the paper threads came through our guest bridge from attendees without an account. In total, 177 people posted, and their posts got more than 2,700 likes and almost 300 reposts. After the conference, there are now more than 1,500 people in the community around IEEE VIS. It was amazing to see how many people created new accounts specifically for this conference and are now engaging in conversations online. While we are still learning as a community how we want to use the discussions, more than 40% of the paper threads had some discussion, and the [busiest paper discussion](https://bsky.app/profile/papers.ieeevis.org/post/3mzzwmo4bfx2j) has 19 replies.

If you have any thoughts or additions about this post, please let me know in [this Bluesky discussion](TODO: link the post that announces this blog post).

<figure>
<img src="{{ '/images/posts/vis-bluesky/recap.avif' | relative_url }}" alt="John Guerra's recap of the VIS 2026 conversation on Bluesky. A scatter plot from Sunday, November 8 to Sunday, November 15 places every post by time and likes, with arrows from replies to the posts they answer and dense clusters during the conference days. Summary tiles: 1,122 posts and questions (724 posts and 398 questions), a Q&A of 560 with 223 questions on Bluesky, 175 website questions and 162 answers, 177 people posted, 153 talks with questions, 1,578 in the community, 2,706 likes, 287 reposts and 75 quotes.">
<figcaption markdown="span">[John Guerra's recap](https://johnguerra.co/viz/influentials/ieeevis2026/recap.html) of the conference on Bluesky. Every dot is a post, placed by time and likes.</figcaption>
</figure>

## The rocky start: our posting account got suspended during the keynote

<figure class="right third">
<img src="{{ '/images/posts/vis-bluesky/suspended.avif' | relative_url }}" alt="Bluesky screen reading: Your account has been suspended. Your account was found to be in violation of the Bluesky Social Terms of Service. You have been sent an email outlining the specific violation and suspension period, if applicable. You can appeal this decision if you believe it was made in error. Buttons for Appeal Suspension and Sign Out.">
<figcaption>What I saw when I checked the posting account during the keynote.</figcaption>
</figure>

It all went great in the end, but we had a rocky start, which luckily most people didn't notice. On Tuesday morning, the main conference started with the welcome and the keynote, and during that time our posting service posted the announcements for the papers in the first sessions. As a reminder, we need one Bluesky post for each paper, and we embed the discussion under that post on the VIS website. During the keynote, I was checking the discussions to see whether everything worked and noticed that our posting account was suspended. This meant that the announcements were hidden and new threads could not be posted. I suspect that our account was flagged as a bot because it posted 24 posts in about 10 seconds---which admittedly is suspicious. I was getting nervous at this point, because having no discussions at the beginning would have set a bad precedent for the conference and probably made the experience much worse. I immediately appealed the suspension and was lucky to be able to [reach out](https://bsky.app/profile/domoritz.de/post/3mzxnum7fds2c) to [Jim Ray](https://bsky.app/profile/jimray.bsky.team) from Bluesky Developer Relations. They unsuspended the account within 15 minutes. The suspension came from an automated system, and Jim put a 90-day flag on our account so the bots wouldn't take it down again. Posting during the rest of the conference went smoothly, even with bursts of more than 30 posts. So a big shout-out to Jim and Bluesky for unlocking the account within minutes!

As a takeaway for other conferences and for us in the future, I recommend contacting Bluesky before the conference so they can mark the bot account as trusted. I also recommend monitoring the announcements and the health of the accounts, so that you can detect when anything goes wrong. Monitoring and observability are probably a good idea for any kind of service running during a conference.

## What people said about the Bluesky integration

People had a lot to say about the discussions, some in person and some on Bluesky itself. Here are the main themes.

### It brought back the "Vis Twitter" backchannel

Besides a persistent space for paper discussions, a goal of using Bluesky was to bring back the online community we had during the Twitter days. Building a community takes longer than one conference, but the early sentiment is very positive. Arvind called it [rebuilding "the conference back channel/lurking and data vis Twitter community of yore"](https://bsky.app/profile/arvindsatya.com/post/3n27jccyzkc24), and others noticed [a lot of appetite to recreate the online community of the Twitter days](https://bsky.app/profile/chezvoila.com/post/3n25dcv2olk2l), were [crazy to see so much vis content on Bluesky](https://bsky.app/profile/dvdkouril.xyz/post/3n22rn7vw5s2k), and [loved how active #ieeevis was this year](https://bsky.app/profile/frank.computer/post/3n2hne7mgtk2s). Patrick Stotz even sees [hope for a lively #dataviz community beyond Twitter and LinkedIn](https://bsky.app/profile/patrickstotz.bsky.social/post/3n2bgvr4jdc2o).

### The Q&A integration was well received, and had benefits over mic-only Q&A

Lane Harrison was [loving the Bluesky Q&A integration](https://bsky.app/profile/laneh.bsky.social/post/3mzxucdv2vc24): "Good for sessions, good for post-talk discussion and connection, too." Threads made room for things that don't fit into a few minutes at the mic. Tamara had [more of a comment than a question, "which is legit on Bluesky"](https://bsky.app/profile/munzner.bsky.social/post/3mzybq3wjmk2s). Danielle Szafir [followed up on a hallway chat](https://bsky.app/profile/danielle-szafir.bsky.social/post/3mzyfqvgety2q) after a talk, and people pointed to [related work](https://bsky.app/profile/ptbremer.bsky.social/post/3n226es3guq27) and [materials](https://bsky.app/profile/alark.bsky.social/post/3n25deto6vc2m). Authors also got time to think about their answers, as I had hoped in my first post. For example, Jean-Daniel Fekete answered every question on [ProgressiVis](https://bsky.app/profile/papers.ieeevis.org/post/3mzzwmo4bfx2j), including one with [a reference to Knuth](https://bsky.app/profile/jdfekete.bsky.social/post/3n22c3zenlc2k).

### Value for people who were not there

VIS this year was spread across Boston, Paris, and Tianjin, and the threads connected the locations. Arvind called it ["an actual globally federated conference"](https://bsky.app/profile/arvindsatya.com/post/3mzxqro4syk2r), and Jason Dykes reported ["a huge cheer at the end from 3 continents"](https://bsky.app/profile/discuss.ieeevis.org/post/3n2263yncdk22) for ProgressiVis. People who could not come at all followed along. Andy Kirk, as a "pre-occupied-with-other-stuff bystander", called it [a great success, and of value to us bystanders](https://bsky.app/profile/visualisingdata.com/post/3n27emf3q4k2x), and others [missed how Twitter used to be a back channel during VIS](https://bsky.app/profile/cybunk.bsky.social/post/3n27tu3tevk2k) but were happy to see it on Bluesky.

The discussions also reached beyond the research community. Chez Voila wrote that [leaving a trace online signals "to the larger dataviz community, beyond IEEEVIS, that there is a commitment"](https://bsky.app/profile/chezvoila.com/post/3n27dnh45zk2a). After a week of following the papers on Bluesky, Chez Voila [asked how practitioners and researchers can work together](https://bsky.app/profile/chezvoila.com/post/3n2cfkcvxn22j), which started a thread that went on for days after the conference.

### Session chairs are critical for making discussions work

Discussions worked best when someone actively ran them. Jason Dykes chaired a session and posted a prompt in each paper thread: ["here's your chance to engage in lively academic debate … and VOTE for your favourites! (then I get to ask them) (no need to be on BlueSky)"](https://bsky.app/profile/discuss.ieeevis.org/post/3n222cvl33o23). The seven papers in his session averaged more than ten replies each. The other paper threads averaged just over one, and more than half had none.

The same goes for authors. Some answered every question, like Jean-Daniel Fekete on ProgressiVis or the [HiLSVA](https://bsky.app/profile/kuangshiai.bsky.social/post/3mzxshiqzm223) authors, and some [came back days later](https://bsky.app/profile/arvindcheenu.bsky.social/post/3n276yqih5a2z). But in about three quarters of the paper threads with questions, I could not find an answer from the authors.

### Bluesky as a platform for discussion rocks

Building on Bluesky meant we didn't have to run a discussion platform ourselves and got moderation, scalability, and apps for free. The open API made it easy to integrate the discussions into the conference website and our conference management tools. It also made it easy for others to build on top. John Guerra built [rankings](https://bsky.app/profile/johnguerra.bsky.social/post/3mzymezalcs2u), [starter packs](https://bsky.app/profile/johnguerra.bsky.social/post/3n27emxrrss2a), a [paper navigator](https://bsky.app/profile/johnguerra.bsky.social/post/3n22bec6jhs25), and the recap above. Rahat Zaman read my first post and [added Bluesky discussions to their own publication pages](https://bsky.app/profile/rahatzaman.bsky.social/post/3mzsxgncky22w). None of this needed the organizers.

## Conclusion

Looking back at the design decisions from [my earlier post]({% post_url 2026-09-16-vis-bluesky-discussions %}), I think most of them held up. Building on Bluesky instead of rolling our own system worked, and now that the conference is over, we can turn off our posting and guest services and embed the Bluesky discussions directly. Letting people post without a Bluesky account worked too: 37% of the replies came through the guest bridge from 92 people, including session chairs who used it to run their sessions. Comments showed real names by default, with pseudonyms as an option, and both were used. Two thirds of guest comments were under real names, so the threads read like conversations between people. We had no issues with harassment. We were prepared with a moderation dashboard that let our student volunteers and ombuds hide or take down comments and de-anonymize people, but none of it was needed. Our community is awesome! Mentioning authors so they get notified also worked well in general, although many paper threads had no discussion, which is something to reflect on for future conferences. Finally, likes (or 🍩s, since we were in Boston) sorted the comments, and some session chairs, like Jason, explicitly asked the most liked questions. The [town hall](https://bsky.app/profile/papers.ieeevis.org/post/3n24ssxunck2q) is a good example: attendees posted and liked questions about the satellite model, the conference location, and [anonymous reviewing](https://bsky.app/profile/discuss.ieeevis.org/post/3n24x7c4n2t2q), many under pseudonyms, and the most liked ones rose to the top. The [panel discussion in the VISions session](https://bsky.app/profile/papers.ieeevis.org/post/3n22o3l22wj2v) collected 18 questions, more than any other thread, many of them longer reflections on friction, craft, and AI. So Bluesky can be a reasonable replacement for tools like Slido that let audiences ask and vote on questions.

Overall, I think the Bluesky integration worked well for VIS, but the work is not done. Building a community takes time and care. We need to establish practices over the years so that people learn, for example, how to chair a session or how to use the discussions in a workshop or panel. For the paper discussions, both authors and attendees need to see the value. This is a chicken-and-egg problem: authors need to answer questions so that attendees see value in asking, and attendees need to ask so that authors see value in answering. The threads where both were engaged were amazing to see.

Bluesky and [Cluster](https://cluster-practitioners-summit.github.io/) were both experiments at VIS this year, and both reached beyond the research community. We will discuss with the organizing committee for 2027 which parts to continue, reduce, or expand. Thanks to everyone who made this experiment a success: the web and tech teams who worked closely together to make the integration work, the session chairs, Jim Ray and Bluesky for the quick unsuspension, John for the analysis, and the amazing community of attendees, authors, and others on Bluesky who discussed papers, research, practice, and grounded airplanes.

# Raw notes

## Opening numbers

- From [John Guerra's recap](https://johnguerra.co/viz/influentials/ieeevis2026/recap.html) (Nov 8 to 15, as of Nov 18):
  - 1,122 posts and questions: 724 posts plus 398 questions.
  - Q&A: 560 posts. 223 questions asked on Bluesky, 175 asked on the website, and 162 answers.
  - 177 people posted. 153 talks got questions.
  - 2,706 likes, 287 reposts and 75 quotes.
  - 1,578 people in the community: accounts that posted, asked or answered in the Q&A, liked or reposted conference posts, or follow @ieeevis.org. Most of them only follow.
  - Hashtag use: 332 posts with #ieeevis, 230 without.
- The announce bot posted 352 threads from Nov 9 to 13: 300 papers, plus workshops (14), tutorials (12), panels (9), meetups (9), challenges (3), the town hall, keynote and capstone.
- 573 replies in those threads (as of Nov 18).
  - 362 from 98 people posting from their own Bluesky accounts.
  - 211 from attendees without an account, through the guest bridge ([`@discuss.ieeevis.org`](https://bsky.app/profile/discuss.ieeevis.org)): 92 distinct senders, and a third of the comments (67) under a pseudonym.
- 129 of 300 paper threads (43%) got at least one reply. Busiest: [ProgressiVis](https://bsky.app/profile/papers.ieeevis.org/post/3mzzwmo4bfx2j) (19, Best Paper), the [town hall](https://bsky.app/profile/papers.ieeevis.org/post/3n24ssxunck2q), and two panels (20 and 18).
- Authors answered in at least 32 of the 127 paper threads that had questions (about 25%). This is a lower bound, because I can only detect authors whose handles we knew or who signed with their name. When authors did answer, the median first answer came about 40 minutes after the first question.
- Visual analysis: [John Guerra's recap](https://johnguerra.co/viz/influentials/ieeevis2026/recap.html), which also compares 2026 with VIS on Twitter from 2015 to 2022.


## The rocky start: our posting account got suspended during the keynote

- What happened, with the timeline from Bluesky timestamps:
  - 9:15 am Tuesday: the bot posted the announcements for the first paper sessions. That was 24 posts within about ten seconds (22 papers, a panel and a tutorial).
  - During the keynote you noticed that `@papers.ieeevis.org` was suspended (screenshot: "Your account has been suspended"). Announcements were hidden, and new threads could not be posted.
  - 9:33: you appealed, and you [asked Bluesky for help publicly](https://bsky.app/profile/domoritz.de/post/3mzxnum7fds2c).
  - 9:35: Jim Ray (Bluesky dev rel) [saw it](https://bsky.app/profile/jimray.bsky.team/post/3mzxnylqab22e).
  - 9:48: the account was back up ([your thanks](https://bsky.app/profile/domoritz.de/post/3mzxoqsdqhc23)). Jim: ["sorry about that was taken down by an automod. We flagged so it should stay up now."](https://bsky.app/profile/jimray.bsky.team/post/3mzxoxj6ll22e) So about 15 minutes from asking to fixed, and about 35 minutes after the burst.
- The likely cause: an automated account posting a burst of almost identical posts (same template, hashtag and link) looks like spam to automatic bot detection.
- After Bluesky flagged the account, much larger bursts went through without problems: 29 to 35 posts at once several times later in the week (for example 35 at 7:15 am Thursday).
- Why this mattered: without the quick fix, the first sessions would have had no discussions. Habits form in the first hours of a conference. If the feature had been broken at the start, people might not have gotten into the flow of using it at all.
- Thank Jim and Bluesky for unlocking the account within minutes. Jim also said: ["Can't wait for the write up 😉"](https://bsky.app/profile/jimray.bsky.team/post/3mzxr7e5qyc23).
- Lessons for other conferences:
  - Contact Bluesky before the conference so they can mark the bot account as trusted.
  - Spread out the announcements, for example a few seconds between posts or one session at a time.
  - Monitor that the account is healthy, not only that posting succeeds.
  - This is the flip side of building on someone else's platform (see the design decisions below): you inherit their moderation, and that includes false positives.

## What people said (themes from Bluesky)

**1. It brought back the "Vis Twitter" backchannel. This came up most often.**
- Andy Kirk, as a "pre-occupied-with-other-stuff bystander": [a great success, and of value to us bystanders](https://bsky.app/profile/visualisingdata.com/post/3n27emf3q4k2x).
- Arvind: ["Rebuilding the conference back channel/lurking and data vis Twitter community of yore"](https://bsky.app/profile/arvindsatya.com/post/3n27jccyzkc24). John Guerra in the same thread: [wants the great #infovis conversations back](https://bsky.app/profile/johnguerra.bsky.social/post/3n27etc7a522a).
- Chez Voila: ["a lot of appetite to recreate the online community of the Twitter days"](https://bsky.app/profile/chezvoila.com/post/3n25dcv2olk2l).
- ["crazy to see so much vis content on bluesky"](https://bsky.app/profile/dvdkouril.xyz/post/3n22rn7vw5s2k), and ["I wasn't even part of the conference, but loved to see more #dataviz conversations happening here"](https://bsky.app/profile/t.datarocks.co.nz/post/3n27icm4z4s2f).
- [cybunk](https://bsky.app/profile/cybunk.bsky.social/post/3n27tu3tevk2k), not at VIS this year: "I am so happy to see bsky is being used during #ieeevis. I miss how Twitter used to be a back channel during VIS."
- Frank Elavsky, after the conference: ["LOVE how active #ieeevis was this year on bluesky!"](https://bsky.app/profile/frank.computer/post/3n2hne7mgtk2s) (20 likes).
- Patrick Stotz: ["Great to see a lot of … #IEEEVIS content on Bluesky along with many new faces. Maybe there is hope for a lively #dataviz community beyond Twitter and LinkedIn. Let's give it another shot."](https://bsky.app/profile/patrickstotz.bsky.social/post/3n2bgvr4jdc2o)
- Miska Knapek, from outside the conference: ["Good work by participants publicizing it on blue sky and @johnguerra.bsky.social visualizing the interactions here"](https://bsky.app/profile/miskaknapek.bsky.social/post/3n27fu4jcls2z).
- Tamara pointed out a difference from Twitter: [she now writes alt text for every image](https://bsky.app/profile/munzner.bsky.social/post/3mzvdru25zk2p). That needs a laptop, but it makes her engage more deeply.
- → First post: "I would like to help bring us back together there." This is the goal that was hit most clearly.

**2. Value for people who were not there.**
- Remote people followed along: [Helena Jambor](https://bsky.app/profile/helenajambor.bsky.social/post/3n22veykh5s2k) ("i am not at VIS, sadly"), [Alberto Cairo](https://bsky.app/profile/albertocairo.com/post/3mzxs4uqdxk2b), [Andy Kirk](https://bsky.app/profile/visualisingdata.com/post/3n27emf3q4k2x), and [cybunk](https://bsky.app/profile/cybunk.bsky.social/post/3n27tu3tevk2k) ("the FOMO of not being at VIS this year").
- Hybrid across Boston, Paris and Tianjin. Arvind: ["an actual globally federated conference … And Q&A on Bluesky"](https://bsky.app/profile/arvindsatya.com/post/3mzxqro4syk2r). Jason Dykes in the ProgressiVis thread: ["a huge cheer at the end from 3 continents"](https://bsky.app/profile/discuss.ieeevis.org/post/3n2263yncdk22).
- → First post: the hybrid setup was the first motivation ("Not all discussions can happen in person").

**3. The Q&A integration was well received, and threads did things a mic queue cannot.**
- Lane Harrison: ["Loving the BlueSky Q&A integration … Good for sessions, good for post-talk discussion and connection, too"](https://bsky.app/profile/laneh.bsky.social/post/3mzxucdv2vc24).
- Comments instead of questions. Tamara: ["I have more of a comment than a question - which is legit on Bluesky :-)"](https://bsky.app/profile/munzner.bsky.social/post/3mzybq3wjmk2s).
- Follow-ups after hallway chats. Danielle Szafir: ["Chatting after the talk, recalled that…"](https://bsky.app/profile/danielle-szafir.bsky.social/post/3mzyfqvgety2q) (CatPAL).
- Pointers to related work ([ptbremer on ProgressiVis](https://bsky.app/profile/ptbremer.bsky.social/post/3n226es3guq27)) and materials ([the PCP literacy test](https://bsky.app/profile/alark.bsky.social/post/3n25deto6vc2m)).
- The town hall thread carried policy debate, for example [anonymous reviewing at VIS](https://bsky.app/profile/discuss.ieeevis.org/post/3n24x7c4n2t2q) (a guest comment) and the replies to it.
- → First post: "Answering on the spot is hard … A discussion that is tied to the paper gives authors time to think about an answer." See Fekete's considered answers on ProgressiVis, for example [the Knuth answer](https://bsky.app/profile/jdfekete.bsky.social/post/3n22c3zenlc2k).

**4. Session chairs make or break it.**
- Jason Dykes is the model. In the talk threads he chaired, he posted a prompt from the guest bridge: ["Once again, here's your chance to engage in lively academic debate … and VOTE for your favourites! (then I get to ask them) (no need to be on BlueSky)"](https://bsky.app/profile/discuss.ieeevis.org/post/3n222cvl33o23). Other prompts: [here](https://bsky.app/profile/discuss.ieeevis.org/post/3mzzzlowbdn24), [here](https://bsky.app/profile/discuss.ieeevis.org/post/3n2236mxkix24) and [here](https://bsky.app/profile/discuss.ieeevis.org/post/3n223ufic2t2k).
- The numbers are stark. The 7 Wednesday-morning paper threads where Jason was active averaged about 11 replies. All other paper threads averaged 1.2, and 59% of them had none. (Check which of these were in his session.)
- The [Observable live-posts of a panel Q&A](https://bsky.app/profile/observablehq.com/post/3n24u7nk22k2h) show the usual time pressure: "keep answers just a LITTLE shorter". Threads can take the overflow.
- → Your point: we need to teach chairs. Establish best practices over years, write a short chair guide, and use the same practice in sessions, panels, etc., so that everybody knows what to expect.

**5. Authors are uneven at following up.**
- Good examples:
  - Jean-Daniel Fekete answered every question on [ProgressiVis](https://bsky.app/profile/papers.ieeevis.org/post/3mzzwmo4bfx2j).
  - The HiLSVA author answered every asker by name ([1](https://bsky.app/profile/kuangshiai.bsky.social/post/3mzxshiqzm223), [2](https://bsky.app/profile/kuangshiai.bsky.social/post/3mzxsyl34ec2c), [3](https://bsky.app/profile/kuangshiai.bsky.social/post/3mzxsqvwc6k2c)).
  - Also [BackdoorScope](https://bsky.app/profile/cyberloafing.bsky.social/post/3n22nmw44hc2l), [Exposing the Unsaid](https://bsky.app/profile/ritase.bsky.social/post/3n226ltku432i), [Libra+](https://bsky.app/profile/luoxu9days.bsky.social/post/3n22k7ze6mk2u), and [HeedVision](https://bsky.app/profile/arvindcheenu.bsky.social/post/3n276yqih5a2z) (two days later).
- But about three quarters of paper threads with questions got no visible answer from the authors.
- → Your point: if questions go unanswered, people stop asking. Authors need to know that answering is part of presenting: put it in the presenter instructions, nudge them after the talk, and collect more handles.

**6. Awareness and discoverability were the weakest part.**
- ["Has there been some sort of official announcement at #IEEEVIS regarding Bluesky?"](https://bsky.app/profile/chezvoila.com/post/3n25dcv2olk2l). Lane: [it was in the slides and the opening, "but maybe a blog post is a good idea"](https://bsky.app/profile/laneh.bsky.social/post/3n27cx7zwbs2p). infowantstobeseen: ["The conference site can link your Bluesky account; it is being used for (some) questions … So, sorta?"](https://bsky.app/profile/infowantstobeseen.org/post/3n25elits3c2w).
- ["So where are the #ieeevis Bluesky posts on the website going I wonder."](https://bsky.app/profile/infowantstobeseen.org/post/3mzvpxlypbk2q). The connection between the hashtag, the threads and the website was not obvious.
- Hashtag confusion: #ieeevis vs #ieeevis2026. You [announced the wrong one and corrected it](https://bsky.app/profile/domoritz.de/post/3mznpdgghqk2p). The bot used #ieeevis, while [some labs](https://bsky.app/profile/viewlab.bsky.social/post/3mzilq7rbyc2a) used #IEEEVIS2026.
- People forgot the hashtag (["forgot to tag #ieeevis"](https://bsky.app/profile/davidlaidlaw.bsky.social/post/3n23gwwy4222p)) or wondered how to get onto John's lists (["I am an ieeevis attendee and speaker and not on either list"](https://bsky.app/profile/rachelbc.bsky.social/post/3n26yajze522k)). Being visible depended on knowing the conventions.
- People also asked general conference questions there, for example [whether videos are coming](https://bsky.app/profile/infowantstobeseen.org/post/3mzy5xyrpus24).
- → Next time: a VIS blog post before the conference, a slide for chairs, one hashtag, and a QR code to the threads on screen.

**7. An open protocol let the community build on top of it.**
- John Guerra: [Influentials ranking](https://bsky.app/profile/johnguerra.bsky.social/post/3mzymezalcs2u), [starter packs](https://bsky.app/profile/johnguerra.bsky.social/post/3n27emxrrss2a), the [paper navigator with live notes](https://bsky.app/profile/johnguerra.bsky.social/post/3n22bec6jhs25), the recap, and a [bar chart race](https://bsky.app/profile/johnguerra.bsky.social/post/3n27fe4lkrk2t).
- Rahat Zaman read the first post and [added Bluesky discussions to their own publication pages](https://bsky.app/profile/rahatzaman.bsky.social/post/3mzsxgncky22w), with a how-to.
- [VIS on Lea](https://bsky.app/profile/mariaa.bsky.social/post/3mzxlhwdtni26), the [Data Viz feed](https://bsky.app/profile/jacqueschrag.com/post/3n25edtre322b), and a new [VGTC account](https://bsky.app/profile/vgtc.bsky.social/post/3n25d3pbd4b2x).
- → First post: "because anyone can build on the protocol, the conference can add its own pieces on top of it." It turned out the community did too, without the organizers.

**8. The research community reaching beyond the conference, to practitioners.**
- Chez Voila, replying to Lane in the announcement thread: ["leaving a trace online would signal to the larger dataviz community, beyond IEEEVIS, that there is a commitment, a momentum to recreate the exchanges on Bluesky."](https://bsky.app/profile/chezvoila.com/post/3n27dnh45zk2a)
- A day later, Chez Voila asked: ["how do you suggest that dataviz practitioners and researchers work together? … I've seen your research on here for the last week"](https://bsky.app/profile/chezvoila.com/post/3n2cfkcvxn22j) (23 likes). The thread kept going for days:
  - Danyel Fisher: ["This would make a great panel, or a topic at Cluster"](https://bsky.app/profile/danyelf.bsky.social/post/3n2clnqvpjn2f), and later ["an amazing thread, with some great questions for the #ieeevis community"](https://bsky.app/profile/danyelf.bsky.social/post/3n2efbaug4s2y).
  - Stephanie Tuerk, on the "For Practitioners" sections of award papers: [link](https://bsky.app/profile/stephanietuerk.net/post/3n2ci6tty3c2g).
  - Miska Knapek: [this year's VIS papers are "written in a language far more useful for real world application"](https://bsky.app/profile/miskaknapek.bsky.social/post/3n2d5sxnwi222).
- The conversation continued after the conference. Observable, still [going through papers](https://bsky.app/profile/observablehq.com/post/3n2hmxikwgk27) a few days later, asked for recommendations.
- Connect to [Cluster](https://cluster-practitioners-summit.github.io/), the practitioner track at VIS this year. Like the Bluesky discussions it was an experiment, and it brought practitioners into the program ([Observable on the Cluster sessions](https://bsky.app/profile/observablehq.com/post/3n2cgydukbk2m)). Both experiments open VIS up beyond the people in the room.
- → First post: "an online discussion includes both the people at the conference and the broader visualization community." The practitioner thread is the clearest example. It started from following the paper posts.

## Looking back at the design decisions in the first post

- **Building on Bluesky instead of our own comment system.** Worked.
  - Existing accounts, apps and notifications brought authors into threads, and the community built tools on top (theme 7).
  - Cost: we depend on Bluesky's moderation, and its automod suspended us on day one. Bluesky's people fixed it in minutes.
- **"Nobody should need a Bluesky account."** Clearly worked. 211 of 573 replies (37%) came through the guest bridge from 92 people, including chairs like Jason who used it to run their sessions.
- **Real names by default, pseudonyms optional.** Both were used: two thirds of guest comments are under real names, so threads read like conversations between people, and a third are under pseudonyms (for example the [parallelism question on ProgressiVis](https://bsky.app/profile/papers.ieeevis.org/post/3mzzwmo4bfx2j)). Did pseudonyms invite questions that would not have been asked otherwise? Your call.
- **Mentioning authors so they get notified.** Worked well in general. Coverage depends on knowing handles: 196 of 352 announcements could mention at least one author. In threads with questions, authors answered in 32% of threads where they were mentioned (27 of 85), against 12% where they were not (5 of 42). Small numbers, but it points the right way. → Collect handles at registration or camera-ready.
  - Challenge for future years: link registrations and authors carefully. Handles come from attendee profiles, so mentions only work if each registration is linked to its author entry. We did that linking manually this year. Next time, build a clear link between registrations and authors into the process from the start.
- **Likes and "most liked" sorting as a Slido replacement.** Partly. 275 likes on replies on Bluesky (guest likes come on top). Jason explicitly used voting. Unknown how many other chairs picked questions from the threads.
- **Static site plus a read proxy that maps paper ids to posts.** Worked invisibly: no rebuilds, and threads appeared on pages on their own.
- **Posting announcements shortly before each session.** Worked for timing, but posting a whole session at once is what triggered the suspension. → Spread it out.
- **Moderation (labels, hide, delete, log).** Fill in: how often did organizers have to act? If almost never, say so. It is good news.
- **One person, part time, plus coding agents.** Worth a sentence on how it held up during the week (any live fixes).
- **Switching off the service after the conference.** Still to do. Say when guest posting closes and when the mapping gets baked into the pages.

## Your reflection (skeleton)

- It worked, but it will not be done after one conference. Building a community takes time and care.
- Establish best practices over years, so that people learn, for example, how to be a session chair.
- Use the same practice in sessions, panels, etc., so that everybody knows what to expect.
- Authors need to follow up and answer questions, so that attendees feel they get value out of posting questions.
- Bluesky and Cluster were both experiments this year, and both reached past the research community (theme 8). Maybe close with that.
- Praise the web team: they worked closely with us in tech to make the Bluesky integration on the paper pages work so well, and they did a phenomenal job this year overall. Others noticed too: Alex Lex, ["Shout-out to the #ieeevis tech/web team. The schedule page on the website is AMAZING!"](https://bsky.app/profile/alex-lex.bsky.social/post/3n24t3b2qbk2k) (23 likes).
- Thanks: Jim Ray and Bluesky for the quick unsuspension, the web team, the tech team, the chairs who used it (Jason), John for the analysis, and everyone who posted.
