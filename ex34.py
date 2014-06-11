# I'm lazy and already know about ordinal vs. cardinal numbers (advanced logic @ uni) so just running through this task fast.
print "\nLoad in arbritary list of animals."
print "\nStart index calls...\n"
animals = ['bear','python','peacock','kangaroo','whale','platypus']
# 1. The animal at 1.
print animals[1]
# 2. The third [3rd) animal.
print animals[2]
# 3. The first [1st] animal.
print animals[0]
# 4. The animal at 3.
print animals[3]
# 5. The fifith [5th] animal.
print animals[4]
# 6. The animal at 2.
print animals[2]
# 7. The sixth [6th] animal.
print animals[5]
# 8. The animal at 4.
print animals[4]

print "\nDone!"
# Lists use a cardinal nubmering system i.e. starts at 0. This is because
# one can call on any element of a list arbritarily without having to go
# through the previous elements, like a magician picking cards out of a
# deck.
#
# A rule of thumb from converting from ordinal to cardinal is simply to
# minus 1 (-1) from the ordinal number to get the cardinal index of 
# an element in a list.