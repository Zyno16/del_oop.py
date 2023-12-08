class test():
     def __init__(self):
         print("new object ")

     def __del__(self):
         print("delete the object")
         

t1 =test()
del t1
