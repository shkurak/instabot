from InstagramAPI import InstagramAPI
from time import time

class extended_api(InstagramAPI):
    def __init__(self, username, password, random_timestamp_interval = (0,0)):
        super().__init__(username, password)
        self.random_timestamp_interval = random_timestamp_interval
        
    def likeFeedposts(self):
        random_timestamp_interval = self.random_timestamp_interval
        next_is_not_liked = True
        self.getTimeline()
        Jsons = []        
        while next_is_not_liked:
            LastFeedJson = self.LastJson
            Jsons.append(LastFeedJson)
            for i in range(len(LastFeedJson['items'])):
                time.sleep(random.uniform(random_timestamp_interval[0], random_timestamp_interval[1]))
                if 'has_liked' in LastFeedJson['items'][i] and 'ad_action' not in LastFeedJson['items'][i]:
                    if LastFeedJson['items'][i]['has_liked']:
                        print('Post of __ ' + LastFeedJson['items'][i]['user']['username'] + ' __  was liked before')
                        next_is_not_liked = False
                    else:               
                        #print(LastFeedJson['items'][i]['caption']['media_id'])
                        try:
                            self.like(LastFeedJson['items'][i]['id'])
                        except:
                            print(i, len(Jsons), 'Not liked')
                        else:
                            print('Liked post of __ ' + LastFeedJson['items'][i]['user']['username'] + ' __')
                else:
                    print(i, len(Jsons), "It's not a post")
            if next_is_not_liked:
                print('   ')
                print('Loud next Json')
                self.SendRequest('feed/timeline/'+ '?max_id=' + LastFeedJson['next_max_id'] + '/?rank_token='+ str(self.rank_token) +'&ranked_content=true&')
        
        print('\nSuccessful')
        return Jsons