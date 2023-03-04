for i in range(1, 100):
    a = bool(input(f"is {i} divisible by 3?"))
    b = bool(input(f"is {i} divisible by 5?"))
    match [a,b]:
        case [True, True]:
            print(f" well then {i} is FizzBuzz but you could have figured that out yourself couldn't you?")
        case [True, False]:
            print(f" well then {i} is Fizz but you could have figured that out yourself couldn't you?")
        case [True, False]:
            print(f" well then {i} is Buzz but you could have figured that out yourself couldn't you?")
        case [False, False]:
            print(f" well then {i} is {i} but you could have figured that out yourself couldn't you?")