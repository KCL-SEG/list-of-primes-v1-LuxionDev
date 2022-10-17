# Primes exercise

## Assignment
This repository contains some template code for a function called `primes`, which takes a single argument `number_of_primes`:

```
def primes(number_of_primes):
    list = []
    return list
```

In this exercise, you must extend the code such that, given a positive value for `number_of_primes`, the `primes` function returns a list containing the first `number_of_primes` prime numbers.  For example, `primes(10)` should the following list:

```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

Note that we will extend this exercise in a future exercise.  At this time, you do not need to concern yourself with the possibility that `number_of_primes` is less than 1.  This will be addressed in a future exercise.  The tests do not cover that scenario.

## How to complete the exercise
To start work on the exercise, find the URL of this repository on GitHub and clone it to your machine with:

`$ git clone URL`

where `URL` is the URL of your repository on GitHub.  Find the `primes.py` file and complete your solution.

You can test your solution in the development environment by running pytest.  From the root of your Python project, simply run

`$ pytest`

If pytest has not been installed yet, run:

`$ pip3 install pytest`

I recommend that you test your solution locally, but you do not have to do this.  Once your exercise is complete, you need to push your repository with:

`$ git push`

GitHub will automatically test your solution.  
