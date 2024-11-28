# Created by pokizaergasheva at 11/28/24
Feature: Sign in page on Target

   Scenario: Verify 'Sign in' page opened
     Given Open target main page
     When Click on sign in icon on top navigation menu
     And Click on sign in button from right side navigation menu
     Then Verify 'Sign in' form is shown
