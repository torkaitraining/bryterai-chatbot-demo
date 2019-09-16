## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:company_question
- I own a [ltd](str_ltd).
- Can I be [shareholder](shareholder) of a [limited company](str_ltd:ltd)?
- Can I be [shareholder](shareholder) of a [private limited company](str_ltd:ltd)?
- I want to become [shareholder](shareholder) of a [limited company](str_ltd:ltd).
- I own a [plc](str_plc).
- Can I be [shareholder](shareholder) of a [limited public corporate](str_plc:plc)?
- How many [shareholders](shareholder:shareholder) this company has?
- Can my company be [shareholder](shareholder) of a [limited company](str_ltd:ltd)?
- Can my company be [shareholder](shareholder) of a [public corporate](str_plc:plc)?
- Kann ich [Gesellschafter](shareholder:shareholder) einer [GmbH](str_ltd:ltd) sein?
- Wer kann [Gesellschafter](shareholder:shareholder) einer [AG](str_plc:plc) sein?
- Kann ich mit meiner [GmbH](str_ltd:ltd) [Mehrheitseigner](shareholder:shareholder) einer [AG](str_plc:plc) sein?
- I want to own an [ltd](str_ltd)
- I want to own an [AG](str_plc:plc)
- Can I be a [shareholder](shareholder) in both an [AG](str_plc:plc) and a [private limted company](str_ltd:ltd)?
- Can my [private limited company](str_ltd:ltd) be a [shareholder](shareholder) in a [public corporate](str_plc:plc)?
- [private limited company](str_ltd:ltd)
- [ltd](str_ltd)
- [Can my private limited company be a shareholder in public corporate?](language:en)[private limited company](str_ltd:ltd) be a [shareholder](shareholder) in [public corporate](str_plc:plc)?
- [Can my private limited company be a shareholder in public corporte?](language:en)[private limited company](str_ltd:ltd) be a [shareholder](shareholder) in public corporte?
- [Can my private limited company be a shareholder in public corporate?](language:en)[private limited company](str_ltd:ltd) be a [shareholder](shareholder) in [public corporate](str_plc:plc)?

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:goodbye
- bye
- goodbye
- see you around
- see you later
- Bye
- [bye](language:no)

## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there
- Hello
- Hello
- [Hello](language:no)

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## synonym:ltd
- limited company
- private limited company
- GmbH
- private limted company
- private limited
- private corporation

## synonym:plc
- limited public corporate
- public corporate
- AG
- public limited company
- public corporation
- public company

## synonym:shareholder
- shareholders
- Gesellschafter
- Mehrheitseigner
