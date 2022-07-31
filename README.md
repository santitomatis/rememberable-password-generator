# Rememberable Password Generator
This is a project similar to my [previous one](https://github.com/santitomatis/password-generator) (just a password generator) but this time I want the password that is created to be easier to remember, that's why this generator provides you a combination of nouns that you can remeber.

## Disclaimer
**Please be aware that as [mentioned later on](https://github.com/santitomatis/rememberable-password-generator#what-i-learned), this is just a project made to help me learn some python, even doe it does work, if someone somehow knew that you used this script to generate your password *specially with the default settings* that person could just brute force your password**

## Demo
When you run this script you are going to be asked wether you like to configure advanced stuff or just go by default

```
Welcome to The Rememberable Password Generator Project
Do you want to do some advanced configuration? Just type y/n (yes or no)
```

If you type n, a random password is going to be generated for you

```
Do you want to do some advanced configuration? Just type y/n (yes or no) n
Your password is:
archives sidewalk objective
Remember that this password is case-senstive (if you copy and paste it, you're going to have to remember if it was uppercase, capitalized, etc the next time you log in)
```

In the other hand if you type y, the amount of words it has among other details are going to be custom

```
Do you want to do some advanced configuration? Just type y/n (yes or no) y
How many words do you want your password to have? (recommended: 3) 5
Do you want to separate the words with a random char (eg: _ ; -)? Just type y/n (yes or no) Words will be separated with spaces by default y

                Do you want your password to be:
                -uc (uppercase)
                -lc (lowercase)
                -c (capitalized)
                -r (random)
                (Just type uc; lc; c or r according to your choice)
                uc
Your password is:
WOK+RIP+GRANDDAUGHTER+SPIDER+JELLYFISH
Remember that this password is case-senstive (if you copy and paste it, you're going to have to remember if it was uppercase, capitalized, etc the next time you log in)
```

*That's pretty much all there is to its functionality*

## What I learned
I've learned a lot with this project, *mostly basic things but those things had to be learn a way or another*

- How to transform a .txt file to an array with pandas
- How to install pandas in WSL2

There are also some thing I already knew but this project gave me a deeper understanding
- Arrays and tuplas
- string manipulation methods (upper() lower(), capitalize())

As [mentioned before](https://github.com/santitomatis/rememberable-password-generator#disclaimer), this is just a better version of the [regular password generator](https://github.com/santitomatis/password-generator) shown at a [Platzi course](https://platzi.com/cursos/python/)


![certificadoCursoBasicoPython](https://user-images.githubusercontent.com/86212669/176564841-410e78cf-518f-4fe3-bb7b-a338679657e8.png)



