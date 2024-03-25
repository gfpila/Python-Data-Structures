"""You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)"""

#1
heroes = ['spider man','thor','hulk','iron man','captain america']
print(f"My list of heroes has {len(heroes)} heros.")

#2
heroes.append('black panther')
print(f"I added {heroes[-1]} to my list now it is {heroes}.")

#3
heroes.pop()
heroes.insert(3, 'black panther')
print(f"I reordered my list now it is {heroes}")

#4
heroes = [heroes[0]] + ['doctor strange'] + heroes[3:]
print(f"I changed my list to {heroes}")

#5
heroes.sort()
print(f"This is my list in alphabetical order {heroes}")