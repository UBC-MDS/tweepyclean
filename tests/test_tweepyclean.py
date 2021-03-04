from tweepyclean import __version__
from tweepyclean import tweepyclean
import pandas as pd

def test_version():
    assert __version__ == '0.1.0'

def load_raw_data():
    """Loads raw data used for testing"""
    raw_dataframe = pd.read_csv('raw_df_example_tweets.csv')
    return raw_dataframe
    
def load_clean_data():
    """Loads clean data used for testing"""
    clean_dataframe = pd.read_csv('clean_df_example_tweets.csv')
    return clean_dataframe


def test_sentiment_total():
    output = tweepyclean.sentiment_total()
    empty_df = pd.DataFrame()
    assert (isinstance(output, pd.DataFrame))
    assert (len(output.columns) == 3)
    assert (output.iloc[:, 2].sum() == output.iloc[:, 1].mean())
    assert (sentiment_total(, ), )

def test_input_sentiment_total():
    a = [1,2,3]
    with raises(TypeError):
        tweepyclean.sentiment_total(a)
    
def test_engagement_by_hour():
    output = tweepyclean.engagement_by_hour()
    assert (isinstance(output, plotly.graph_objs._figure.Figure))
    
def test_input_type_engagement():
    a = [1,2,3]
    with raises(TypeError):
        tweepyclean.engagement_by_hour(a)

