# Smash Ultimate Metagame Discourse Analysis - Final Post

This project was a rollercoaster. At the start of the semester, my plan was to analyze the different attitudes about the MLB lockout by fans of different teams using Reddit (totally different, right?). The reason that fell apart is because of the lack of ability to determine the location of posters and what teams they followed, outside of looking at team subreddits. The issue is that most MLB discussion happens on r/baseball, which makes it hard to automatically categorize commenters into their respective fanbases. About halfway through the semester, I decided I needed to switch my project topic to something that was not just more practical, but also something which I had more knowledge about.

I have been in the Super Smash Bros. community for about 6 years now, and during those years I've spent lots of time on Twitter. Smashers love to vocalize their thoughts on the game in Tweet format, and so I thought this would be a good place to look for a new topic for my project. When scrolling through Twitter one day, trying to think of something to research, this tweet popped up on my feed:
![alt text](https://github.com/Leo-Kasper/is310-final-project-leo-kasper/blob/main/Capture.PNG?raw=true)

This brought several questions to my mind: Do people really complain now more than they used to? Do they complain about different things? Was Smash 4 (the last game) more complained about than Smash Ultimate (the new one)?

I realized I could answer these questions through quantitative research, and so I chose my new topic. I recalled one of this semester's readings, Ted Underwood's "Seven ways humanists are using computers to understand text", and I used that as a basis for how I can go about my data analysis (Underwood, 2015). The section in particular about identifying distinctive vocabulary caught my eye, and so I decided to try looking at the frequency of common gamer words used to express dislike or concern about a character's overall effect on the health of the metagame. 

To start this project, I used Twitter's official API. This proved to be very difficult and annoying to work with, as I kept having to apply for higher levels of access to get more features. Eventually, I realized this would not be very useful as I was looking for historical data and the API only allowed me to retrieve the last 7 days of Tweets. Normally this would be okay, but I wanted to compare the sentiment about the current game's most broken characters to the one in the last game, and to do that I needed to view Tweets from 2016 to 2018 when that game was still the latest one.

I met with Professor Leblanc and she showed me a library called Twint which provided exactly what I was looking for. Initially I had some trouble with my queries due to a lack of understanding of the search operators, but I eventually decided to just search the characters name and 'smash' for each of the characters I was looking to analyze, and then to filter for the words I was looking for.

![alt text](https://github.com/Leo-Kasper/is310-final-project-leo-kasper/blob/main/blogpic1.PNG?raw=true)

I tried several different ways of analyzing the data, first beginning with sentiment analysis (which gave me errors I couldn't fix), then to TFIDF (which didn't do what I wanted it to), and more until I eventually decided on a more manual approach. I removed all the stop words from the tweets and created CSVs of the word counts for each set of Tweets. I then searched up the words 'ban'/'banned', 'op'/'overpowered', 'nerf'/'nerfed', 'hate', and 'broken'. These are all terms commonly used by the fighting game community on Twitter.

Finally, I used the altair library used in class to create bar graph visualizations of all the counts, as well as a final image that compared the frequency of those words used for characters in Ultimate (Steve and Kazuya) vs. the best character from Smash 4 (Bayonetta). I was surprised to find that Bayonetta won by a magnitude of 10!

![alt text](https://github.com/Leo-Kasper/is310-final-project-leo-kasper/blob/main/kazuya_raw.png?raw=true)
![alt text](https://github.com/Leo-Kasper/is310-final-project-leo-kasper/blob/main/steve_raw.png?raw=true)
![alt text](https://github.com/Leo-Kasper/is310-final-project-leo-kasper/blob/main/bayo_raw.png?raw=true)
![alt text](https://github.com/Leo-Kasper/is310-final-project-leo-kasper/blob/main/comparison.png?raw=true)

I go more in depth on my hypothesized explanation for this in my presentation, as well as getting into the explanations for the raw counts (found here: https://mediaspace.illinois.edu/media/t/1_uyyj6tbt) but to summarize, I believe that COVID has a large role to play in this. Bayonetta had plenty of time and tournaments to shine in the spotlight, being picked up by a large chunk of top players, as you can see in the image of the top 15 rankings below.

![alt text](https://github.com/Leo-Kasper/is310-final-project-leo-kasper/blob/main/blogpic2.PNG?raw=true)

Right now, we are still in the midst of a global pandemic, and tournaments are only just now starting to come back after a 2 year hiatus. Steve and Kazuya both released during this hiatus of in-person tournaments, and so they haven't had much of an opportunity to be shown off at a high level of play. If we give it more time, we may see these characters change the meta, as well as shape the discourse about the game on Twitter, in a similar way to that of Bayonetta back in 2016.

Over the course of this semester, I have learned a ton about digital humanities and how quantitative analysis can be used by humanists to gain knew knowledge on a piece of literature or media. The analogies that the authors of class readings used to describe emerging technologies helped my understanding of the topics greatly and piqued my interest. One of my favorite examples of this comes from Maciej Cegłowski's "Deep Fried Data" article, in which the author likens machine learning to deep frying: "Machine learning is like a deep-fat fryer. If you’ve never deep-fried something before, you think to yourself: 'This is amazing! I bet this would work on anything!' And it kind of does." (Cegłowski, 2016). Simple, yet fitting explanations for these advanced topics allowed me to ease myself into the topics of this class without it feeling too overwhelming, which I greatly appreciate.

I was honestly a little skeptical of the concept of digital humanities research, but readings such as Miriam Posner's "Humanities Data: A Necessary Contradiction" changed my mind. "If you can analyze something computationally, I think it’s going to be really hard to tell people that they shouldn’t." (Posner, 2015). Instead of thinking about why I should do analysis on something as bland as complaints on Twitter, if I have the urge to do it why shouldn't I?

The reason I am talking about how much I enjoyed these readings is because that enjoyment and newfound curiosity motivated me to create something I am passionate about for this project. It may be simple, but this is something that I have thought about doing in the back of my mind every time I see Tweets such as the one from Lucky found earlier in this post. Lots of statistics are taken on tournament results for this game, but nobody has bothered to look into the humanities side of the Smash community until now. 

Most people who were there during ths Smash 4 days know that Bayonetta was a much larger issue and topic of discussion back then than Steve and Kazuya are now, but I don't think anybody could have predicted the sheer magnitude by which Bayonetta beats out the newcomers. With that, it seems fitting to end on a quote from Lincoln Mullen's aritcle, "Isn't it obvious?" in which he talks about how there is always something to be learned from digital humanities research: "I’ve found that [asking to predict a trend before showing them a visualization], used both for myself and with audiences, helps dispel the sense that what is learned from visualizations was already obvious." (Mullen, 2018).

# References

Cegłowski, M. (2016, September 27). Deep Fried Data. Deep-fried data. Retrieved May 14, 2022, from https://idlewords.com/talks/deep_fried_data.htm 

Mullen, L. (2018, January 10). Isn't it obvious? Isn't it obvious? | Lincoln Mullen. Retrieved May 14, 2022, from https://lincolnmullen.com/blog/isnt-it-obvious/ 

Posner, M. (2015, June 25). Humanities data: A necessary contradiction. Miriam Posners Blog. Retrieved May 14, 2022, from https://miriamposner.com/blog/humanities-data-a-necessary-contradiction/ 

SmashWiki. (2022, April 13). PGR V5. SmashWiki. Retrieved May 14, 2022, from https://www.ssbwiki.com/PGR_v5 

Underwood, T. B. (2015, November 30). Seven ways humanists are using computers to understand text. The Stone and the Shell. Retrieved May 14, 2022, from https://tedunderwood.com/2015/06/04/seven-ways-humanists-are-using-computers-to-understand-text/ 







