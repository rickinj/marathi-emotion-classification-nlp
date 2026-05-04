from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


def build_model(vectorizer_type="count"):
    """
    Build NLP pipeline
    """

    if vectorizer_type == "count":
        vectorizer = CountVectorizer()
    else:
        vectorizer = TfidfVectorizer()

    pipeline = Pipeline([
        ('vectorizer', vectorizer),
        ('model', LogisticRegression(max_iter=300, solver='lbfgs'))
    ])

    return pipeline


def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)

    acc = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)

    return acc, report


def predict_text(model, text):
    return model.predict([text])[0]