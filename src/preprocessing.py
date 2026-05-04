import neattext.functions as nfx
import re
from mahaNLP.preprocessing import MarathiPreprocessor


# Initialize Marathi Preprocessor
marathi_processor = MarathiPreprocessor()


def clean_english_text(text):
    """Clean English text before translation"""
    text = str(text)

    text = nfx.remove_userhandles(text)      # @user
    text = nfx.remove_urls(text)             # links
    text = nfx.remove_emojis(text)
    text = nfx.remove_punctuations(text)
    text = nfx.remove_special_characters(text)
    text = nfx.remove_stopwords(text)

    return text.strip()


def clean_marathi_text(text):
    """Clean Marathi text after translation"""
    text = str(text)

    # remove URLs manually (important)
    text = re.sub(r'http\S+|www\S+', '', text)

    # remove @mentions
    text = re.sub(r'@\w+', '', text)

    # remove hashtags
    text = re.sub(r'#\w+', '', text)

    # mahaNLP processing
    text = marathi_processor.remove_punctuation(text)
    text = marathi_processor.remove_stopwords(text)
    text = marathi_processor.normalize(text)

    # extra cleanup
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def full_preprocessing_pipeline(df):
    """
    Complete preprocessing pipeline
    """

    # Safety: drop missing rows
    df = df.dropna(subset=['English_Text', 'Marathi_Text', 'Emotion'])

    # Clean English
    df['clean_en'] = df['English_Text'].apply(clean_english_text)

    # Clean Marathi
    df['clean_mr'] = df['Marathi_Text'].apply(clean_marathi_text)

    return df