# linguistify
A unified toolkit for advanced text processing and linguistic analysis. `linguistify` offers a comprehensive set of functions to clean, preprocess, and analyze text data, applying linguistic techniques to enhance your text analytics workflow.

The purpose of the `linguistify` package is to provide tools that simplify and enhance the process of text cleaning and analysis. It aims to:

- **Clean Text Data**: Remove unwanted elements from text, such as punctuation, URLs, and special characters, and normalize text for consistent processing.
- **Feature Extraction**: Extract meaningful features from text data, including text length, stop words, and part-of-speech tags, to support various text analysis tasks.
- **Preprocess Text**: Prepare text data for further analysis or modeling by transforming it into a suitable format.
- **Analyze Text**: Apply linguistic techniques to derive insights from text, such as identifying key terms, sentiment analysis, and more.

## Getting Started

To get started with `linguistify`, you need to install it. The package is available on PyPI and can be installed using `pip`. Open your terminal and run the following command:
### Installation
```bash
pip install linguistify
```
### Usage
Here’s a basic example to get you started:
```python
import pandas as pd
from linguistify.cleaning import clean_text
from linguistify.feature_extraction import add_features_to_dataframe

# Sample text data
data = {
    'text': [
        "Check out our new product launch at https://example.com! We are excited to share it with you. Follow us @CompanyName #ProductLaunch :)"
    ]
}

df = pd.DataFrame(data)

# Clean the text
df['cleaned_text'] = df['text'].apply(clean_text)

# Extract features
df_with_features = add_features_to_dataframe(df, 'cleaned_text')
```

#### Examples:

Here is an example of a DataFrame processed by the `linguistify` package:

| text                                                                                                                                                                                                                                                                                                                                 | cleaned_text                                                                                                     | length_of_text | num_stop_words | num_digits | num_spaces | num_exclamations | num_questions | num_periods | num_adjectives | num_nouns | num_pronouns | num_verbs | num_adverbs |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|----------------|----------------|------------|------------|------------------|---------------|-------------|----------------|-----------|--------------|-----------|-------------|
| Check out our new product launch at https://example.com! We are excited to share it with you. Follow us @CompanyName #ProductLaunch :)                                                                                                                                | check out our new product launch at url we are excit to share it with you follow us mention companynam hashtag productlaunch happi | 130            | 9              | 0          | 22         | 0                | 0             | 0           | 4              | 6         | 5            | 4         | 0           |


### Contribution
Contributions are welcome! If you notice a bug or have suggestions for improvements, please let us know. 

### Author 
+ **Main Maintainer**: Jawaher Alghamdi
