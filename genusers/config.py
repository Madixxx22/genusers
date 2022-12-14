import os
from environs import Env

env = Env()
env.read_env(".env")
SMS_KEY = env.str("SMS_KEY")