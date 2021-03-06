from sys import argv 
from flask import Flask, request, render_template, Markup
app = Flask (__name__)

@app.route("/home/", methods={"GET","POST"})
def home():
    pick = []
    html = ''
    empty = ''
    x = 0
    Data = open("static/data.txt", "r")
    txt  = Data.readline()
    for txt in range(0,5):
        txt = Data.readline()
        if txt != empty:
          pick = txt.split("@")
          div = '''<li><a href="http://localhost:5000/''' + pick[0] + '''">''' + pick[1] + '''</a></li>'''
          html = html + div
    Data.close()
    LAPlayers = Markup(html)
    return render_template('home.html',LAPlayers=LAPlayers)


@app.route('/search/', methods=["GET"])
def search():
    key = request.args.get("name")
    print key
    html = ''
    pick = []
    Data = open("static/data.txt", "r")
    txt = Data.readline()
    while txt:
        txt = Data.readline()
        if txt != '':
          pick = txt.split("@")
          print "loop"
          if key in pick[1]:
            print "success"
            div = '''<p>''' + pick[1] + '''</p>'''
            html = html + div
    input = Markup(html)
    return render_template('players.html', input=input)

@app.route("/home/players")
def player():
  return render_template('players.html')

@app.route("/gallery")
def gallery():
  return render_template('gallery.html')

@app.route('/home/<name>')
def hello(name=None):
    user = {'name': name}
    return render_template('Hello.html', user=user)

@app.route('/club/<clubToken>')
def clubpage (clubToken):
   html = ''
   Data = open("static/data.txt", "r")
   txt = Data.readline()
   while txt:
      print clubToken
      txt = Data.readline()
      if txt == "":
          print "Passed!"
          pass
      else:
          pick = txt.split("@")
          print pick[2]
          if clubToken == pick[2]:
              print "working"
              div = '''<li>''' + pick[6] + '''</li>'''
   Data.close()
   html = html + div 
   Club = Markup(html)
   return render_template('clubPage.html', Club=Club)


@app.route('/<token>')
def club(token):
   pick = []
   html = ''
   Data = open("static/data.txt", "r")
   txt = Data.readline()
   while txt:
       txt = Data.readline()
       pick = txt.split("@")
       if token == pick[0]:
         # for 0 to big:
         #command to find biggest value in list pick[]  save this value in   BIGG
         #if you want to add code at beginning of snippet, place here
         #for 0 to BIG
         #format:  '''<li><a href="">''' + pick[BIGG] + '''</a></li>'''

         div = '''<div class="Pdata"> <ul> <li> <a href="http://localhost:5000/club/''' + pick[2] + '''">''' + pick[2] + '''</a></li><li>''' + pick[1] + '''</li><li>''' + pick[3] + '''</li><li>''' + pick[4] + '''</li><li>''' + pick[5] + '''</li><li>''' + pick[7] + '''</li></div>'''
        
         #if you want to place code here on 1 / 2 iterations use a if
         #statement with:  if counter % 2 == 0 
       #  break

         #end for loop
         #if you want to place code at end of snippet place here
         html = html + div
   Data.close()
   id = Markup(html)
   return render_template('PlayerStats.html',id=id)

@app.route("/players", methods={"GET","POST"})
def players():
    pick = []
    html = ''
    empty = ''
    Data = open("static/data.txt", "r")
    txt  = Data.readline()
    while txt:
        txt = Data.readline()
        if txt != empty:
          pick = txt.split("@")
          div = '''<li><a href="http://localhost:5000/''' + pick[0] + '''">''' + pick[1] + '''</a></li>'''
          html = html + div
    Data.close()
    input = Markup(html)
    return render_template('players.html',input=input)


@app.route("/clubs", methods={"GET","POST"})
def clubs():
    pick = []
    html = ''
    empty = ''
    x = 0
    Data = open("static/data.txt", "r")
    txt  = Data.readline()
    while txt:
        txt = Data.readline()
        if txt != empty:
          pick = txt.split("@")
          div = '''<li><a href="http://localhost:5000/club/''' + pick[2] + '''">''' + pick[2] + '''</a></li>'''
          html = html + div
    Data.close()
    input = Markup(html)
    return render_template('clubs.html',input=input)


if __name__ == "__main__":
  app.run(host='0.0.0.0')
