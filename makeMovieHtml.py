import sys
from glob import glob
from os.path import basename


ROW_START = '<div class="w3-row-padding">'
ROW_END = '</div>'

MOVIE_TEMPLATE = """
<div class="w3-third w3-container w3-margin-bottom">
  <div class="w3-container w3-white">
    <h4><b>{}</b></h4>
    <iframe width="560" height="315" style="width:100%" src="https://www.youtube.com/embed/{}" frameborder="0" allowfullscreen></iframe>
    <p>This is a blah blah blah with two galaxies smashing into each other</p>
  </div>
</div>
"""
#MOVIE_TEMPLATE = """
#<div class="w3-third w3-container w3-margin-bottom">
#  <div class="w3-container w3-white">
#    <h4><b>{}</b></h4>
#    <video width="320" height="240" controls style="width:100%" >
#      <source src="Movies/{}"/>
#    </video>
#    <p>This is a blah blah blah with two galaxies smashing into each other</p>
#  </div>
#</div>
#"""

#import pdb; pdb.set_trace()

#movies = [m for m in sys.argv if m[-3:] == 'mp4']
movies = [u'YyCYs8ql1nM', u'XHS7pgmAJ_0', u'MLj4Aqk9s50', u'Wsa30VoCxdw', u'IMwSxf-Zq_0', u'Kvqw8LkIh4Q', u'LBy4TCV6zVA', u'uMEE6eKrcFM', u'3c-5vISWoZw', u'ZbjoMAvy-CI', u'r36RunA9Y04', u'RdAlgP1kQAE', u'fycrP_TcN4E', u'mWkLI2qODXU', u'YF57P4u-Hcs', u'n1C0a2BdUdA'] 

for idx, movie in enumerate(movies):
  if (idx % 3) == 0:
    print(ROW_START)

  print(MOVIE_TEMPLATE.format('MOVIE TITLE', movie))

  if ((idx + 1) % 3 ) == 0:
    print(ROW_END)

if(len(movies) % 3 != 0):
  print(ROW_END)
  
