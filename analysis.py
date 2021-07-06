import text2emotion as te
import pandas as pd
from vader_sentiment.vader_sentiment import SentimentIntensityAnalyzer

# list definition and calling analyzer.
val = []
val2 = []
# defining sentiment analyzer variable
analyzer = SentimentIntensityAnalyzer()

# open file and read
with open('deathRowLast.csv', encoding='utf-16', mode='r') as file:
    for row in file:
        # separate the row
        sentence = row.split('|')[7]
        # use sentiment analyzer and append value in list
        vs = analyzer.polarity_scores(sentence)
        val.append(vs)
        # use emotion analyzer and append in list
        # print(te.get_emotion(sentence))
        val2.append(te.get_emotion(sentence))
        # print(val2)

    # convert list of dictionaries to dataframes
    df = pd.DataFrame(val)
    print(df)
    df2 = pd.DataFrame(val2)

# appending a new column that categories the statements by highest emotion.
series = df2.idxmax(axis=1, skipna=True)
df2['emotion'] = series
print(df2)
# convert dataframe to csv file
df2.to_csv('emotion_analysis.csv', sep='|')
df.to_csv('sentiment_analysis.csv', sep='|')

