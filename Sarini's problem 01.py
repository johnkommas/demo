# Incomplete Python Script
# z = input(Enter Z value:)
# Y == 1 /
# print(The Y Value is +y)

# a) Identify some errors within his code:
# at Line 1:
# A. we want z to be a float number not a string so input() is incomplete we need float(input())
# B. if we want to prompt a message we have to put ("...") " -> are missing
# C. We must take care of ZeroDivisionError
# D. We must take care of ValueError

# at Line 2:
# A.  == is for equalities and returns True or False, we want to assign to Y a value and for the we will use =
# B. 1 / is not our equation so we have to write the correct one
# C. the output must be trimmed to 4 decimals and for that we use round()

# at Line 3:
# A. Missing ("..")
# B. Missing f <- format

def get_number():
    try:
        z = float(input("Enter Z value:"))
        y = round(1 / (z + 1 / (z + 1 / (z + 1 / z))), 4)
        print(f'The Y value is: {y}')
        return y
    except ZeroDivisionError:
        print("ZeroDivisionError please try with another number")
        return get_number()
    except ValueError:
        print("ValueError please try with a number")
        return get_number()
    except KeyboardInterrupt:
        print('Exit Requested')
        quit()


Y = get_number()
