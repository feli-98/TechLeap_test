## SECTION 1: Logic & Problem Solving (10 marks)

 # Question 2:

 # Explain how you would optimize a page that loads too slowly. Mention at least three causes and how you’d fix each.
Large images- Resize and compress before uploading to reduce load time. 
Too many CSS/JS files- Combine them into a single HTML file 
No caching- Enable browser caching so pages load faster on repeat visits.


## SECTION 3: Debugging & Reasoning (10 marks)
# Question 5:
 You’ve been given this code snippet:
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    if i % 2 == 0:
        numbers.remove(i)
print(numbers)

# What’s wrong with the code?
The code removes values equal to the index, not the actual elements at even positions. 
Changing the list while iterating through it causing it to skip some numbers.


# What will it output?
[1, 3, 4]


# How would you fix it to remove even numbers correctly?

numbers = [1, 2, 3, 4, 5]
numbers = [n for n in numbers if n % 2 != 0]
print(numbers)



## SECTION 4: Version Control & Collaboration (5 marks)

# Question 6:

 # Explain how you would use Git to collaborate on a team project with other developers.
Clone the repository from GitHub and create my own branch to work on new features. 
After making changes, I’d put in the demands below then the team would review and merge the branch into the main project:
git add .
git commit -m "Added new feature"
git push origin feature-branch

 # Mention at least:
# One common Git command you use often.

git commit -m "...." (To save my work with a clear description.)


# One problem you’ve faced while using Git and how you solved it.

Merge conflicts when pulling updates. 
I solved it by running git pull -- rebase, fixing the conflicts manually and recommitting my changes.
