# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['Ron', 'Roy', 'Will', 'John']

# simple for loop
# for person in people:
#     print('Current person: ', person)


# break out
# for person in people:
    # print('Current person: ', person)
    # if person == 'Will':
    #     break
    # print('Current person: ', person)

# continue
# for person in people:
#     if person == 'Ron':
#         continue
#     print('Current person: ', person)

# range
# for i in range(len(people)):
#     print('Current person: ', people[i])
 
# for i in range(0, 10):
#     print('Number ', i)



# While loops execute a set of statements as long as a condition is true.

count = 0
while count <=10:
    print('Count ', count)
    count +=1
