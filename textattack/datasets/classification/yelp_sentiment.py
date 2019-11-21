from textattack import utils as utils
from textattack.datasets import TextAttackDataset

class YelpSentiment(TextAttackDataset):
    """
    Loads the Yelp Sentiment dataset.
    
    Labels:
        0 - Negative
        1 - Positive

    Args:
        n (int): The number of examples to load
        offset (int): line to start reading from
    
    """
    DATA_PATH = '/p/qdata/jm8wx/research/text_attacks/textattack_data/yelp_polarity.txt'
    def __init__(self, n=None, offset=None):
        """ Loads a full dataset from disk. """
        utils.download_if_needed(YelpSentiment.DATA_PATH)
        self.examples = self._load_text_file(YelpSentiment.DATA_PATH, n=n,
            offset=offset)
        print('YelpSentiment loaded', len(self.examples), 'examples.')
