


def most_common(clean_dataframe, top_n):
	
    """
	Returns the most common words and counts from a list of tweets
	
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
	#>>> most_common(dataframe, 3)

	pd.DataFrame(data = {'words' : ['best', 'apple', 'news'], 'count' : [102, 52, 24]}) 
    """

def sentiment_total(data, lexicon):

    """
    Takes unaggregated tweet data and summarizes the number of tweeted words associated with particular emotional sentiments.

    Parameters:
    -------
    data: pandas.DataFrame 
        unaggregated tweet data. Obtained from using most_common().
    lexicon: string or list
        the particular sentiments the user selects.
                    

    Returns:
    --------
    pandas.DataFrame

    Examples:
    ---------
    #>>> sentiment(df, “nrc”)

    A tibble: 3 x 3
    sentiment      total_words     words
    <chr>          <int>           <dbl>
    anger          4901            321
    anticipation   4901            256
    disgust        4901            207
    """


