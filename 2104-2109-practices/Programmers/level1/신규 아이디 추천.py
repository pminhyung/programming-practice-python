import re
def solution(new_id):
    id = new_id.lower()
    id = re.sub('[^a-z0-9\-_\.]',"", id)
    while '..' in id:
        id = re.sub('\.{2}','.', id)
    if id.startswith('.'):
        id = id[1:]
    if id.endswith('.'):
        id = id[:-1]
    if id=='':
        id = 'a'
    if len(id)>=16:
        id = id[:15]
    if id.endswith('.'):
        id= id[:-1]
    if len(id)<=2:
        while len(id)!=3:
            id+=id[-1]
    return id