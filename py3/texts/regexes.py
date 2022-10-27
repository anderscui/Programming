import re

RE_DATE_FUNC = re.compile(r'(?P<func>GetDate_(Day|Mon))\(\s*(?P<param>-?\d{1,3})?\s*\)', re.U | re.I)

s = 'select * from abc where abc.date = GetDate_Day()'
m = RE_DATE_FUNC.search(s)
print(s)
print(f"match: {m.group(0)}, func: {m.group('func')}, param: {m.group('param')}")

print(RE_DATE_FUNC.sub("'20211012'", s))

s = 'select * from abc where abc.date = GetDate_Day(-1)'
m = RE_DATE_FUNC.search(s)
print(s)
print(f"match: {m.group(0)}, func: {m.group('func')}, param: {m.group('param')}")

s = 'select * from abc where abc.date = GetDate_Mon( 100 )'
m = RE_DATE_FUNC.search(s)
print(s)
print(f"match: {m.group(0)}, func: {m.group('func')}, param: {m.group('param')}")

s = 'select * from abc a where a.date1 = GetDate_Day() and a.date2=GetDate_Day(-1) and a.mon1=GetDate_Mon() and a.mon2=GetDate_Mon(-1)'
matches = RE_DATE_FUNC.finditer(s)
for m in matches:
    print(m)
