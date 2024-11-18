from otree.api import *
from .models import *

class WelcomePage(Page):
    template_name = 'global/WelcomePage.html'

class PolicyIssuePage(Page):
    form_model = 'player'
    form_fields = ['text_question']
    template_name = 'global/SurveyPage.html'

    def vars_for_template(self):
        return {
            'page_title': 'Policies',
            'question_text': 'In your opinion, what is the most important policy issue at the moment? Please state only one issue.',
            'question_type': 'text',
            'question_name': 'text_question'
        }

class VotingDecisionPage(Page):
    form_model = 'player'
    form_fields = ['party_vote_question']
    template_name = 'global/SurveyPage.html'

    def vars_for_template(self):
        return {
            'page_title': 'Voting decision',
            'question_text': 'If the federal election were held next Sunday, which party would you vote?',
            'question_type': 'choice',
            'question_name': 'party_vote_question',
            'choices': ['CDU / CSU', 'SPD', 'GRÜNE', 'FDP', 'DIE LINKE', 'AfD', 'FW', 'BSW', 'Another party', 'I would not vote', 'None of the above']
        }

# Sociodemographics

class NumericQuestionPage(Page):
    form_model = 'player'
    form_fields = ['numeric_question']
    template_name = 'global/SurveyPage.html'

    def vars_for_template(self):
        return {
            'page_title': 'Sociodemographics',
            'question_text': 'Please provide your age:',
            'question_type': 'numeric',
            'question_name': 'numeric_question'
        }

class GenderQuestionPage(Page):
    form_model = 'player'
    form_fields = ['gender_question']
    template_name = 'global/SurveyPage.html'

    def vars_for_template(self):
        return {
            'page_title': 'Sociodemographics',
            'question_text': 'Please specify your gender:',
            'question_type': 'choice',
            'question_name': 'gender_question',
            'choices': ['Female', 'Male', 'Diverse', 'I do not want to specify a gender']
        }

class RegionQuestionPage(Page):
    form_model = 'player'
    form_fields = ['region_question']
    template_name = 'global/SurveyPage.html'

    def vars_for_template(self):
        return {
            'page_title': 'Sociodemographics',
            'question_text': 'Please specify your region:',
            'question_type': 'choice',
            'question_name': 'region_question',
            'choices': ['Baden-Württemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen', 'Hamburg', 
                        'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen', 'Nordrhein-Westfalen', 
                        'Rheinland-Pfalz', 'Saarland', 'Sachsen', 'Sachsen-Anhalt', 'Schleswig-Holstein', 
                        'Thüringen', 'I have German citizenship and live abroad', 'None of the above']
        }

class EndPage(Page):
    template_name = 'global/EndPage.html'

# Define the sequence of pages to show
page_sequence = [
    WelcomePage,
    PolicyIssuePage,        # policy issue question (open text)
    VotingDecisionPage,     # voting decision question (multiple-choice)
    NumericQuestionPage,    # age question (numeric)
    GenderQuestionPage,     # gender question (multiple-choice)
    RegionQuestionPage,     # region question (multiple-choice)
    EndPage
]
