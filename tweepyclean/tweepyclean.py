import pandas as pd

def raw_tweets(tweets):
    """
    Creates a dataframe with labeled columns from a tweepy.cursor.ItemIterator object.
    Parameters
    ----------
    tweets : tweepy.cursor.ItemIterator
        Input Iterator object generated using the tweepy package
    
    Returns
    -------
    tweets_df: pandas.core.frame.DataFrame
        Dataframe with up to 31 labeled columns based on the info stored in the ItemIterator.
    
    Examples:
    --------
    #>>> raw_df(tweets)
    """
    import pandas as pd

    tweet_search_results = []
    for status in tweets:
        tweet_search_results.append(status._json)
    return(pd.DataFrame(tweet_search_results))

def clean_tweets(tweets, handle = "", text_only = True, emojis = True, hashtags = True, sentiment = True, flesch_readability = True, media_links = True, proportion_of_avg_retweets = True, proportion_of_avg_hearts = True):
    """
    Creates new columns based on the data in the pandas.dataframe generated by raw_df()
    Parameters
    ----------
    raw_dataframe: pandas.core.frame.DataFrame
        Dataframe generated by raw_tweets() which will have columns added to it
    handle: string, optional
        String which adds adds a column containing the a specified twitter handle, (default is none and adds no column)
    text_only : bool, optional
        Bool which specifies to add a column of the tweet text containing no emojis, links, hashtags, or mentions (default is True)
    emojis: bool, optional
        Bool which specifies to add a column of the extracted emojis from tweet text and places them in their own column (default is True)
    hashtags: bool, optional
        Bool which specifies to add a column of the extracted hashtags from tweet text (default is True)
    sentiment: bool, optional
        Bool which specifies to add a column containing the nltk.sentiment.vader SentimentIntensityAnalyzer sentiment score for each tweet (default is True)
    flesch_readability: bool, optional
        Bool which specifies to add a column containing the textstat flesch readability score (default is True)
    media_links: bool, optional 
        Bool which specifies to add a column containing links to photo or video attached to a tweet (default is True)
    proportion_of_avg_retweets: bool, optional
        Bool which specifies to add a column containing a proportion value of how many retweets a tweet received compared to the account average (default is True)
    proportion_of_avg_hearts: bool, optional
        Bool which specifies to add a column containing a proportion value of how many hearts a tweet received compared to the account average (default is True)
    
    Returns
    -------
    tweets_df_extra: pandas.core.frame.DataFrame
        Pandas dataframe containing the additional columns specified by the user.
    
    Examples
    --------
    #>>> extra_cols(tweets_df)
    #>>> extra_cols(tweets_df, flesch_readability = False)
    #>>> extra_cols(tweets_df, emojis = False, hashtags = False, sentiment = False)
    """

def tweet_words(clean_dataframe, top_n=1):	
    """
	Returns the most common words and counts from a list of tweets.
    
    The output is sorted descending by the count of words and in reverse
    alphabetical order for any word ties.
    
	
    Parameters
	----------
	clean_dataframe : pandas.DataFrame
		A processed dataframe containing a user's tweet history and associated information
	top_n : int
		An integer representing the the number of most common words to display
	
    Returns
	-------
	pandas.DataFrame
		A dataframe with one column containing individual words and a second column with the count of each word
	
    Examples:
	--------
	#>>> tweet_words(dataframe, 3)

	pd.DataFrame(data = {'words' : ['best', 'apple', 'news'], 'count' : [102, 52, 24]}) 
    """

    # check input type of clean_dataframe
    if not isinstance(clean_dataframe, pd.DataFrame):
        raise TypeError("clean_dataframe should be of type pd.DataFrame")
    
    # check input of top_n
    if not isinstance(top_n, int):
        raise TypeError("top_n should be of type Int")
    
    # check if top_n is greater than 0
    if top_n == 0:
        raise ValueError("top_n must be greater than 0")
        
    # keep only the necessary column to count words
    clean_text_column = 'text_only'
    
    split_words_df = clean_dataframe[clean_text_column].str.split().explode()
    output = split_words_df.value_counts().to_frame()
    
    # index and column transformations
    output['words'] = output.index
    output.reset_index(inplace=True, drop=True)
    output.rename(columns={'text_only': 'count'}, inplace=True)
    output = output[['words', 'count']]
    
    # sort by alphabetical while preserving numerical sort
    output = output.sort_values(['count', 'words'], ascending=False)
    output.reset_index(inplace=True, drop=True)    
    
    # select top_n
    if top_n >= output.shape[0]:
        output = output
    else:
        output = output.iloc[0:top_n, :]
    
    return output
  

def sentiment_total(data, drop_sentiment = False):

    """
    Takes an input of of single english words and outputs the number of words associated 
    with eight emotions and positive/negative sentiment. This is based on the the 
    crowd-sourced NRC Emotion Lexicon, which associates words with eight basic emotions 
    (anger, fear, anticipation, trust, surprise, sadness, joy, and disgust) and two 
    sentiments (negative and positive). For more information on NRC: 
    http://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm
    
    Note that words can be 0:n with emotions (either associated with none, 1, or many).
    
    Parameters:
    -------
    data: pandas.DataFrame or np.array
        A list or single column dataframe of single words.
    drop_sentiment: boolean
        drop emotion/sentiment rows if no words are associated with them. Default is False.
                    
    Returns:
    --------
    pandas.DataFrame

    Examples:
    ---------
    #>>> sentiment(df, drop_sentiment = True)

    3 x 5
    sentiment      word_count  total_words
    <chr>          <int>       <dbl>
    anger          1            4
    disgust        2            4
    fear           1            4
    negative       2            4
    sadness        1            4
    """
    
    # delete once I get a function to get list of tweet word from clean_df 
    tweet_words = pd.DataFrame({"word": ["bad", "thrilled", "pissed", "gross"]})
    
    total_words = len(data)
    emotion_lexicon_df = pd.read_csv("data/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt", sep = "\t") #NRC dataset

    tweet_words_sentiment = pd.merge(data, emotion_lexicon_df, how = 'inner')
    
    #if user deviates from default parameter drop 0 count sentiments
    if drop_sentiment == True:  
        tweet_words_sentiment = tweet_words_sentiment[tweet_words_sentiment['count'] == 1]
        
    # get aggregated sentiment-words counts
    tweet_words_sentiment = tweet_words_sentiment.groupby(['sentiment'], as_index = False).sum()
    tweet_words_sentiment = tweet_words_sentiment.rename(columns = {'count': 'word_count'})
    tweet_words_sentiment['total_words'] = total_words
    return tweet_words_sentiment



def engagement_by_hour(tweets):
    """
    Creates a line chart of total number of likes and retweets received by hour of tweet posted.
    
    Parameters
    ----------
    tweets : pandas.DataFrame
        A processed dataframe containing a user's tweet history and associated information
    
    Returns
    -------
    An Altair graph object (line chart) of total engagement received by hour of tweet posted
    
    Examples
    --------
    #>>> engagement_by_hour(tweets_df)
    """


