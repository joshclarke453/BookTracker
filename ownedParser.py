import json
f = open('./owned.txt', encoding='utf-8')
lines = f.readlines()
bookObjs = []
bookObj = []
composite_list = [lines[x:x+12] for x in range(0, len(lines),12)]
objList = []
for x in composite_list:
    obj = {
        "Title": x[1].replace('\n', ''),
        "Author": x[2].replace('\n', ''),
        "Read Date": x[7].replace('\n', '').replace('not set', '').replace(' [edit]', ''),
        "Owned": True,
        "Read": x[7] != 'not set [edit]\n'
    }
    if obj['Read'] != True:
        objList.append(obj)
with open('./owned.json', 'w', encoding='utf-8') as f:
    json.dump(objList, f, ensure_ascii=False, indent=4)