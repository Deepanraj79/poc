import json
import time

data = None

with open("test.json", "r", encoding='utf-8-sig') as read_file:
    data = json.load(read_file)

print('process done')

import pdb; pdb.set_trace()
# json_string = json.dumps(data)

iteration = 0

start = time.time()
for index in range(0, 4000):
    json.dumps(data[index].update({'new_key': 'new_value'}))
    # print(json.dumps(data[index]), '\n')
end = time.time()

# json_object = json.loads(data)


print(end - start)

