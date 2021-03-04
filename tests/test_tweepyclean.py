from tweepyclean import __version__
from tweepyclean import tweepyclean
import pandas as pd
from pytest import raises

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
    

    

    


