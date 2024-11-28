# Created by pokizaergasheva at 11/28/24
Feature: Shopping cart on Target

    Scenario: Verify “Your cart is empty” message is shown
      Given Open target main page
      When Click on cart icon
      Then Verify “Your cart is empty” message is shown
