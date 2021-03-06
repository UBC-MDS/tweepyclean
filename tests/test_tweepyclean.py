from tweepyclean import __version__
from tweepyclean import tweepyclean
import pandas as pd
import altair as alt
from pytest import raises
import re # Needed for clean_tweets() regex to remove emojis
from nltk.sentiment.vader import SentimentIntensityAnalyzer # Needed for clean_tweets() to generate sentiment score
import textstat # Needed for clean_tweets() to generate flesch_readability score
import emoji # Needed for clean_tweets() to extract emojis
import tweepy # Needed to check for tweepy.cursor.ItemIterator object

def test_version():
    assert __version__ == '0.1.0'

def load_raw_data():
    """Loads raw data used for testing"""
    raw_dataframe = pd.read_csv('tests/raw_df_example_tweets.csv')
    return raw_dataframe
    
def load_clean_data():
    """Loads clean data used for testing"""
    clean_dataframe = pd.read_csv('tests/clean_df_example_tweets.csv')
    return clean_dataframe

def test_raw_df():
    "tests raw_df() function"
    with raises(TypeError):
        tweepyclean.raw_df("wrong_datatype")

def test_clean_tweets():
    "tests clean_tweets() function"
    raw_df = load_raw_data()
    output_df_test = tweepyclean.clean_tweets(raw_df, handle = "Canucks")
    
    # Confirm output is a dataframe
    assert (isinstance(tweepyclean.clean_tweets(raw_df, handle = "Canucks"), pd.DataFrame))
    
    # Check input type errors
    with raises(TypeError):
        tweepyclean.clean_tweets(["wrong", "datatype"], handle = "Canucks")
    with raises(TypeError):
        tweepyclean.clean_tweets(raw_df, handle = 156.56)
    
    # Check if neccesary columns are present
    raw_df_no_retweet_count = raw_df.drop('retweet_count', 1)
    with raises(ValueError):
        tweepyclean.clean_tweets(raw_df_no_retweet_count, handle = "Canucks")
        
    raw_df_no_favorite_count = raw_df.drop('favorite_count', 1)
    with raises(ValueError):
        tweepyclean.clean_tweets(raw_df_no_retweet_count, handle = "Canucks")
    
    raw_df_no_entities = raw_df.drop('entities', 1)
    with raises(ValueError):
        tweepyclean.clean_tweets(raw_df_no_entities, handle = "Canucks")
    
    raw_df_no_full_text = raw_df.drop('full_text', 1)
    with raises(ValueError):
        tweepyclean.clean_tweets(raw_df_no_entities, handle = "Canucks")
    
    # Confirm output is a dataframe
    assert (isinstance(tweepyclean.clean_tweets(raw_df, handle = "Canucks"), pd.DataFrame))
    
    # Check input type errors
    with raises(TypeError):
        tweepyclean.clean_tweets(["wrong", "datatype"], handle = "Canucks")
    with raises(TypeError):
        tweepyclean.clean_tweets(raw_df, handle = 156.56)
    
    # Check if neccesary columns are present
    raw_df_no_retweet_count = raw_df.drop('retweet_count', 1)
    with raises(ValueError):
        tweepyclean.clean_tweets(raw_df_no_retweet_count, handle = "Canucks")
        
    raw_df_no_favorite_count = raw_df.drop('favorite_count', 1)
    with raises(ValueError):
        tweepyclean.clean_tweets(raw_df_no_retweet_count, handle = "Canucks")
    
    raw_df_no_entities = raw_df.drop('entities', 1)
    with raises(ValueError):
        tweepyclean.clean_tweets(raw_df_no_entities, handle = "Canucks")
    
    raw_df_no_full_text = raw_df.drop('full_text', 1)
    with raises(ValueError):
        tweepyclean.clean_tweets(raw_df_no_entities, handle = "Canucks")
    
    # Check if the correct columns are generated in for output
    output_df_test_handle = tweepyclean.clean_tweets(raw_df, handle = "Canucks")
    assert 'handle' in output_df_test_handle.columns, "no handle column in output when it should have been generated"
    
    output_df_text_only = tweepyclean.clean_tweets(raw_df, handle = "Canucks", text_only = True)
    assert 'text_only' in output_df_text_only.columns, "no text_only column in output when it should have been generated"
    
    output_df_word_count= tweepyclean.clean_tweets(raw_df, handle = "Canucks", word_count = True)
    assert 'word_count' in output_df_word_count.columns, "no word_count column in output when it should have been generated"
    
    output_df_emojis = tweepyclean.clean_tweets(raw_df, handle = "Canucks", emojis = True)
    assert 'emojis' in output_df_emojis.columns, "no emojis column in output when it should have been generated"
    
    output_df_hashtags = tweepyclean.clean_tweets(raw_df, handle = "Canucks", hashtags = True)
    assert 'hashtags' in output_df_hashtags.columns, "no hashtags column in output when it should have been generated"
    
    output_df_sentiment = tweepyclean.clean_tweets(raw_df, handle = "Canucks", sentiment = True)
    assert 'sentiment_polarity' in output_df_sentiment.columns, "no sentiment_polarity column in output when it should have been generated"
    
    output_df_flesch_readability = tweepyclean.clean_tweets(raw_df, handle = "Canucks", flesch_readability = True)
    assert 'flesch_readability_score' in output_df_flesch_readability.columns, "no flesch_readability_score column in output when it should have been generated"
    
    # output_df_media_links = tweepyclean.clean_tweets(raw_df, handle = "Canucks", media_links = True)
    # assert 'media' in output_df_media_links.columns, "no media column in output when it should have been generated"
    # assert 'media_url' in output_df_media_links.columns, "no media_url column in output when it should have been generated"
    # assert 'media_link' in output_df_media_links.columns, "no media_link column in output when it should have been generated"

    output_df_proportion_of_avg_retweets = tweepyclean.clean_tweets(raw_df, handle = "Canucks", proportion_of_avg_retweets = True)
    assert 'prptn_rts_vs_avg' in output_df_proportion_of_avg_retweets.columns, "no prptn_rts_vs_avg column in output when it should have been generated"
    
    output_df_proportion_of_avg_favorites = tweepyclean.clean_tweets(raw_df, handle = "Canucks", proportion_of_avg_favorites = True)
    assert 'proportion_favorites_vs_avg' in output_df_proportion_of_avg_favorites.columns, "no proportion_favorites_vs_avg column in output when it should have been generated"


def test_tweet_words():
    clean_data = pd.DataFrame({'id' : [1,2,3,4,5],
                               'text_only' : [
                                   'this is example tweet 1',
                                   'this is example tweet 2 with a few extra words',
                                   'is third',
                                   '4th tweet',
                                   'fifth tweet']})
    
    expected_output = pd.DataFrame({'words' : ['tweet', 'is', 'this'],
                                    'count' : [4, 3, 2]})
    
    actual_output = tweepyclean.tweet_words(clean_data, 3)
    
    # check if the output is a dataframe
    assert (isinstance(tweepyclean.tweet_words(clean_data, 3), pd.DataFrame))
    
    # check if the output has 2 columns
    assert (tweepyclean.tweet_words(clean_data, 3).shape[1] == 2)
    
    # check input type raises error when it should
    with raises(TypeError):
        tweepyclean.tweet_words(5, 3)
    with raises(TypeError):
        tweepyclean.tweet_words(clean_data, pd.DataFrame())
    with raises(ValueError):
        tweepyclean.tweet_words(clean_data, 0)
            
    # check if function returns the correct dataframe for example data
    pd.testing.assert_frame_equal(actual_output,expected_output)
    pd.testing.assert_frame_equal(tweepyclean.tweet_words(clean_data, 1),
                                  pd.DataFrame({'words' : ['tweet'],
                                  'count' : [4]}))
    pd.testing.assert_frame_equal(tweepyclean.tweet_words(clean_data),
                                  pd.DataFrame({'words' : ['tweet'],
                                    'count' : [4]}))
    pd.testing.assert_frame_equal(tweepyclean.tweet_words(clean_data, 1000),
                                  pd.DataFrame({'words': {0: 'tweet',
                                                          1: 'is',
                                                          2: 'this',
                                                          3: 'example',
                                                          4: 'words',
                                                          5: 'with',
                                                          6: 'third',
                                                          7: 'fifth',
                                                          8: 'few',
                                                          9: 'extra',
                                                          10: 'a',
                                                          11: '4th',
                                                          12: '2',
                                                          13: '1'},
                                                         'count': {0: 4,
                                                          1: 3,
                                                          2: 2,
                                                          3: 2,
                                                          4: 1,
                                                          5: 1,
                                                          6: 1,
                                                          7: 1,
                                                          8: 1,
                                                          9: 1,
                                                          10: 1,
                                                          11: 1,
                                                          12: 1,
                                                          13: 1}}))


def test_engagement_by_hour():
    
    test_data = pd.DataFrame({'created_at' : ['Sun Feb 28 16:16:35 +0000 2021', 'Sun Feb 28 14:34:00 +0000 2021',
                                              'Wed Feb 24 19:17:38 +0000 2021', 'Tue Feb 23 17:41:37 +0000 2021'],
                                'retweet_count' : [12, 25, 15, 4],
                                'favorite_count' : [20, 23, 33, 24]})
    
    chart = tweepyclean.engagement_by_hour(test_data)
    
    # check chart attributes
#     assert chart.encoding.x.field == 'hour', 'x_axis should be mapped to the x axis'
#     assert chart.encoding.y.field == 'total_engagement', 'y_axis should be mapped to the y axis'
    assert chart.mark == 'line', 'mark should be a line'
    
# check input type raises error when it should
    with raises(TypeError):
        tweepyclean.engagement_by_hour(['1', '2', '3'], pd.DataFrame())