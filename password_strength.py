"""

**Set Up**  
In this coding challenge, you will be required to create a function that checks a user's password against a defined security policy. The goal is to demonstrate your ability to enforce password policies, validate passwords, and provide feedback to users on the strength and compliance of their passwords.

We have the following “ground rules” for this round:

- We are looking for a complete solution for each part. It does not need to be optimized or fast.
- The question has multiple parts but not all parts are necessary to pass this interview.
- You may choose any language to solve the problem. It will, though, take longer if you are using C/C++.
- We do expect you to write any tests you believe are necessary.
- You may use any third party libraries they deem are necessary.
- You are allowed to use any resources that may assist them, except for generative AI. We do ask that you let us know what you are looking up so that we can offer assistance if needed.

**Part 1**  
We are going to define the first step in our password complexity function to reject any passwords that:

1. Are shorter than 10 characters
2. Do not include an uppercase character, lowercase character, number, and a special character

Write a function that our engineers can call in their registration API request handler that takes in a password and validates it against our policy.

For example, these cases should not pass the verification:

# Too short
password

# No uppercase
password123!

# No number
Pa$$word!!

And these cases should pass the verification:
Pa$$word123
-WWVWLoV-bd.FMF8*vwH2hP-FutT@k

"""

# SOLUTION 1
# Reference: https://uibakery.io/regex-library/password-regex-python

import re

# Validate strong password
password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
result = re.match(password_pattern, '-WWVWLoV-bd.FMF8*vwH2hP-FutT@k') # Returns None

if (result):
    print ("valid")

else:

    print ("password not valid")

"""
Part 2

We’ve had some complaints about our password policy restrictions not supporting passphrases and have decided to update our requirements to reject any passwords that:
Are shorter than 10 characters
For passwords shorter than or equal to 16 characters, do not include an uppercase character, lowercase character, number, and a special character
For passwords longer than 16 characters, do not include a lowercase character and an uppercase character, number, or a special character [ie 16 AND () OR () ]
Our examples from Part 1 should not change the validation. Though, in addition, these cases should now pass the verification:

cafe-aloft-vienna-hoagie # not valid
novice pizzeria suggest severely # not valid
toxinkludgeturnpikeCAULDRON # not valid
QUAINT6download@dotard*partial # VALID
"""

# SOLUTION 2
# Reference: https://regex101.com/

# Still finding the solution its around here somewhere. Stay tuned.
"""
Part 3

Kind of didn't make it to part 3 in time.
"""
