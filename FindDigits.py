#name =open("/tmp/String.txt")
#s=name.read()
#res=""
#if i in name:
#   if name.isdigit(i):
#        print(str[i])
#        i+=1
#open file and read strings in it
with open('/tmp/String.txt') as f:
    s=f.read()
    res=""
    #cycle every char of strings and judge if it is digit
    for char in s:
        if char.isdigit():
            res+=char
    print(res)

