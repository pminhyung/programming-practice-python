class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.deleted =[]

    def insert_before(self, data, before_data):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node == None:
                    return False
            new = Node(data)
            before_new = node.prev
            if before_new:
                before_new.next = new
            else:
                self.head = new
            new.next = node
            return True

    def insert_after(self, data, after_data):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.head
            while node.data != after_data:
                node = node.next
                if node == None:
                    return False
            new = Node(data)
            after_new = node.next
            new.next = after_new
            new.prev = node
            node.next = new
            if new.next == None:
                self.tail = new
            return True

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def getat(self, ind):
        curr= self.head
        while curr.data!=ind:
            curr = curr.next
        return curr

    def move(self, curr, cmd1, cmd2):
        if cmd1=='U':
            for _ in range(cmd2):
                curr = curr.prev
        if cmd1 == 'D':
            for _ in range(cmd2):
                curr = curr.next
        return curr

    def delete(self, curr):
        if curr.data == self.head.data:
            self.deleted.append(curr.data)
            curr = self.head.next
            self.head = curr
            self.head.prev = None
            return curr

        if curr.data == self.tail.data:
            self.deleted.append(curr.data)
            curr = self.tail.prev
            self.tail = curr
            self.tail.next = None
            return curr

        # 삭제
        self.deleted.append(curr.data)
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        return curr.next

    def recover(self):
        recdata = self.deleted.pop()
        if recdata == 0:
            self.insert_before(recdata, recdata+1)
            return
        self.insert_after(recdata, recdata - 1)

    def get_result(self, n):
        result = ['O']*n
        for i in self.deleted:
            result[i]='X'
        return ''.join(result)

# N, K = 8,2
# doublelinked = NodeMgmt(0)
# for data in range(1, 8):
#     doublelinked.insert(data)
# currnode = doublelinked.getat(2)
# currnode = doublelinked.move(currnode, 'U', 2)
# currnode = doublelinked.delete(currnode)
#
# print(currnode.data)
# print()
# doublelinked.desc()
# print()
# print(doublelinked.deleted)
# print()
# doublelinked.recover()
# doublelinked.desc()
# print('curr', currnode.data)
n,k = 8,2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
doublelinked = NodeMgmt(0)
for data in range(1, n):
    doublelinked.insert(data)
currnode = doublelinked.getat(k)
print(currnode.data, '\n')
for c in cmd:
    if len(c) == 1:
        if c == 'C':
            # node삭제
            currnode = doublelinked.delete(currnode)
            #print(doublelinked.deleted[-1], currnode.data)
        elif c == 'Z':
            # node 복구
            doublelinked.recover()
    else:
        d, n = c.split()
        # node 이동
        currnode = doublelinked.move(currnode, d, int(n))
    print('명령:', c)
    print('현재:', currnode.data)
    print('삭제노드:', doublelinked.deleted)
    doublelinked.desc()
    print()
print(doublelinked.get_result(8))
# node_mgmt.desc()
# node_mgmt.insert_after(1.5, 1)
# node_mgmt.desc()
