from instabot import manager
from instabot import param_getter

params = param_getter()

agent = manager.create_agent(params['agent'])

while agent.running:

    agent.act()
