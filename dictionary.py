
# user = { 
#     'name' : 'gopal',
#     'age' : 26,
#     'school' : ['vvm','nktt'],
#     'place' : ['thane','mumbai'],
#     }

# print(user['school'])

##### print cube of no.

# def cube_no(a):
#     cu_be = {}
#     for i in range(1,a+1):
#         cu_be[i] = i**3
#     return cu_be


# n = int(input('enter no. : '))
# print(cube_no(n))

####### word counter 122

# def word_counter(s):
#     count = {}
#     for i in s:
#         count[i] = s.count(i)
#     return count
# print(word_counter('python programming'))

###### print dictionary via user input

# user = {}

# name = input("enter name: ")
# age = int(input("enter age: "))
# fav_movies = input("enter movies saperated by , : ").split(',')
# fav_songs = input('enter songs saperated by comma: ').split(',')

# user['name'] = name
# user['age'] = age
# user['fav_movies'] = fav_movies
# user['fav_songs']= fav_songs

# for i,j in user.items():
#     print(f'{i} : {j}')