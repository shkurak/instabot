from InstagramAPI import InstagramAPI
from extended_api import extended_api
import sys
import json
import time
import random


project_folder = '/home/shkiv/prog/instabot/'
log_folder = '/var/log/'


with open(project_folder + 'login_pass.txt', 'r') as file:
    data = file.read().split('\n')
    user = data[0]
    pwd = data[1]

interval = (15000, 20000)

while True:
    
    Inst = extended_api(user, pwd, random_timestamp_interval = (1, 15))
    
    old_stdout = sys.stdout
    sys.stdout = open(log_folder + "instabot_stdout.log", "a")
    file_for_jsons = open(log_folder + "instabot_jsons.log", "a")
    print('\nStart session ' + time.ctime()+ '\n')



    Inst.login()



    Jsons = Inst.likeFeedposts()
    file_for_jsons.write('\nStart session ' + time.ctime()+ '\n')
    for j in Jsons:
        json.dump(j,file_for_jsons)
        file_for_jsons.write('\n')
        
        
    file_for_jsons.write('\nEnd session ' + time.ctime() + '\n')

    Inst.logout()

    print('\nEnd session ' + time.ctime() + '\n')

    
    
    time_to_sleep = random.uniform(interval[0], interval[1])
    print('Next session in ', time_to_sleep, ' sec   That mean in ', time_to_sleep/3600, ' hours')
    
    file_for_jsons.close()
    sys.stdout = old_stdout
    time.sleep(time_to_sleep)
    