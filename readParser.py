import json
f = open('./read.txt')
lines = f.readlines()
bookObjs = []
bookObj = []
composite_list = [lines[x:x+12] for x in range(0, len(lines),12)]
objList = []
for x in composite_list:
    obj = {
        "Title": x[1].replace('\n', '').replace(u"\u2018", "'").replace(u"\u2019", "'"),
        "Author": x[2].replace('\n', '').replace(u"\u2018", "'").replace(u"\u2019", "'").replace(" *", ""),
        "Read Date": x[7].replace('\n', '').replace('not set', '').replace(' [edit]', ''),
        "Owned": True,
        "Read": x[7] != 'not set [edit]\n'
    }
    if "bookcase" not in x[5]:
        objList.append(obj)
with open('./read.json', 'w') as f:
    json.dump(objList, f, ensure_ascii=False, indent=4)