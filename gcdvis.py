import sys
import os

# teste
(a,b) = (int(sys.argv[1]),int(sys.argv[2]))
if a<b:
    (a,b) = (b,a)

if len(sys.argv) == 4:
    beamer = (sys.argv[3] == 'beamer')
    endline = "\pause \n"
else:
    beamer = False
    endline = "\n"


# angle of rotation (starts at 0, is set to -90 after first iteration)
hor = 0

# counter for alternating the colors
c = 0 
seq_colors = ['orange', 'red', 'cyan', 'lime','pink', 'yellow']
# x of translation 
tx = 0 
# counter for the number of steps (used to close the scope env.)
steps = 0 


"""
The squares are drawn as follows: The first set of squares to fill a
a x b rectangle are drawn horizontally with its first square lower
left vertex with cordinates (0,0). After that we set the angle
hor to -90 and the variable tx to pa (previous a), so that the 
following sets of of squares are 
rotated by -90 degrees and translated to the lower right vertex of 
previous rectangle (coordinates (pa,0)), by doing so recursively we
get the desired result. Since we're including one scope envirovment
inside another the affine transformations are all composed in tikz.
"""

def mdc(a,b, pa):
    global c, hor, tx, ty, cmd
    global steps
    steps += 1
    # the actual euclidean algorithm is just the following 3 lines
    # (and the recursive call)
    if b == 0:
        return a
    (q,r) = divmod(a,b)
    cmd += "% Rectangle for  a = {} and b = {}".format(a,b) + endline
    # previous a, used for the translation of the squares
    if hor == -90:
        tx = pa 
    args = [hor,tx]
    cmd += r"\begin{{scope}}[cm={{cos({0}),-sin({0}),sin({0}),cos({0}),({1},0)}}]".format(*args) + "\n"
    for i in range(q):
        args = [seq_colors[c],(b*i,0),(b*(i+1),b),r"{}\times{}".format(b,b)]
        cmd += r"\draw[fill={}] {} rectangle {} node[pos=.5] {{${}$}};".format(*args) + endline
    c = (c+1) % len(seq_colors)
    # after the first set of squares, the following ones are rotated
    # by -90 deg wrt to the previous one
    if hor == 0:
        hor = -90

    return mdc(b,r,a)

cmd =  "\draw (0, 0) rectangle  ({},{});".format(a,b)
cmd += "\draw ({},-.5) node {{ ${}$ }};".format(a/2,a)
cmd += "\draw (-.5,{}) node {{ ${}$ }};".format(b/2,b) + endline
    
mdc(a,b,a)

for i in range(steps-1):
    cmd += "\\end{scope}\n"


# running pdflatex with tikz comands generated above.

if beamer:
    fin = open("diag_beamer.tex","rt")
    fout = open("final_beamer.tex","wt")
else:
    fin = open("diag_generico.tex","rt")
    fout = open("final.tex","wt")


for line in fin:
  if "#####SUBS####" in line:
    fout.write(line.replace("#####SUBS####",cmd))
  else:
    fout.write(line)

fin.close()
fout.close()

if beamer:
    os.system('pdflatex final_beamer.tex')
else:
    os.system('pdflatex final.tex')