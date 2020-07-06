import re
b = ' aada sfgdrgd dt      fthfth fthfth     fthfh fthfthfth'

# b = re.sub(' +', ' ', b)
b = ' '.join(b.split())

print(b)