import re

pattern = re.compile(r'(?<=mem\[)(\d+)\] = (\d+)')
mem = list()

with open('../inputs/AoC2020-14.txt','r') as file :
    for line in file :
        if line.startswith('mask') :
            exec(line.replace('= ','= "').replace('\n','"'))
        else :
            m = pattern.search(line)
            adress,value = int(m.group(1)),int(m.group(2))
            bin_val = list(bin(value)[2:].zfill(36))
            for k,bit in enumerate(mask) :
                if bit != 'X' :
                    bin_val[k] = bit
            if len(mem) <= adress :
                mem.extend([0]*(adress-len(mem)+1))
            mem[adress] = int(''.join(bin_val),2)

print(sum(mem))
            
            
