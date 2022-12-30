# Input : tuples = [(), (‘ram’,’15’,’8′), (), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”,”),()]
# Output : [(‘ram’, ’15’, ‘8’), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”, ”)]

# Input : tuples = [(”,”,’8′), (), (‘0′, ’00’, ‘000’), (‘birbal’, ”, ’45’), (”), (),  (”,”),()]
# Output : [(”, ”, ‘8’), (‘0′, ’00’, ‘000’), (‘birbal’, ”, ’45’), (”, ”)]



def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples
 
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('',''),()]
print(Remove(tuples))



# using tuple method

def Remove(tuples):
    tuples = filter(None, tuples)
    return tuples
 

tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('',''),()]
print(tuples)