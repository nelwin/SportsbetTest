Feature: Test Next to jump on placing 2 single bets
  Background:
    Given user launches the web application


  Scenario: Validate the placing of of 2 single bets on betslip
    Then I click on first card under "Next to Jump" carousel
    And I add 2 different bets into the Bet Slip by clicking on market button for a particular horse
    And I check betslip to confirm the 2 bets placed