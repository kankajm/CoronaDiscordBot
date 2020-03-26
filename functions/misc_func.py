import os
from sys import platform
# Debug print for a developer to check if he streams data into right client key.
def debug_bot_onstart(bot_name):
    print('DEBUG: Bot name is: ' + str(bot_name))

# Returns value on what system server runs
def system_is():
    if platform == "linux" or platform == "linux2":
        return "Linux"
    elif platform == "darvin":
        return "Mac OS"
    elif platform == "win32":
        return "Windows"