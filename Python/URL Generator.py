#lets begin

import random
import urllib.parse



protocol = "https://"
path = "path/to/resource"
query_params = {"param1": "value1", "param2": "value2"}

generate_domain = "".join(random.choice("abcdefghijklmnopqrstuvwxyz")for _ in range(9))
domain = generate_domain + ".com/"

url= protocol + domain + path

url += "?" + urllib.parse.urlencode(query_params)

print(url)