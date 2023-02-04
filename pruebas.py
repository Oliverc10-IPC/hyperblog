file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

file = open("filename.txt", "r")
for i in range(21):
  
  print(file.readlines())
  
file.close()
try:
  print(1)
  assert 2 + 2 == 5
except AssertionError:
  print(3)
except:
  print(4)


a="Harry Potter/nComercio formal"
print(a)
a.replace("/n","")
print(a)

sqs=[0,1,4,9,16,25,36,49,64]
print(sqs[4:7])

nums = [i*2 for i in range(10)]
print(nums)