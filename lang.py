from rasa.nlu.components import Component
from rasa.nlu import utils
from rasa.nlu.model import Metadata

from langdetect import detect


class LangRecognizer(Component):
    """A language recognizer component"""

    name = "lang"
    provides = ["entities"]
    requires = []
    defaults = {}
   
    def __init__(self, component_config=None):
        super(LangRecognizer, self).__init__(component_config)

    def train(self, training_data, cfg, **kwargs):
        """Not needed, because the the model is pretrained"""
        pass

    def convert_to_rasa(self, value, confidence, start, end):
        """Convert model output into the Rasa NLU compatible output format."""

        entity = {"value": value,
                  "confidence": confidence,
                  "entity": "language",
                  "extractor": "lang_extractor",
                  "start": start,
                  "end": end}

        return entity

    def process(self, message, **kwargs):
        """Retrieve the text message, pass it to the classifier
            and append the prediction results to the message class."""

        res = detect(message.text)
    
        entities = self.convert_to_rasa(res, 1, 0, len(message.text))

        message.set("entities", message.get("entities", []) + [entities], add_to_output=True)


    def persist(self, file_name, model_dir):
        """Pass because a pre-trained model is already persisted"""

        pass