from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'election_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    numeric_question = models.IntegerField(
        label='What is your age?'
    )
    
    gender_question = models.StringField(
        label='With which gender do you identify yourself?',
        choices=['Female', 'Male', 'Diverse', 'I do not want to specify a gender']
    )

    region_question = models.StringField(
        label='In which region do you live?',
        choices=['Baden-Württemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen', 'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen', 'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland', 'Sachsen', 'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thüringen', 'I have German citizenship and live abroad', 'None of the above']
    )
    
    text_question = models.StringField(
        label='In your opinion, what is the most important policy issue at the moment? Please enter only one issue.'
    )
    
    party_vote_question = models.StringField(
        label='If the federal election were held next Sunday, which party would you vote?',
        choices=['CDU / CSU', 'SPD', 'GRÜNE', 'FDP', 'DIE LINKE', 'AfD', 'FW', 'BSW', 'Another party', 'I would not vote', 'None of the above']
    )
