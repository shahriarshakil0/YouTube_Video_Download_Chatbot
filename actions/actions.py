# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from pytube import YouTube


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "youtube_video"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            url = tracker.get_slot('url')
            my_video = YouTube(url)
            title = my_video.title
            my_video = my_video.streams.get_highest_resolution()
            my_video.download()
            dispatcher.utter_message(f'your video title is "{title}" \n Dowload Completed')

        except Exception:
            dispatcher.utter_message(f'your video title is "{title}" \n Dowload Completed')

        return []

from rasa_sdk.events import AllSlotsReset

class ActionHelloWorld(Action):

     def name(self) -> Text:
            return "action_another"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message("Want to download another video")

         return [AllSlotsReset()]