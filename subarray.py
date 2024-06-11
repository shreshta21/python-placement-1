def large_array(list):
    max_sum=cur_sum=list[0]
    for i in  list[1:]:
        cur_sum=max(i,cur_sum+i)
        max_sum=max(max_sum,cur_sum)
    return max_sum

list=[-2,1,-3,4,-1,2,1,-5,4]
print(large_array(list))