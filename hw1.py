# 1. Write a function count_vowels(word) that takes a word as an argument and returns the number of vowels in the word

def count_vowels(word):
  count=0;
  for letter in word:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
      count+=1;
  return count;


print(count_vowels("academics"));




# 2. Iterate through the following list of animals and print each one in all caps.

animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther'];
for animal in animals:
  animalCaps = animal.upper();
  print(animalCaps);



# 3. Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.

for i in range(20):
  if((i+1) % 2 == 0):
    print(str(i+1) + ": Even")
  else:
    print(str(i+1) + ": Odd")


# 4. Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.

def sum_of_integers(a,b):
  sum = int(a) + int(b);
  return sum;

num1 = input("Enter number 1: ");
num2 = input("Enter number 2: ");
print(sum_of_integers(num1, num2));


