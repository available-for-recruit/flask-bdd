from behave import *

@given(u'flaskr is set up')
def flask_is_setup(context):
  assert context.client and context.db

@given(u'we log in with "{username}" and "{password}"')
@when(u'we log in with "{username}" and "{password}"')
def login(context, username, password):
  context.client.get("/login", follow_redirects = True)
  context.page = context.client.post(
                                     "/login/",
                                     data = dict(
                                                 username = username,
                                                 password = password),
                                     follow_redirects = True
                                     )
  assert context.page

@when(u'we log out')
def logout(context):
  context.page = context.client.get("/logout", follow_redirects = True)
  assert context.page

@then(u'we should see the alert "{message}"')
def messge(context, message):
  assert str.encode(message) in context.page.data

@given(u'we add a new entry with "{title}" and "{text}" as the title and text')
@when(u'we add a new entry with "{title}" and "{text}" as the title and text')
def add(context, title, text):
  context.page = context.client.post(
                                     "/add/",
                                     data = dict (
                                                  title = title,
                                                  text = text
                                                  ),
                                     follow_redirects = True
                                     )
  assert context.page

@then(u'we should see the post with "{title}" and "{text}" as the title and text')
def entry(context, title, text):
  assert str.encode(title) and str.encode(text) in context.page.data

@given(u'we are not logged in')
def logout(context):
  context.page = context.client.get("/logout/", follow_redirects = True)

@when(u'we are at the index page')
@given(u'we are at the index page')
def index(context):
  context.page = context.client.get("/", follow_redirects = True)

@then(u'we should see the following text: "{string}"')
def str_in_page(context, string):
  assert str.encode(string) in context.page.data

