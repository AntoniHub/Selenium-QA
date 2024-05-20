Feature: Antonio Rodriguez Farias E2E
  User correctly logged into the application, try to browse /client and explore all functionalities.
  Visualising in each of the sections:
    .- Home: Initial graphic with the cybersecurity level, completed actions and pending actions.
    .- Dashboard: You will see the details of the subscriptions you have in a graph classified by Licenses installed, sent but not installed and available to send;
       in addition to other indicators in various tables.
    .- Actions: View your progress, pending and completed actions.
    .- Protections: Hover over each of the sub-sections in this section, displaying the corresponding tool-tip.
    .- Exposure: Like the protections, hover on each of the items and display their tool-tips.
    .- Phishing: You will navigate in each of the sections of this section, looking for the detail of campaigns and users.
       Seeing all the options to create a campaign and the selection of employees to send.
  Finally you will navigate through settings, viewing each of the functionalities such as employees, viewing the registration, importing by CSV and XLSX, filtering by tags.
  In the communications section you will see the operation of each of the slide-buttons as well as the level of subscription and alerts you have.
  Also in each of these sections, you will see the corresponding tutorials and you can choose to watch or skip them.
  The user used in this test is a user with an active subscription in order to be able to go through each of the above mentioned sections.

  Scenario: Run a quick view in /client
    Given User after LogIn
     When Browse /client
     Then Navigate through the entire application