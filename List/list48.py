# 1. Length of the list
hero = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
print(len(hero))

# 2. Add 'black panther' at the end of this list
hero = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
hero.append("black panther")
print(hero)

# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
hero = ['spider man', 'thor', 'hulk', 'iron man', 'captain america', 'black panther']
hero.remove("black panther")
hero.insert(3, "black panther")
print(hero)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
hero = ['spider man', 'thor', 'hulk', 'iron man', 'captain america', 'black panther']
hero.remove("thor")
hero.remove("hulk")
hero.insert(1, 'doctor strange')
print(hero)
