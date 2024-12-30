import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from preprocessing import preprocess_text

# Download NLTK resources (only needed once)
import nltk
nltk.download('punkt_tab')

# Load sample data (you can replace this with your own dataset)
data = {
    'text': [
        "I love this product!",
        "This is the worst experience I've ever had.",
        "It's okay, not great but not bad either.",
        "Absolutely fantastic! Highly recommend.",
        "I'm disappointed with this purchase.",
        "This is a one of the best apps acording to a bunch of people and I agree it has bombs eggs pigs TNT king pigs and realustic stuff.",
        "This is a pretty good version of the game for being free. There are LOTS of different levels to play. My kids enjoy it a lot too.",
        "this is a really cool game. there are a bunch of levels and you can find golden eggs. super fun.",
        "This is a silly game and can be frustrating, but lots of fun and definitely recommend just as a fun time.",
        "This is a terrific game on any pad. Hrs of fun.  My grandkids love it. Great entertainment when waiting in long lines.",
        "This is a very entertaining game!  You don't have to be smart to play it.  I guess that's why I like it...it's easy and fun and that's what games are suppose to be.  Be warned: this game is highly addictive.",
        "this is awesome and you don't need wi ti to play trust me. it is really fun and addicting. there are like 100 levels it is even free don't waste your money on the expensive one I mean seriously. get the app.",
        "this is awesome I bet no one even reads the reviews because they know this game is so good that they need to.",
        "This is basicly the free version but with ads. That's actually awesome!!!! It's addicting and free at the same time really. Id reccomend it.",
        "this is by far the best free app that is available anywhere. it has helped pass the time when nothing else would do. does not pass this one up. PS I hate this 20 word minimum!.",
        "This is definitely a great game.  I have to get my 6-year-old grand-nephew to teach me the tricks.  I have figured out some of them, but some configurations are tough to beat.  I does not particularly care spending about 45 minutes  completing a level, but.",
        "This is good if you like physics games, free games, or bird games. Not like free version on ipod. You get all the levels and the only adds pop up in the corner and are barely noticeable.",
        "This game is really fun to play. My dad loves to play this game on my kindle. He finished the game on his phone, so he is doing it on my kindle now.",
        "My youngest grandson of 4 yrs. loves this game and he plays it whenever he is here. He down loads other free games as well.",
        "I love the challengers set up in the different series as you progress to higher level games in each set. I was over 60 yrs. old when I first learned to play this game. I'm now over 70 yrs. old & still getting a big kick when I play these games. I am alwa.",
        "This game is loads of fun and very frustrating at the same time if you are trying to get all 3 stars on each level. I have finally completed every level with 3 stars and completed all 22 golden egg levels. I have version 1.5.3. I installed the updated ve.",
        "I believe this game got me started on an angry birds addiction.  The games are challenging and fun with loads of different backgrounds to keep it interesting.",
        "Just as fun and challenging as the rest of the Angry Birds adventures. Our grand kids thoroughly enjoy it.Thanks for the freebie!.",
        "Great game.. will recommend to others.Angry Birds Angry Birds Angry Birds Angry Birds Angry Birds Angry Birds Angry Birds Angry Birds Angry BirdsYesss!.",
        "My daughter loves to play this game and has downloaded lots of games on my kindle fire she loves all the angry birds games and loves to play them.",
        "Longtime Angry Birds player, Angry Birds runs great on my new Kindle, which I found to my great relief. Yay!.",
    
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Preprocess text data
df['processed_text'] = df['text'].apply(preprocess_text)

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(text):
    score = analyzer.polarity_scores(text)
    if score['compound'] >= 0.05:
        return 'Positive'
    elif score['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment analysis to the processed DataFrame
df['sentiment'] = df['processed_text'].apply(analyze_sentiment)

# Print results
print(df[['text', 'processed_text', 'sentiment']])