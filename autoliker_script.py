from InstagramAPI import InstagramAPI
import sys
import json
import time
import random




user = ''
pwd = ''

interval = (15000, 20000)

while True:
    
    Inst = InstagramAPI(user,pwd)
    
    old_stdout = sys.stdout
    sys.stdout = open("stdout_log.txt", "a")
    file_for_jsons = open("jsons_log.txt", "a")
    print('\nStart session ' + time.ctime()+ '\n')



    Inst.login()



    Jsons = Inst.likeFeedposts(random_timestamp_interval = (1, 15))
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
    