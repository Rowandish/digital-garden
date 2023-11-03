def find_cube_root(n):
    low = 0
    high = n
    while low < high:
       mid = (low+high)//2
       if mid**3 < n:
           low = mid+1
       else:
           high = mid
    print(low)

find_cube_root(2205316413931134031074603746928247799030155221252519872649594750678791181631768977116979076832403970846785672184300449694813635798586699205901153799059293422365185314044451205091048294412538673475392478762390753946407342073522966852394341)