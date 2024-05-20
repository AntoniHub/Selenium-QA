Feature: User browsing in Proteccion
  User with valid ID and Pass to enter example.com. If you want to see the status of your protections,
  click on Protection and it will display each of the sections with the different protections available. You will be able to:
    .- View the protected devices and the status of the protections.
    .- Send licenses and see the licenses sent to your employees.
    .- You can also view the security status of mailboxes, view the quarantine, release and delete mails that seem suspicious.

  Scenario: User who wants to check the status of his safeguards
    Given User in the example.com application who wants to check the status of his protections
     When Click on Protections
     Then It will display each of the sections and you will be able to navigate between them