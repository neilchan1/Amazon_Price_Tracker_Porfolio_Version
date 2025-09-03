# PSEUDOCODE: Fetcher
#
# Responsibilities:
# - Perform HTTP GET to product page
#
# Example (pseudocode only):
#
# class Fetcher:
#     def __init__(self, proxies=None, user_agents=None):
#         ...
#
#     async def get_html(self, url):
#         1) choose headers and proxy
#         2) perform HTTP GET with timeout
#         3) detect captcha / block and raise specific exception
#         4) return html content
#         
#
