Feature: Checking multiple posts
  Scenario: successful post in reverse order
    Given flaskr is set up
    and we log in with "admin" and "admin"
    and we add a new entry with "test1" and "test1" as the title and text
      When we add a new entry with "test2" and "test2" as the title and text
      Then we should see the alert "New entry was successfully posted"
      Then we should see the post with "test2" and "test2" as the title and text
      Then we should see the post with "test1" and "test1" as the title and text
