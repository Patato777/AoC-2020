import re

pattern = re.compile(r'(?<=mem\[)(\d+)\] = (\d+)')
values = dict()

def floating(adr) :
    if 'X' in adr :
        ind = adr.index('X')
        ad1,ad2 = adr.copy(),adr.copy()
        ad1[ind],ad2[ind] = '0','1'
        return floating(ad1)+floating(ad2)
    return [adr.copy()]

with open('../inputs/AoC2020-14.txt','r') as file :
    for line in file :
        if line.startswith('mask') :
            exec(line.replace('= ','= "').replace('\n','"'))
        else :
            m = pattern.search(line)
            adress,value = int(m.group(1)),int(m.group(2))
            bin_adr = list(bin(adress)[2:].zfill(36))
            for k,bit in enumerate(mask) :
                if bit != '0' :
                    bin_adr[k] = bit
            for adr in floating(bin_adr) :
                new_adr = int(''.join(adr),2)
                values[new_adr] = value

print(sum(values.values()))
