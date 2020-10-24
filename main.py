# create 2 dects
# add them into one list
#loop through the new list

user1 = {'username':'nour', 'age':'24','id':1}
user2 = {'username':'sara', 'age':'23', 'email':'n@g.com', 'id':2}

my_users = [user1,user2]
print(my_users)

# for user in my_users:
  # print(user['email'])

# the example above , it will not find the email because it looks for it in the first dict
# using conditions will do the trick , conditions are true false statement.

for user in my_users:
  if 'email' in user:
    print (user['email'])

#looping inside a loop:
selected_user = {}
my_user_loockup = 2
for user in my_users:
  if 'id' in user:
    if user['id'] == my_user_loockup:
      selected_user = user
print(selected_user)

# or going ilke this:
selected_user = {}
my_user_loockup = 2
for user in my_users:
  if 'id' in user and user['id'] == my_user_loockup:
    selected_user = user
print(selected_user)

# or going ilke this:
selected_user = {}
my_user_loockup = 2
for user in my_users:
  # if one of our dict has no id this loop will break and through an error
  if user['id'] == my_user_loockup:
    selected_user = user
print(selected_user)