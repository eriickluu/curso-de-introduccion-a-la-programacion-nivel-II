def resultHanoi(disks, source, middle, destination):
     if disks >= 1:
         resultHanoi(disks-1, source, destination, middle)
         print("Mover disco de torre", source, "a", destination)
         resultHanoi(disks-1, middle, source, destination)

resultHanoi(3, 1, 2, 3)

"""
Página web 
http://pythontutor.com/visualize.html#mode=edit
"""