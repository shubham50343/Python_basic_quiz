
def python_quiz():
    return [
        {
            "question": "What is the correct file extension for Python files?",
            "options": ["A) .pyth", "B) .pt", "C) .pyt", "D) .py"],
            "answer": "D",
            "explanation": "Python files use the .py extension."
        },
        {
            "question": "How do you insert COMMENTS in Python code?",
            "options": ["A) // comment", "B) /* comment */", "C) # comment", "D) <!-- comment -->"],
            "answer": "C",
            "explanation": "Comments in Python start with #."
        },
        {
            "question": "Which keyword is used to create a function in Python?",
            "options": ["A) func", "B) def", "C) function", "D) define"],
            "answer": "B",
            "explanation": "Functions in Python are defined using the 'def' keyword."
        },
        {
            "question": "What is the output of: print(2 * 3 ** 2)?",
            "options": ["A) 36", "B) 18", "C) 12", "D) 24"],
            "answer": "B",
            "explanation": "Exponentiation (**) has higher precedence: 3**2=9, then 2*9=18."
        },
        {
            "question": "Which of these is NOT a Python data type?",
            "options": ["A) list", "B) tuple", "C) array", "D) dictionary"],
            "answer": "C",
            "explanation": "Python has lists, tuples, and dictionaries — but no built-in array type."
        },
        {
            "question": "How do you start a for loop in Python?",
            "options": ["A) for i = 1 to 10:", "B) for (i=0; i<10; i++):", "C) for i in range(10):", "D) foreach i in range(10):"],
            "answer": "C",
            "explanation": "Python uses 'for i in range()' to start a loop."
        },
        {
            "question": "What does the 'len()' function do?",
            "options": ["A) Returns the length of an object", "B) Calculates sum", "C) Converts to integer", "D) None of these"],
            "answer": "A",
            "explanation": "len() returns the number of items in an object like a list or string."
        },
        {
            "question": "Which of the following is a valid variable name?",
            "options": ["A) 2variable", "B) variable_2", "C) variable-2", "D) variable 2"],
            "answer": "B",
            "explanation": "Variable names cannot start with a number or include spaces or hyphens."
        },
        {
            "question": "What is the output of: print(type(3.14))?",
            "options": ["A) <class 'int'>", "B) <class 'float'>", "C) <class 'str'>", "D) <class 'double'>"],
            "answer": "B",
            "explanation": "3.14 is a floating-point number, so type() returns <class 'float'>."
        },
        {
            "question": "How do you create a list in Python?",
            "options": ["A) list = ()", "B) list = []", "C) list = {}", "D) list = <>"],
            "answer": "B",
            "explanation": "Lists are created using square brackets []."
        },
        {
            "question": "Which statement is used to stop a loop?",
            "options": ["A) stop", "B) exit", "C) break", "D) quit"],
            "answer": "C",
            "explanation": "The 'break' statement stops the loop immediately."
        },
        {
            "question": "Which statement is used to skip to the next iteration in a loop?",
            "options": ["A) break", "B) continue", "C) pass", "D) skip"],
            "answer": "B",
            "explanation": "'continue' skips the current iteration and moves to the next one."
        },
        {
            "question": "What is the output of: print(10 // 3)?",
            "options": ["A) 3.33", "B) 3", "C) 3.0", "D) 4"],
            "answer": "B",
            "explanation": "'//' is floor division, it removes the decimal part and gives 3."
        },
        {
            "question": "Which of the following is immutable?",
            "options": ["A) list", "B) dict", "C) set", "D) tuple"],
            "answer": "D",
            "explanation": "Tuples cannot be changed after creation, so they are immutable."
        },
        {
            "question": "How do you start an 'if' statement in Python?",
            "options": ["A) if x > y:", "B) if (x > y)", "C) if x > y then", "D) if x > y {}"],
            "answer": "A",
            "explanation": "Python uses a colon (:) to start the block after 'if'."
        },
        {
            "question": "How do you start an 'else if' statement in Python?",
            "options": ["A) elseif", "B) elif", "C) else if", "D) otherwise"],
            "answer": "B",
            "explanation": "Python uses 'elif' instead of 'else if'."
        },
        {
            "question": "Which operator is used for exponentiation?",
            "options": ["A) ^", "B) **", "C) *", "D) pow"],
            "answer": "B",
            "explanation": "'**' is the power operator, e.g., 2**3 = 8."
        },
        {
            "question": "What is the output of: bool(0)?",
            "options": ["A) True", "B) False", "C) 0", "D) None"],
            "answer": "B",
            "explanation": "0 is considered False in Python."
        },
        {
            "question": "How do you define a class in Python?",
            "options": ["A) create class MyClass:", "B) def class MyClass:", "C) class MyClass:", "D) MyClass class:"],
            "answer": "C",
            "explanation": "Classes are defined using the 'class' keyword."
        },
        {
            "question": "What keyword is used to create an object from a class?",
            "options": ["A) construct", "B) new", "C) self", "D) None of these"],
            "answer": "D",
            "explanation": "Python creates objects by simply calling the class name like MyClass()."
        
        },
        {
            "question": "Which method is called when an object is created?",
            "options": ["A) __start__", "B) __create__", "C) __init__", "D) __main__"],
            "answer": "C",
            "explanation": "__init__ is the constructor method that runs when an object is created."
        },
        {
            "question": "How do you import a module named 'math'?",
            "options": ["A) import math", "B) include math", "C) using math", "D) load math"],
            "answer": "A",
            "explanation": "The 'import' keyword is used to include modules like 'math'."
        },
        {
            "question": "Which of these is used to handle exceptions?",
            "options": ["A) catch/throw", "B) try/except", "C) do/while", "D) error/catch"],
            "answer": "B",
            "explanation": "Python uses 'try' and 'except' to handle exceptions."
        },
        {
            "question": "What is the output of: print(5 == '5')?",
            "options": ["A) True", "B) False", "C) Error", "D) None"],
            "answer": "B",
            "explanation": "Different data types (int and str) are not equal, so it's False."
        },
        {
            "question": "What is the correct syntax to open a file named 'data.txt' for reading?",
            "options": ["A) open('data.txt')", "B) open('data.txt', 'r')", "C) open('data.txt', 'read')", "D) open.file('data.txt')"],
            "answer": "B",
            "explanation": "'r' mode is used for reading a file in Python."
        },
        {
            "question": "Which keyword is used to define a lambda function?",
            "options": ["A) def", "B) lambda", "C) func", "D) lmb"],
            "answer": "B",
            "explanation": "Anonymous functions are defined using the 'lambda' keyword."
        },
        {
            "question": "Which of the following functions converts a string to lowercase?",
            "options": ["A) lower()", "B) down()", "C) toLowerCase()", "D) strlower()"],
            "answer": "A",
            "explanation": "The 'lower()' function changes all characters to lowercase."
        },
        {
            "question": "What is the output of: 'Hello'.upper()?",
            "options": ["A) hello", "B) HELLO", "C) Error", "D) none"],
            "answer": "B",
            "explanation": "'upper()' converts all characters to uppercase."
        },
        {
            "question": "What is a correct way to create a dictionary?",
            "options": ["A) {'name': 'John', 'age': 25}", "B) ('name': 'John', 'age': 25)", "C) ['name': 'John', 'age': 25]", "D) dict{'name': 'John'}"],
            "answer": "A",
            "explanation": "Dictionaries are created using curly braces with key-value pairs."
        },
        {
            "question": "What does 'append()' do in a list?",
            "options": ["A) Adds an item to the end", "B) Removes the last item", "C) Sorts the list", "D) Adds to the beginning"],
            "answer": "A",
            "explanation": "'append()' adds an element to the end of a list."
        },
        {
            "question": "What is the output of: print('5' + '6')?",
            "options": ["A) 11", "B) 56", "C) Error", "D) None"],
            "answer": "B",
            "explanation": "Both are strings, so they are concatenated to form '56'."
        },
        {
            "question": "How do you create a tuple?",
            "options": ["A) ()", "B) []", "C) {}", "D) <>"],
            "answer": "A",
            "explanation": "Tuples are created using parentheses ()."
        },
        {
            "question": "How do you get the number of items in a list?",
            "options": ["A) length(list)", "B) count(list)", "C) len(list)", "D) size(list)"],
            "answer": "C",
            "explanation": "'len()' returns the number of elements in a list."
        },
        {
            "question": "Which of the following is used to define a block of code?",
            "options": ["A) Curly braces {}", "B) Parentheses ()", "C) Indentation", "D) Quotes"],
            "answer": "C",
            "explanation": "Python uses indentation instead of braces to define code blocks."
        },
        {
            "question": "What is the output of: print(3 * 'ab')?",
            "options": ["A) ab3", "B) ababab", "C) Error", "D) 3ab"],
            "answer": "B",
            "explanation": "Strings can be multiplied; 'ab' * 3 = 'ababab'."
        },
        {
            "question": "Which function is used to get input from a user?",
            "options": ["A) read()", "B) input()", "C) gets()", "D) scan()"],
            "answer": "B",
            "explanation": "The 'input()' function reads user input as a string."
        },
        {
            "question": "How do you check the data type of a variable?",
            "options": ["A) typeof(x)", "B) type(x)", "C) gettype(x)", "D) data(x)"],
            "answer": "B",
            "explanation": "'type()' returns the data type of any object."
        },
        {
            "question": "Which keyword is used to return a value from a function?",
            "options": ["A) return", "B) yield", "C) send", "D) give"],
            "answer": "A",
            "explanation": "'return' is used to send a result back from a function."
        },
        {
            "question": "What is the output of: print(9 % 2)?",
            "options": ["A) 4.5", "B) 1", "C) 0", "D) 2"],
            "answer": "B",
            "explanation": "'%' gives the remainder — 9 divided by 2 leaves remainder 1."
        },
        {
            "question": "How do you check if 'x' is even?",
            "options": ["A) if x/2 == 0:", "B) if x%2 == 0:", "C) if even(x):", "D) if x==even"],
            "answer": "B",
            "explanation": "If x % 2 equals 0, the number is even."
        },
        {
            "question": "What keyword is used to create an empty class?",
            "options": ["A) pass", "B) none", "C) break", "D) empty"],
            "answer": "A",
            "explanation": "'pass' is used as a placeholder for an empty class or function."
        },
        {
            "question": "What does 'import os' allow you to do?",
            "options": ["A) Handle math operations", "B) Interact with the operating system", "C) Create graphics", "D) Manage databases"],
            "answer": "B",
            "explanation": "The 'os' module lets you interact with the operating system."
        },
        {
            "question": "How can you remove whitespace from both ends of a string?",
            "options": ["A) strip()", "B) trim()", "C) clean()", "D) cut()"],
            "answer": "A",
            "explanation": "'strip()' removes leading and trailing spaces."
        },
        {
            "question": "Which function is used to convert a string into an integer?",
            "options": ["A) int()", "B) str()", "C) float()", "D) chr()"],
            "answer": "A",
            "explanation": "'int()' converts a string or number to an integer."
        },
        {
            "question": "What is the output of: print(bool('False'))?",
            "options": ["A) True", "B) False", "C) None", "D) 0"],
            "answer": "A",
            "explanation": "Any non-empty string is considered True in Python."
        },
        {
            "question": "Which function can be used to sort a list?",
            "options": ["A) sort()", "B) order()", "C) arrange()", "D) organize()"],
            "answer": "A",
            "explanation": "'sort()' arranges the list elements in ascending order by default."
        },
        {
            "question": "Which data type is returned by the input() function?",
            "options": ["A) str", "B) int", "C) bool", "D) float"],
            "answer": "A",
            "explanation": "'input()' always returns user input as a string."
        },
        {
            "question": "Which module is used for random number generation?",
            "options": ["A) random", "B) randint", "C) numbers", "D) math"],
            "answer": "A",
            "explanation": "The 'random' module is used to generate random numbers."
        },
        {
            "question": "What is the correct way to define a docstring?",
            "options": ["A) // comment", "B) '''This is a docstring'''", "C) <doc>Text</doc>", "D) # This is a docstring"],
            "answer": "B",
            "explanation": "Triple quotes '''...''' are used for docstrings."
        },
        {
            "question": "Which function is used to find the maximum value?",
            "options": ["A) high()", "B) max()", "C) top()", "D) largest()"],
            "answer": "B",
            "explanation": "'max()' returns the largest value in an iterable."
        },
        {
            "question": "Which Python keyword is used for inheritance?",
            "options": ["A) inherits", "B) extends", "C) super", "D) class Child(Parent):"],
            "answer": "D",
            "explanation": "Inheritance is defined using 'class Child(Parent):'."
        },
        {
            "question": "What symbol is used to comment multiple lines?",
            "options": ["A) ''' ... '''", "B) #", "C) //", "D) --"],
            "answer": "A",
            "explanation": "Triple quotes ''' ... ''' can be used for multi-line comments."
        }
    ]
  
  
  
def calculate_grade(score, total):
    percentage = (score / total) * 100
    if percentage >= 90:
        return "A+ (Excellent)"
    elif percentage >= 80:
        return "A (Very Good)"
    elif percentage >= 70:
        return "B (Good)"
    elif percentage >= 60:
        return "C (Satisfactory)"
    elif percentage >= 50:
        return "D (Needs Improvement)"
    else:
        return "F (Fail)"


def run_quiz():
    questions = python_quiz()
    score = 0

    print("📘 Welcome to the Python Basics Quiz!\n")

    for i, q in enumerate(questions, start=1):
        print(f"Q{i}. {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.")
            print(f"💡 Explanation: {q['explanation']}\n")

    total = len(questions)
    grade = calculate_grade(score, total)

    print("🎉 Quiz Complete!")
    print(f"Your Score: {score} out of {total}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    run_quiz()
