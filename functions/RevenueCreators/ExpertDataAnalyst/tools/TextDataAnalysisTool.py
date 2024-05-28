from agency_swarm.tools import BaseTool
from pydantic import Field
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import spacy


class TextDataAnalysisTool(BaseTool):
    """
    A tool designed to analyze text data, leveraging NLP techniques for sentiment analysis, topic discovery, and keyword extraction. This tool enables the ExpertDataAnalyst agent to process transcripts and textual data for insights.
    """

    text_data: str = Field(
        ..., description="The text content to be analyzed.")

    def run(self):
        # Loading NLTK and spaCy resources
        nltk.download('vader_lexicon')
        nlp = spacy.load('en_core_web_sm')

        # Sentiment analysis
        sia = SentimentIntensityAnalyzer()
        sentiment = sia.polarity_scores(self.text_data)

        # Keyword extraction and topic modeling (simplified example)
        doc = nlp(self.text_data)
        keywords = [token.text for token in doc if token.is_stop != True and token.is_punct != True]

        # Return a compiled analysis result
        return f"Sentiment Analysis: {sentiment}\nKeywords: {keywords}"
