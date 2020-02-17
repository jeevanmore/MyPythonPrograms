n = 6
s = ['0','0','0','0','1','0']
jumps = 0

for cloud in s:
    if cloud == 0:
        jumps += 1
    
print(jumps)        

