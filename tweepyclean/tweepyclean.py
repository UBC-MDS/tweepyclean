

def sentiment_total(data, lexicon):

    '''
    Takes unaggregated tweet data and summarizes the number of tweeted words associated with particular emotional sentiments.

    Parameters:
    -------
    data (dataframe): unaggregated tweet data. Obtained from using most_common().
    lexicon (str): the particular sentiments the user selects.
                    

    Returns:
    pandas.DataFrame

    #>>> sentiment(df, “nrc”)
    
    
    A tibble: 3 x 3
    sentiment      total_words     words
    <chr>          <int>           <dbl>
    anger          4901            321
    anticipation   4901            256
    disgust        4901            207
    '''


