## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## str path 1
* greet
  - utter_greet
* company_question
  - utter_company_question
* affirm
  - utter_happy



## interactive_story_1
* greet
    - utter_greet
* company_question{"str_ltd": "ltd", "shareholder": "shareholder", "str_plc": "plc"}
    - utter_company_question
* company_question{"str_ltd": "ltd"}
    - utter_happy
* company_question{"str_lted": "ltd"}
* goodbye

## interactive_story_1
* greet
    - utter_greet

## interactive_story_1
* greet{"language": "no"}
    - utter_greet
* company_question{"language": "en", "str_ltd": "ltd", "shareholder": "shareholder", "str_plc": "plc"}
    - utter_company_question
* company_question{"language": "en", "str_ltd": "ltd", "shareholder": "shareholder"}
    - utter_company_question
* company_question{"language": "en", "str_ltd": "ltd", "shareholder": "shareholder", "str_plc": "plc"}
* goodbye{"language": "no"}
