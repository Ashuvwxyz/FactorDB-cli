#! /bin/python3

import sys
from pathlib import Path
import requests

args_count = len(sys.argv)
url = "http://factordb.com/?query="
url2 = "http://factordb.com/index.php?id="

d = {'C':"Composite, no known factors",'CF':"Composite, factors known",'FF':'Fully Factored','P':"Definitely Prime",'Prp':"Probably Prime",'U':"Unknown"}

if args_count < 2 or args_count > 3:
    print("USAGE : factordb <--check (optional)> <number>")
    exit()

if args_count == 3 and sys.argv[1] != '--check':
    print("USAGE : factordb <--check (optional)> <number>")
    exit()

else:
    num = str(sys.argv[args_count-1])
    use = url+num

    try:
        r = (requests.get(use))
        if r.status_code != 200:
            print("Error. Please try again.")
            exit()

        op = r.text.split('<td>')[3].split('</td>')[0]
        if op[-1] != '>':
            loop = int(op.split('^')[-1])
            op = op[:op.rfind('^')-1]
        else:
            loop = 0
        op = op.split(' = ')[1]
        vals = op.split(' &middot; ')
        ans = []

        for strr in vals:
            num = strr.split('#')[1][8:].split('<')[0]
            id = strr.split('id=')[1].split('"')[0]

            if num == id:
                ans.append(int(num))
            else:
                x = num.split('^')
                x.append('1')
                if '...' in x[0]:
                    x[0] = (requests.get(url2+id).text).split('name="query" value="')[1].split('"')[0]

                for v in range(int(x[1])):
                    ans.append(int(x[0]))
        
        if loop:
            for j in range((loop)-1):
                ans += ans
        
        ans.sort()

        status = (r.text.split('<tr><td>')[1].split('<')[0]).rstrip('*')

        if status == 'P':
            ans = (list(set(ans)))
        
        print()
        
        if sys.argv[1] == '--check':
            print(status,":",d[status])
        print(ans)
    
    except:
        print("Error encountered.  Please check input.")
        exit()
    
    

    