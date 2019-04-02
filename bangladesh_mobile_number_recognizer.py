import re

numbers  = '''
(+88)-01711309967
(+88)-0171-1309967
(+88)-0171-130-9967
(+880)-1711309967
(+880)-171-1309967
(+880)-171-130-9967
+88-01711309967
+88-0171-1309967
+88-0171-130-9967
+880-1711309967
+880-171-1309967
+880-171-130-9967
+8801711309967
01711309967
8801711309967
88-01711309967
88-0171-1309967
88-0171-130-9967
880-1711309967
880-171-1309967
880-171-130-9967
0171-1309967
0171-130-9967
01711-309969
'''

r = re.compile(r"\(?\+?[8]{2}?0?\)?\0?-?0?[0-9]{3}-?[0-9]{3}-?[0-9]{4}|[0-9]{4}-?[0-9]{3}-?[0-9]{4}|[0-9]{5}-[0-9]{6}")
found_numbers = r.findall(numbers)
print(found_numbers)
