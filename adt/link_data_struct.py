# -*- coding: utf-8 -*-


# 实现一个链表的数据结构，同java中的LinkedList
# 链表的节点
class Node:
    def __init__(self, data, prev, next):
        self.next = next
        self.prev = prev
        self.data = data

    def show(self):
        print(self.data)


class LinkList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    # 遍历链表
    def show(self):
        current = self.first
        while current is not None:
            print current.data,
            current = current.next

    # 是否为空
    def is_empty(self):
        return True if self.first is None else False

    # 插入到最后
    def insert(self, data):
        self._insert_to_last(data=data)
        return True

    # 同上,链表结构默认就是插入到最后一个位置
    def insert_last(self, data):
        self._insert_to_last(data=data)
        return True

    # 插入到第一个位置
    def insert_first(self, data):
        self._insert_to_first(data=data)
        return True

    # 实现这个方法
    def insert_all(self, data, index):
        self._check_position(index)
        current = self.last
        for value in data:
            pass

    # 插入到某个角标的位置
    def insert_to_index(self, data, index):
        self._check_position(index)
        self._insert_before(data, index)
        return True

    # 检查某个角标是否合理
    def _check_position(self, index):
        if index > self.size or index < 1:
            raise Exception

    # 寻找某个角标的值
    def _node(self, index):
        result = None
        if index < self.size >> 1:
            result = self.first
            for i in range(1, index):
                result = result.next
        else:
            result = self.last
            for i in range(self.size, index, -1):
                result = result.prev
        return result

    # 插入到最后的实际执行方法
    def _insert_to_last(self, data):
        l = self.last  # 先获取最后一个元素
        new_node = Node(data, l, None)
        self.last = new_node

        if l is None:  # 如果最后节点为空，说明链表为空
            self.first = new_node
        else:
            l.next = new_node

        self.size += 1

    def _insert_to_first(self, data):
        f = self.first
        new_node = Node(data, None, f)
        self.first = new_node
        if f is None:
            self.last = new_node
        else:
            f.prev = new_node

        self.size += 1

    # 查到某个值的前面
    def _insert_before(self, data, index):
        before_node = self._node(index)
        temp_node = before_node.prev
        new_node = Node(data, temp_node, before_node)
        before_node.prev = new_node

        if temp_node is None:
            self.first = new_node
        else:
            temp_node.next = new_node

        self.size += 1

if __name__ == "__main__":
    link_list = LinkList()
    link_list.insert_first(12)
    link_list.insert(13)

    link_list.insert(14)
    link_list.insert_first(15)
    link_list.show()

    print(link_list.insert_to_index(11111, 1))

    link_list.show()
