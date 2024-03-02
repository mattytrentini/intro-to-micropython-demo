# Autogenerated file
def render(message):
    yield """<!doctype html>
<html>
  <head>
    <title>Introduction to MicroPython Demo</title>
    <meta charset=\"UTF-8\">
  </head>
  <body>
    <h1>Introduction to MicroPython Demo</h1>
    """
    if message:
        yield """    <p>Your message: \"<b>"""
        yield str(message)
        yield """</b>\" has been queued!</p>
    """
    yield """    <form method=\"POST\">
      <p>
        What message would you like to display?
        <input type=\"text\" name=\"message\" autofocus />
      </p>
      <input type=\"submit\" value=\"Submit\" />
    </form>
  </body>
</html>
"""