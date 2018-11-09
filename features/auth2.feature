
Feature: Posting is successful or not depending upon login
  Scenario: successful post
    Given flaskr is set up
    and we log in with "admin" and "admin"
      When we add a new entry with "test" and "test" as the title and text
      Then we should see the alert "New entry was successfully posted"
      Then we should see the post with "test" and "test" as the title and text

  Scenario: unsuccessful post
    Given flaskr is set up
    Given we are not logged in
      When we add a new entry with "test" and "test" as the title and text
      Then we should see the alert "Unauthorized"

