# Rasa Chatbot Demo with Custom Component
In this project, I created a custom component to detect the language used in the message. Beside initial intents provided by Rasa demo project, I 
added an intent related to structure of the company. 

### Overview of the Dataset
Tags
1. Lang: English
2. Lang: German
3. Company Structure: Ltd.
4. Company Structure: plc
5. Shareholder

3 and 4 refer to the legal structure a company chooses (limited liability company vs.
corporation).

Example Questions/Training Data:
- “Can I be shareholder of a limited company?” -> 1,3,5
- “I want to become shareholder of a limited company.” -> 1,3,5
- “Can I be shareholder of a limited public corporate?” -> 1,4,5
- “Can my company be shareholder of a limited company?” -> 1,3,5
- “Can my company be shareholder of a public corporate?” -> 1,4,5
- “Kann ich Gesellschafter einer GmbH sein?“ -> 2,3,5
- „Wer kann Gesellschafter einer AG sein?“ -> 2,4,5
- „Kann ich mit meiner GmbH Mehrheitseigner einer AG sein?“ -> 2, 3,4,5

The data is very limited. I added a few sentences. More relevant sentences can be added using Ludwig sentence search engine. 

### Installation
- First, a conda environment with python 3.7 is created. It can be done using following command:
``` conda create -n myenv python=3.7 ```
- Rasa 1.2.8 and Rasa X are installed using the following commands:
```
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
```

### Steps
- Rasa demo project is created using command:
```rasa init```
- In ```nlu.md```, a new intent "company_question", new entities like "str_ltd", "str_plc", "shareholder" are defined. 
- In ```domain.yml```, a new action "utter_company_question" is defined.
- Model is trained and run to see if the intent is identified correctly. 
![Intent Identification](images/1.png?raw=true)
- Model is run in interactive mode to see if entities are identified correctly. 
![Entities Identification](images/3.png?raw=true)
- To detect the language of the message, a custom component is defined in ```lang.py```. Python ```lang_detect``` module is used, 
a better approach would be to use commercially used google api for language recognition. 
```
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
```
- As a custom component is used, pipeline in ```config.yml``` is to be modified:
```
pipeline: 
    - name: "lang.LangRecognizer"
    - name: "WhitespaceTokenizer"
    - name: "RegexFeaturizer"
    - name: "CRFEntityExtractor"
    - name: "EntitySynonymMapper"
    - name: "CountVectorsFeaturizer"
    - name: "CountVectorsFeaturizer"
      analyzer: "char_wb"
      min_ngram: 1
      max_ngram: 4
    - name: "EmbeddingIntentClassifier"
```
- Model is retrained and tested to see if language is identified correctly as an entity beside other entities.
![Language Entitiy Identification](images/4.png?raw=true)

## Instructions:
1. Install Rasa as mentioned above. 
2. Clone this repository. 
3. In terminal, use the commands ```rasa shell``` or ```rasa interactive``` to test how the custom component works. 

