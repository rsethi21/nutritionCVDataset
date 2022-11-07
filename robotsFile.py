import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url('https://www.allrecipes.com/robots.txt')
rp.read()
rrate = rp.request_rate("*")
# print(f"{rrate.requests} requests/{rrate.seconds} seconds")
# print(f"{rp/crawl_delay} seconds")
print(rp.can_fetch("*", "https://www.allrecipes.com/recipes/732/us-recipes/amish-and-mennonite/"))
print(rp.can_fetch("*", "https://www.allrecipes.com/recipe/51013/baked-oatmeal-ii/"))
