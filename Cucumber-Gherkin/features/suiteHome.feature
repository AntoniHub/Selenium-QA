Feature: Quick view /home
  The user or viewer browsing the home page will be able to observe:
    .- Information about what is, what it is for, who it is aimed at and why.
    .- Video demonstration on how to use the application, install protections and verify each of the sections of example.com.
    .- You can also see the terms of use, terms of contract, privacy policy, configure cookies and go to the online chat.

  Scenario: User or potential client viewing the homepage
     Given User or viewer on the example.com homepage
      When The user wants to view any of the links at the top of the page
      Then He will be able to see each of the links, video, PDF documents and other actions at the top of the page