import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def preprocess(reviews: list[str]) -> list[str]:
    """Cleans and preprocesses a list of text reviews.

    Removes non-alphabetic chars, lowercases, stems (Porter), and removes
    English stopwords (excluding 'not'). Handles non-string input.

    Args:
        reviews: A list of raw text review strings.

    Returns:
        A list of processed review strings.
    """
    corpus = []

    # NOTE: Consider handling NLTK download outside this function
    try:
        nltk.data.find('corpora/stopwords')
    except (nltk.downloader.DownloadError, LookupError):
        nltk.download('stopwords', quiet=True)

    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    if 'not' in all_stopwords:
        all_stopwords.remove('not')
    stopwords_set = set(all_stopwords)

    for i in range(len(reviews)):
        if not isinstance(reviews[i], str):
            review_text = ""
        else:
            review_text = reviews[i]

        review = re.sub('[^a-zA-Z]', ' ', review_text)
        review = review.lower()
        review = review.split()
        review = [ps.stem(word) for word in review if word not in stopwords_set]
        review = ' '.join(review)
        corpus.append(review)

    return corpus

