import os
from postmark import PMMail


def send_reward_email(**kwargs):
    message = PMMail(api_key=os.environ.get('POSTMARK_API_KEY'),
                     subject="Your reward from Obi",
                     sender="shill@taluslabs.com",
                     **kwargs)
    message.send()