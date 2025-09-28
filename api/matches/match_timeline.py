from api.matches.timeline_models import LolMatchV5MatchTimeline
class Timeline:
    def __init__(self, riot_client, match_id):
        self.riot_client = riot_client
        self.match_id = match_id
        self.match_timeline = self.riot_client.get_match_timeline_data(self.match_id)
        self.match_timeline = LolMatchV5MatchTimeline.model_validate(self.match_timeline)
        #TODO:  methods to parse timeline data more specifically
    
    def get_events_between(self, start_minute: int, end_minute: int):
        pass
    def get_participant_frames_between(self, participant_id: int, start_minute: int, end_minute: int):
        pass
    def get_participant_frame_at(self, participant_id: int, minute: int):
        pass
    def get_events_at(self, minute: int):
        pass
    def get_events_of_type(self, event_type: str):
        pass

    
