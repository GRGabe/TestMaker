tfTitle = "True /False"
tfInst  = "For the following questions, please clearly {\\bf circle} {\\bf T} (if the statement is always true) or {\\bf F} (if the statement is sometimes false). If your answer is unclear it will be marked wrong. Each question is worth 2 points. "

mcTitle = "Multiple Choice"
mcInst  = "Clearly circle the letter for your answer. Only {\\bf one} choice is correct. Each question is worth 4 points."

saTitle = "Short Answer"
saInst  = "The questions below are each worth 5 points. Show all of your work and place your answers in the boxes provided."



plot1 = """\\begin{center}
\\begin{tikzpicture}[scale=0.5]
\\draw [<->] (0,-2.2)--(0,2.2) node[above] {$y$};
\\draw [<->] (-2.2,0)--(2.2,0) node[right] {$x$};
\\draw (0,0) circle (0.8cm);
\\draw (0,0) circle (1.2cm);
\\draw (0,0) circle (1.5cm);
\\draw (0,0) circle (1.7cm);
\\draw (0,0) circle (1.8cm);
\\draw (0,0) circle (1.87cm);
\\draw (0,0) circle (1.93cm);
\\end{tikzpicture}
\\end{center}
"""

plot2 = """\\begin{center}
\\begin{tikzpicture}[scale=0.5]
\\draw [<->] (0,-2.2)--(0,2.2) node[above] {$y$};
\\draw [<->] (-2.2,0)--(2.2,0) node[right] {$x$};
\\draw (-2,1.8)--(-1.9,2);
\\draw (-2,1.2)--(-1.6,2);
\\draw (-2,0.8)--(-1.4,2);
\\draw (-2,0.4)--(-1.2,2);
\\draw (-2,-0.2)--(-0.9,2);
\\draw (-2,-1)--(-0.5,2);
\\draw (-1.9,-2)--(0.1,2);
\\draw (-1.5,-2)--(0.5,2);
\\draw (-1.2,-2)--(0.8,2);
\\draw (-1,-2)--(1,2);
\\draw (-0.8,-2)--(1.2,2);
\\draw (-0.5,-2)--(1.5,2);
\\draw (-0.1,-2)--(1.9,2);
\\draw (0.5,-2)--(2,1);
\\draw (0.9,-2)--(2,0.2);
\\draw (1.2,-2)--(2,-0.4);
\\draw (1.4,-2)--(2,-0.8);
\\draw (1.6,-2)--(2,-1.2);
\\draw (1.9,-2)--(2,-1.8);
\\end{tikzpicture}
\\end{center}
"""



tf01q = 'If  $\\v{{u}}$ and $\\v{{v}}$ are vectors and $\\theta$ is the angle between them, then $\\dfrac{{{}}}{{|\\v{{u}}||\\v{{v}}|}}={} \\theta$.'
tf01a = ['F', 'T', 'T', 'F']
tf01v = [['|\\v{u}\\times\\v{v}|', '|\\v{u}\\times\\v{v}|', 
		'\\v{u}\cdot\\v{v}', '\\v{u}\cdot\\v{v}'],
	['\\cos', '\\sin', '\\cos', '\\sin']]

tf02q = 'If $\\v{{u}}$ is the vector normal to one plane, and $\\v{{v}}$ is the vector normal to another plane, then the vector ${}$ is parallel to the line in which these two planes intersect.'
tf02a = ['T', 'F']
tf02v = [['\\v{u}\\times\\v{v}', '\\operatorname{proj}_{\\v{v}}\\v{u}',]]

tf03q = 'The {} product of two vectors produces a {}.'
tf03a = ['F', 'T', 'T', 'F']
tf03v = [['cross', 'cross', 'dot', 'dot'],['scalar', 'vector', 'scalar', 'vector']]

tf04q = 'If two vectors are {} their {} product is ${}$.'
tf04a = ['T', 'F', 'F', 'T']
tf04v = [['parallel', 'parallel', 'perpendicular', 'perpendicular'],
	 ['cross', 'dot', 'cross', 'dot'],
	 ['\\v0', '0', '\\v0', '0']]

tf05q = 'Given two functions of three variables, $f(x,y,z),g(x,y,z)$ that are both continuous with continuous partial derivatives, the intersection of $f(x,y,z)=C_1$ and $g(x,y,z)=C_2$, for some constants $C_1,C_2$ generically is a {}.'

tf05a = ['T', 'F', 'F']
tf05v = [['curve', 'surface', 'point']]

tf06q = 'The ordered set of vectors, $\\langle\\v{{\\hat{{{}}}}},\\v{{\\hat{{{}}}}},\\v{{\\hat{{{}}}}}\\rangle$ form a right hand orientation.'
tf06a = ['F', 'F', 'T', 'T', 'F']
tf06v = [['i', 'j', 'j', 'k', 'k'],
	 ['k', 'i', 'k', 'i', 'j'],
	 ['j', 'k', 'i', 'j', 'i']]

tf07q = 'The contour plot below could be a contour plot of the function $f(x,y)={}$.\n{}'
tf07a = ['T', 'F', 'F', 'T']
tf07v = [['e^{x^2+y^2}', '\\sin(2x-y)','e^{x^2+y^2}', '\\sin(2x-y)'],
	 [plot1, plot1, plot2, plot2]]

tf08q = 'The function $f(x,y)={}$ is radially symmetric.'
tf08a = ['T', 'T', 'F']
tf08v = [['3x^2+3y^2', 'e^{-(x^2+y^2)}', 'x^2 - y^2 + 2xy']]

tf09q = 'The function $f(x,y)={}$ is linearly symmetric.'
tf09a = ['T', 'T', 'F', 'F']
tf09v = [['(3x-4y)^2', '\\cos(3x-4y)', 'xy+y^2-x', 'e^y\\sin(x)']]

tf10q = 'When evaluating a limit such as $\\displaystyle{{\\lim_{{(x,y)\\to(0,0)}}f(x,y)}}$, it {} enough to show that $\\displaystyle{{\\lim_{{t\\to0}}f(at,bt)}}$ exists and is the same for every $a,b$.'
tf10a = ['F', 'T']
tf10v = [['is', 'is not']]

tf11q = 'If $f(x,y)$ is an elementary function, and $(0,0)$ is in its domain, then $\\displaystyle{{\\lim_{{(x,y)\\to(0,0)}}f(x,y)=f(0,0)}}$.'
tf11a = ['T']
tf11v = [['']]

tf12q = 'If $f(x,y)$ is defined everywhere, and $f_{{xy}}$ and $f_{{yx}}$ are defined and continuous everywhere, then for all points $(a,b)$,\n\\[f_{{xy}}(a,b)=f_{{yx}}(a,b).\\]'
tf12a = ['T']
tf12v = [['']]

tf13q = 'The directional derivative of a function of several variables can be computed directly in terms of the gradient of that function.'
tf13a = ['T']
tf13v = [['']]

tf14q = 'For any continuous and differentiable function $f(x,y)$, its gradient, $\\nabla f(a,b)$, produces the vector that points {} on the graph of $f$.'
tf14a = ['T', 'F', 'F']
tf14v = [['uphill', 'downhill', 'along the same elevation']]

tf15q = 'For any continuous and differentiable function, $f(x,y)$, its gradient, $\\nabla f(a,b)$, is {} to the level curves of $f$.'
tf15a = ['T', 'F']
tf15v = [['normal', 'tangent']]

tf16q = 'For any continuous and differentiable function the set of critical points is a subset of the {}, while the set of critical values is a subset of the {}.'
tf16a = ['T', 'F']
tf16v = [['domain', 'codomain'],['codomain','domain']]

tf17q = 'The set $C=\\{{(x,y)\\,|\\,{}\\}}$ is a closed set.'
tf17a = ['T', 'F', 'F']
tf17v = [['x^2+y^2 \\leq 1', 'x^2 + y \\leq 1', 'x^2 + y^2 < 1']]

tf18q = 'When finding the extrema of a function $f(x,y,z)$ subject to a constraint $g(x,y,z)=k$, assuming that $f,g$ are continuous, differentiable, and $g$ has a nonzero gradient on $g=k$, the method of Lagrange multipliers takes advantage of the geometric fact that at such extrema, $\\nabla f$ is {} to $\\nabla g$.'
tf18a = ['T', 'F']
tf18v = [['parallel', 'perpendicular']]



mc1q = 'What is the projection of $\\v{{u}}$ in the direction of $\\v{{v}}$?'
mc1a = ['$\\left(\\dfrac{\\v{u}\cdot\\v{v}}{|\\v{v}|^2}\\right)\\v{v}$']
mc1v = [['']]
mc1c = ['$\\left(\\dfrac{\\v{u}\cdot\\v{v}}{|\\v{u}|^2}\\right)\\v{v}$', 
	'$\\left(\\dfrac{\\v{u}\cdot\\v{v}}{|\\v{v}|^2}\\right)\\v{u}$', 
	'$\\left(\\dfrac{\\v{u}\cdot\\v{v}}{|\\v{u}|^2}\\right)\\v{u}$']
mc1e = True

mc2q = 'The cross product is'
mc2a = ['neither associative nor commutative.']
mc2v = [['']]
mc2c = ['both associative and commutative.', 
	'associative but not commutative.', 
	'commutative but not associative.']
mc2e = True

mc3q = 'For $f(x,y)={}$, compute the value of $f({})$.'
mc3a = ['-8', '-9', '2', '-6']
mc3v = [['2x^2y-y^2', '2x^2y-y^2', 'xy^2-2x^2', 'xy^2-2x^2'],
	['1,-2', '2,-1', '1,-2', '2,-1']]
mc3c = ['-10', '-7', '0', '7', '8']
mc3e = True

mc4q = 'The tangent plane of $f(x,y)=x^2y+x$ at $(x,y)=(1,2)$ is given by'
mc4a = ['$T(x,y)=5(x-1)+(y-2)+3$.']
mc4v = [['']]
mc4c = ['$T(x,y)=6(x-1)+(y-2)+3$.', 
	'$T(x,y)=4(x-1)+(y-2)+3$.', 
	'$T(x,y)=5(x-1)+2(y-2)+3$.', 
	'$T(x,y)=5(x-1)-(y-2)+3$.',  
	'$T(x,y)=4(x-1)+(y-2)+2$.', 
	'$T(x,y)=5(x-1)+2(y-2)+2$.', 
	'$T(x,y)=5(x-1)-(y-2)+4$.']
mc4e = True

mc5q = 'Given functions $f(x,y)$ and $x(u,v)$ and $y(u,v)$ to obtain a function $f(u,v):=f(x(u,v),y(u,v))$, what is $\\dfrac{{\\partial f}}{{\partial u}}$'
mc5a = ['$\\dfrac{\\partial f}{\\partial x}\\dfrac{\\partial x}{\\partial u}+\\dfrac{\\partial f}{\\partial y}\\dfrac{\\partial y}{\\partial u}$']
mc5v = [['']]
mc5c = ['$\\dfrac{\\partial f}{\\partial u}\\dfrac{\\partial u}{\\partial x}+\\dfrac{\\partial f}{\\partial u}\\dfrac{\\partial u}{\\partial y}$',
	'$\\dfrac{\\partial f}{\\partial x}\\dfrac{\\partial x}{\\partial u}+\\dfrac{\\partial f}{\\partial y}\\dfrac{\\partial y}{\\partial u}+\\dfrac{\\partial f}{\\partial v}\\dfrac{\\partial v}{\\partial u}$', 
	'$\\dfrac{\\partial f}{\\partial x}\\dfrac{\\partial u}{\\partial x}$']
mc5e = True

mc6q = 'The gradient of $f(x,y,z)=2xyz-x^2y+3y^2z$ is'
mc6a = ['$\\langle 2yz-2xy,\\, 2xz-x^2+6yz,\\, 2xy+3y^2 \\rangle$.']
mc6v = [['']]
mc6c = ['$\\langle 2yz,\\, -x^2,\\, 3y^2 \\rangle$.',
	'$\\langle 2yz-2y,\\, 2xz-x^2+6z,\\, 2xy+3y^2 \\rangle$.',
	'$(2yz-2xy) + (2xz-x^2+6yz) + (2xy+3y^2)$.']
mc6e = True



sa1q = 'Compute the dot product of $\\langle{}\\rangle$ and $\\langle{}\\rangle$.'
sa1a = [-5,1]
sa1v = [['1,-2,3', '1,0,2'],['0,1,-1', '-1,4,1']]

sa2q = 'Compute the cross product of $\\langle 0,1,1\\rangle$ and $\\langle 1,-1,0\\rangle$.'
sa2a = ['$\\langle 1,1,-1 \\rangle$']
sa2v = [['']]

sa3q = 'Compute the critical point(s) of $f(x,y)=(x-{})^2+(y-{})^2$.'
sa3a = [(3,2),(1,2),(1,3),(2,1)]
sa3v = [['3', '1', '1', '2'],
	['2', '2', '3', '1']]

sa4q = 'For $f(x,y)={}$, compute $f_x(x,y)$.'
sa4a = ['($2xy+\\cos x\\cos y$)']
sa4v = [['x^2y+\\sin x\\cos y']]

sa5q = 'For $f(x,y)={}$, compute $f_y(x,y)$.'
sa5a = ['[$x^2-\\sin x\\sin y$]']
sa5v = [['x^2y+\\sin x\\cos y']]

sa6q = 'For $f(x,y)=x^2y$ and $\\v{{u}}=\\langle 1,2 \\rangle$, compute $D_{{\\v{{u}}}}f(3,2)$.'
sa6a = [30]
sa6v = [['']]

sa7q = 'For $\\v{{r}}(t)=\\langle t^2,e^t\\rangle$, compute $\\v{{v}}(t)$.'
sa7a = ['$\\langle 2t,e^t \\rangle$']
sa7v = [['']]

sa8q = 'For $\\v{{r}}(t)=\\langle t^2,e^t\\rangle$, compute $\\v{{a}}(t)$.'
sa8a = ['$\\langle 2,e^t \\rangle$']
sa8v = [['']]
