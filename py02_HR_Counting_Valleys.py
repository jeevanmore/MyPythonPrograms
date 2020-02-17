# s = ["U","D","D","D","U","D","U","U"]
n = 12
s = ['D','D','U','U','D','D','U','D','U','U','U','D']
level = 0
valleys = 0

for step in s:
    if step == 'U':
        level += 1
        if level == 0:
            valleys += 1
    else:
        level -=1
print(valleys)        

