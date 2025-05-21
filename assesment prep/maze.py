

list = [
       [0,1,2,3,4,5],
       [0,1,2,3,4,5],
       [0,1,2,3,4,5],
       [0,1,2,3,4,5],
       [0,1,2,3,4,5]
]

for row in list:
    for col in row:
        print(col)
    
print ("*******")


#difference in brackets between hashtable and arrray

rows=(3)
cols=(4)
num = [[0]*cols]*rows
print(num[2])

word = "Test"
total = 0
for i in range (0,len(word)):
    total = total + 1
print(total)
    
    

hash_person= {
    "name": "Lachy",
    "age" : "25",   
    
    
}
print(hash_person["name"]) 