from projects.class_project1 import Perfect, Stunning

user = Perfect('bakhtiyor', 'parpiboev')
user2 = Perfect('baiysh', 'zhalalov')
user3 = Perfect('ismoil','shamsiddinov')
user.add_students('alfie brather','umar jumavoy')
user.add_students('baiysh zhalalov', 'aunthet')
print(user.get_students())
#dir(user)

print(user.HowManyTimes())
print(Perfect.totalNumberOfUsingThisCode)

use = Stunning('parpiboev','bakhtiyor',2003,'uzbek')
print(use)