# here is my notebook about basic python command ; 

a = "0123456"
a[::2] # output: 0246
a[5] # output: 4

b = "Hello bob how are you ? "

b.upper() # output: HELLO BOB HOW ARE YOU ?
b.find("bob") #output: 7
b[:1] # output: e
b[1:5:2] #output: "el "
b.replace("bob", "marry") #output: hello marry how are you ?

c = "123\nabc" #output : 123
              #          abc

Rating = (0,6,4,7,3,1,9,8,10)
RatingSorted = sorted(Rating) #output (0,1,3,4,6,7,8,9,10)

list = [1,b,[a,b]]

list.extend[1,2] # output: [1,b,[a,b],1,2]
list.append[1,2] #output: [1,b,[a,b],[1,2]]
list[0]= 2 #output: [2,b,[a,b]]
del(list[2]) = #output: [1,b]

"Hard Rock".split() #output:["Hard","Rock"]
