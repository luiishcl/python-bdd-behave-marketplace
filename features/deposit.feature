Feature: Register on Deposit 
  As a BEES user,
  I want to access deposit
  So I can manager the deposit register

    @create
    Scenario: Register a Deposit
        Given stay on "Deposits" session
        When create a new deposit
        """
            {
                "name": "Deposit_A",
                "address": "Rua Orlando Viana",
                "city": "Campinas",
                "state": "Sao Paulo",
                "zipcode": "13044900"
            }
        """
        Then the deposits were created successful


    @wip
    Scenario: Edit a Deposit
        Given stay "Edit this deposit" session
        When edit a deposit
        """
            {
                "name": "Deposit_Edited",
                "address": "wall street",
                "city": "city_edited",
                "state": "NY",
                "zipcode": "71601"
            }
        """
        Then the deposits were edited successful