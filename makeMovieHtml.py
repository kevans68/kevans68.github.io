import sys
from glob import glob
from os.path import basename


ROW_START = '<div class="w3-row-padding">'
ROW_END = '</div>'

MOVIE_TEMPLATE = """
<div class="w3-third w3-container w3-margin-bottom">
  <div class="w3-container w3-white">
    <h4><b>{}</b></h4>
    <video width="320" height="240" controls style="width:100%" >
      <source src="Movies/{}"/>
    </video>
    <p>This is a blah blah blah with two galaxies smashing into each other</p>
  </div>
</div>
"""

#import pdb; pdb.set_trace()

movies = [m for m in sys.argv if m[-3:] == 'mp4']

for idx, movie in enumerate(movies):
  if movie[-3:] != 'mp4':
    #print("oh no..." + movie[-3:])
    continue
  if (idx % 3) == 0:
    print(ROW_START)

  print(MOVIE_TEMPLATE.format(basename(movie), movie))

  if ((idx + 1) % 3 ) == 0:
    print(ROW_END)

if(len(movies) % 3 != 0):
  print(ROW_END)
  
