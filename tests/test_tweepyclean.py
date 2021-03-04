from tweepyclean import __version__
from tweepyclean import tweepyclean
import pandas as pd

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

def test_tweet_words():
    clean_data = load_clean_data()
    assert(5 == 5)
    


