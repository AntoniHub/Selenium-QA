Feature: Focus on Exposure
  User correctly logged in and with active subscription, will go through each of the sub-sections of this section.
    .- Email security: Having only information, you will click on the drop-downs only (the rescan can take a long time for an automated test).
    .- Data filtrations: Same as the previous section but will search the observed inputs for information.
    .- Website security: With more content, information modalities will be displayed, the configured domain will be displayed,
       the remove domain button will be disabled if there is only one domain configured (the rescan can take a long time for an automated test).
    .- Possible impersonations: The configured domain is displayed, an attempt is made to add another domain, input is used.
    .- Supplier security: Only the dropdowns are displayed because adding a supplier can take a long time for an automated test.
  In each of these sections there are tutorials that can be viewed and skipped in all cases.


  Scenario: User browsing through Exposure
    Given Clicking on Exposure
     When Begin with exposure
     Then Switch to all items