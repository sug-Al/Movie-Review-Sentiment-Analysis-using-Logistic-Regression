import pandas as pd
import string
import nltk
import joblib

from bs4 import BeautifulSoup
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

from tfidf_logreg_module import Logistic_Regression as lr


def preprocessing(df):

    df["text"] = df["text"].str.lower()

    df["text"] = df["text"].apply(lambda text: BeautifulSoup(text, "lxml").text)

    stop_words = set(stopwords.words('english'))
    df["text"] = df["text"].apply(lambda text: " ".join([word for word in str(text).split()
                                                        if word not in stop_words]))

    punct_to_remove = string.punctuation
    df["text"] = df["text"].apply(lambda text: text.translate(str.maketrans(' ', ' ', punct_to_remove)))

    df["text"] = df["text"].apply(lambda text: " ".join([line for line in str(text).split()
                                                         if not line.isdigit()]))

    lemmatizer = WordNetLemmatizer()
    wordnet_map = {
        "N": wordnet.NOUN,
        "V": wordnet.VERB,
        "J": wordnet.ADJ,
        "R": wordnet.ADV
    }
    df["text"] = df["text"].apply(lambda text: " ".join([lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN))
                                                        for word, pos in nltk.pos_tag(text.split())]))

    return df


def feature_extraction(df):

    vectorizer = TfidfVectorizer(ngram_range=(1, 3), min_df=0.0015)
    fitted_vectorizer = vectorizer.fit(df["text"])
    # joblib.dump(fitted_vectorizer, 'feature-extraction-tfidf.joblib')
    # joblib.load('feature-extraction-tfidf.joblib')
    return fitted_vectorizer.transform(df["text"])


def model_generator(train_transform, y):

    X_train = train_transform.toarray()
    y_train = y
    log_reg = lr.Logistic_Regression(learning_rate=0.9, no_of_iterations=10000)
    log_reg.fit(X_train, y_train)
    print(joblib.dump(log_reg, "log-reg-model.joblib"))


dataframe = pd. read_csv('train.csv', header=None, delimiter=',', skiprows=1, names=['text', 'label'])

df_train = preprocessing(dataframe)

train_vectorized = feature_extraction(df_train)

model_generator(train_vectorized, dataframe["label"])
