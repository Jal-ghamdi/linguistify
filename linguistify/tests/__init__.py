__version__ = '0.1.0'

from linguistify.cleaning import clean_text
from linguistify.feature_extraction import add_features_to_dataframe

def test_clean_text():
    data = {
        'text': [
            "this is # and there is @ where :) was nice."
        ]
    }

    df = pd.DataFrame(data)

    # Apply the `clean_text` function to the 'text' column
    df['cleaned_text'] = df['text'].apply(clean_text)

    # Check the result
    expected = "this is hashtag and there is mention where happy was nice"
    assert df['cleaned_text'].iloc[0] == expected