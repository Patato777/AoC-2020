from numpy import array,copy,concatenate,count_nonzero

table = list()
with open('../inputs/AoC2020-11.txt','r') as f :
    for line in f :
        table.append(list(line[:-1]))

arr = array(table)
border_s = array([['.']]*len(arr))
border_u = array([['.']*(len(arr[0])+2)])
arr = concatenate((concatenate((border_s,arr),1),border_s),1)
arr = concatenate((concatenate((border_u,arr)),border_u))

count = array([[0]*len(arr[0])]*len(arr))
adj = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
first = True

while first or not (arr == prev_arr).all() :
    first = False
    prev_arr = copy(arr)
    work_arr = copy(arr)
    work_count = copy(count)
    for k in range(1,len(arr)-1) :
        for j in range(1,len(arr[0])-1) :
            if arr[k,j] == 'L' and count[k,j] == 0 :
                work_arr[k,j] = '#'
                for a in adj :
                    work_count[k+a[0],j+a[1]] += 1
            if arr[k,j] == '#' and count[k,j] >= 4 :
                work_arr[k,j] = 'L'
                for a in adj :
                    work_count[k+a[0],j+a[1]] -= 1
    arr = copy(work_arr)
    count = copy(work_count)

print(count_nonzero(arr=='#'))
