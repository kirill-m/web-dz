from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

html = """
<html>
<body>
	<h1> Hello world! (wsgi) </h1>
   <form method="post" action="hello.py">
      <p>
         Age: <input type="text" name="age">
         </p>
      <p>
         Hobbies:
         <input name="hobbies" type="checkbox" value="software"> Software
         <input name="hobbies" type="checkbox" value="tunning"> Auto Tunning
	 </p>
      <p>
         <input type="submit" value="Submit">
         </p>
      </form>

      <form method="get" action="hello.py">
      <p>
         Info: <input type="text" name="info">
         </p>
      </form>
      <p>
         Age: %s<br>
         Hobbies: %s <br>
         Info: %s
         </p>
   </body>
</html>
"""

def application(environ, start_response):

   try:
      request_body_size = int(environ.get('CONTENT_LENGTH', 0))
   except (ValueError):
      request_body_size = 0

   request_body = environ['wsgi.input'].read(request_body_size)
   d = parse_qs(request_body)
   e = parse_qs(environ['QUERY_STRING'])

   age = d.get('age', [''])[0] 
   hobbies = d.get('hobbies', [])
   info = e.get('info',[''])[0] 
 #  age = e.get('age', [''])[0]
 #  hobbies = e.get('hobbies', [])

   age = escape(age)
   hobbies = [escape(hobby) for hobby in hobbies]
   info = escape(info)

   response_body = html % (age or 'Empty',
               ', '.join(hobbies or ['No Hobbies']), info or 'Empty')

   status = '200 OK'

   response_headers = [('Content-Type', 'text/html'),
                  ('Content-Length', str(len(response_body)))]
   start_response(status, response_headers)

   return [response_body]
