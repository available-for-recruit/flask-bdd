Feature: Logged in users and posts
  Scenario: not logged in users can see posts
    Given flaskr is set up
    and we log in with "admin" and "admin"
    and we add a new entry with "test1" and "test1" as the title and text
    When we log out
    and we are at the index page
      Then we should see the post with "test1" and "test1" as the title and text
