def sub_heapify(x, n, i_root):
    i_left = 2 * i_root + 1
    i_right = 2 * i_root + 2
    i_max = i_root
    if i_left < n and x[i_root] < x[i_left]:
        # left child is greater
        i_max = i_left
    if i_right < n and x[i_max] < x[i_right]:
        # right child is greater
        i_max = i_right
    if i_max != i_root:
        x[i_root], x[i_max] = x[i_max], x[i_root]
        sub_heapify(x, n, i_max)

def heapify(x):
    END = len(x)
    for k in range(END // 2 - 1, -1, -1):
        sub_heapify(x, END, k)

def push(x, e):
    x.append(e)
    heapify(x)

def popmax(x):
    e = x.pop(0)
    heapify(x)
    return e