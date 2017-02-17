
class Node:
    value = 0
    ptr = None
    def __init__(self, value=0):
        self.value = value
        self.ptr = None
        return

def init_list(array):
    cur = head = None
    is_set_head = False
    for item in array:
        nd = Node(item)

        if not is_set_head:
            cur = head = nd
            is_set_head = True
            continue

        cur.ptr = nd
        cur = nd
    return head

def print_list(l):
    out = ''
    while l:
        out += '%d, ' % l.value
        l = l.ptr
    print(out)
    return

def reverse_list(sublist):
    i = len(sublist) - 1
    head = sublist[-1]
    tail = sublist[0]
    while i > 0:
        sublist[i].ptr = sublist[i-1]
        i -= 1 
    return head, tail
    
def reverse_list_k(l, k):
    cur_head = final_head =  None
    is_set_head = False
    sublist = []
    while l:
        if len(sublist) < k:
            sublist.append(l)
            l = l.ptr
        elif len(sublist) == k:
            sub_head, sub_tail = reverse_list(sublist)
            #print('h - %d, t - %d' % (sub_head.value, sub_tail.value))

            if not is_set_head:
                final_head = sub_head
                is_set_head = True
                cur_head = sub_tail
                cur_head.ptr = None
                continue
            else:
                cur_head.ptr = sub_head
                cur_head = sub_tail
                cur_head.ptr = None
                sublist = []
                #print_list(final_head)
                continue
            
    if len(sublist) < k:
        for item in sublist:
            cur_head.ptr = item
            cur_head = item
    return final_head
    

if __name__ == '__main__':

    #l = init_list([1,2,3,4,5,6,7,8])
    l = init_list([3,2,6,3,2,9,8])
    print_list(l)
    b = reverse_list_k(l, 3)
    print_list(b)
