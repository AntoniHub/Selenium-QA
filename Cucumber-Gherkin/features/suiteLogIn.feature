Feature: User who can log in successfully
  If the user has the correct ID and Pass, after clicking on login,
  he/she will be able to successfully log in to example.com at /client.

  Scenario: User with valid ID and Pass who can successfully LogIn.
     Given User with a valid ID and Pass
      When Click on LogIn
      Then Successfully log in to example.com at /client