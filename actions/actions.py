# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Dict, Text, Any, List, Union

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from db_sqlite import insert_data3, insert_data2

class ValidateHealthForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_survey_form"

    async def validate_survey(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if value:
            return {"confirm_survey": True}
        else:
            return {"confirm_survey": False }

class ActionSubmitSurvey(Action):
    def name(self) -> Text:
        return "action_submit_results"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

            feel_down = tracker.get_slot("feel_down")
            litte_interest = tracker.get_slot("litte_interest")
            bother_sleep = tracker.get_slot("bother_sleep")
            bother_tired = tracker.get_slot("bother_tired")
            bother_apetite = tracker.get_slot("bother_apetite")
            bother_feelingbad = tracker.get_slot("bother_feelingbad")
            bother_concentrate = tracker.get_slot("bother_concentrate")
            bother_moving = tracker.get_slot("bother_moving")
            bother_anxiety = tracker.get_slot("bother_anxiety")
            bother_nervous = tracker.get_slot("bother_nervous")
            bother_worry = tracker.get_slot("bother_worry")
            bother_worry_things = tracker.get_slot("bother_worry_things")
            bother_relax = tracker.get_slot("bother_relax")
            bother_restless = tracker.get_slot("bother_restless")
            bother_annoy = tracker.get_slot("bother_annoy")
            bother_afraid = tracker.get_slot("bother_afraid")
            # dispatcher.utter_message(text="Thank you so much for your time!")
            insert_data3(feel_down,litte_interest,bother_sleep,bother_tired,bother_apetite,bother_feelingbad,bother_concentrate,bother_moving,bother_anxiety,bother_nervous,bother_worry,bother_worry_things,bother_relax,bother_restless,bother_annoy,bother_afraid)	
            return []


class ValidateActualForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_mhsurvey_form"

    async def validate_mhsurvey(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if value:
            return {"confirm_mhsurvey": True}
        else:
            return {"confirm_mhsurvey": False }

class ActionSubmitMHSurvey(Action):
    def name(self) -> Text:
        return "action_submit_mhresults"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

            self_empl_flag  = tracker.get_slot("self_empl_flag")
            tech_comp_flag  = tracker.get_slot("tech_comp_flag")
            mh_coverage_flag    = tracker.get_slot("mh_coverage_flag")
            mh_employer_discussion  = tracker.get_slot("mh_employer_discussion")
            mh_resources_provided   = tracker.get_slot("mh_resources_provided")
            mh_anonimity_flag   = tracker.get_slot("mh_anonimity_flag")
            mh_medical_leave    = tracker.get_slot("mh_medical_leave")
            mh_discussion_neg_impact    = tracker.get_slot("mh_discussion_neg_impact")
            mh_discussion_cowork    = tracker.get_slot("mh_discussion_cowork")
            mh_discussion_supervis  = tracker.get_slot("mh_discussion_supervis")
            mh_conseq_coworkers = tracker.get_slot("mh_conseq_coworkers")
            mh_hurt_on_career   = tracker.get_slot("mh_hurt_on_career")
            mh_neg_view_cowork  = tracker.get_slot("mh_neg_view_cowork")
            mh_bad_response_workplace   = tracker.get_slot("mh_bad_response_workplace")
            mh_family_hist  = tracker.get_slot("mh_family_hist")
            mh_disorder_past    = tracker.get_slot("mh_disorder_past")
            mh_disorder_current = tracker.get_slot("mh_disorder_current")
            mh_diagnos_proffesional = tracker.get_slot("mh_diagnos_proffesional")
            mh_sought_proffes_treatm    = tracker.get_slot("mh_sought_proffes_treatm")
            mh_eff_treat_impact_on_work = tracker.get_slot("mh_eff_treat_impact_on_work")
            mh_not_eff_treat_impact_on_work = tracker.get_slot("mh_not_eff_treat_impact_on_work")
            age = tracker.get_slot("age")
            sex = tracker.get_slot("sex")
            country_live    = tracker.get_slot("country_live")
            live_us_teritory    = tracker.get_slot("live_us_teritory")
            country_work    = tracker.get_slot("country_work")
            work_us_teritory    = tracker.get_slot("work_us_teritory")
            work_position   = tracker.get_slot("work_position")
            remote_flag = tracker.get_slot("remote_flag")


            # dispatcher.utter_message(text="Thank you so much for your time!")
            insert_data2(self_empl_flag, tech_comp_flag, mh_coverage_flag, mh_employer_discussion, mh_resources_provided, mh_anonimity_flag, mh_medical_leave, mh_discussion_neg_impact, mh_discussion_cowork, mh_discussion_supervis, mh_conseq_coworkers, mh_hurt_on_career, mh_neg_view_cowork, mh_bad_response_workplace, mh_family_hist, mh_disorder_past, mh_disorder_current, mh_diagnos_proffesional, mh_sought_proffes_treatm, mh_eff_treat_impact_on_work, mh_not_eff_treat_impact_on_work, age, sex, country_live, live_us_teritory, country_work, work_us_teritory, work_position, remote_flag)	
            return []
