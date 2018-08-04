latexHeader1 = """\\documentclass[11pt]{article}
\\usepackage{amssymb}
\\usepackage{amsmath}
\\usepackage{amsthm}
\\usepackage{amsfonts}
\\usepackage{amsthm}
\\usepackage{fancyhdr}
\\usepackage{multicol}
\\usepackage{amscd}
\\usepackage{tikz}
\\usepackage{enumerate}
\\usepackage[tone]{tipa}
\\usepackage{multicol}
\\usepackage{qrcode}

\\textwidth = 7 in
\\textheight = 9 in
\\oddsidemargin = -0.0 in
\\evensidemargin = 0.0 in
\\topmargin = -0.4 in
\\headheight = 0.0 in
\\headsep = 0.3 in
\\parindent = 0.0in

\\pagestyle{fancyplain}
\\lhead{"""




latexHeader2 = """}
\\rhead{"""




latexHeader3 = """}

\\begin{document}
\\newcommand{\\tf}{\\fbox{\\bf T \\,\\,/\\,\\, F}\\quad}
\\newcommand{\\cd}{\\fbox{\\bf C \\,\\,/\\,\\, D}\\quad}
\\renewcommand{\\v}[1]{\\mathbf{#1}}
\\renewcommand{\\a}{\\underline{\\hspace{1.5cm}}\\,\\,\\,}

"""




coverPage1 = """\setcounter{page}{1}
\\begin{center}
\\begin{Large}
\\underline{"""




coverPage2 = """}
\\end{Large}
\\end{center}


\\vspace{1cm}
{\\bf Name:} \\underline{\\hspace{3in}} {\\bf ID \\#:} \\underline{\\hspace{1.5in}}\\vspace{.5cm}

You have """




coverPage3 = """ to complete the following exam.
\\vspace{.5cm}

Read the directions carefully. In two sections, you are asked to {\\bf circle} the correct answer(s) clearly. If your answer choice is unclear for any given question, it will be marked incorrect.  \\vspace{.5cm}

Pace yourselves. If anything is unclear or confusing, do not be afraid to come and ask me. Good luck!

\\begin{center}
\\vfill

\\qrcode{"""




coverPage4 = """}
\\vfill

Do {\\bf not} write in the grid below. \\vspace{.5cm}

"""




coverPage5 = """\\end{center}

\\newpage
"""




grid1 = """\\begin{tabular}{|c|c|c|}
\\hline
Page Number&Points&Out of\\\\ \\hline
"""




grid2 = """{\\bf Total}&&100 \\\\[2ex] \\hline
\end{tabular}
"""




gridLine1 = "{\\bf "
gridLine2 = "}&&"
gridLine3 = " \\\\[2ex] \\hline"


section1 = "\\section{"
section2 = "}\n"
section3 = "\n \\begin{enumerate}[\\bf 1.)]\n"
sectionA = "\\newpage"
section4 = "\\end{enumerate}\n\\newpage\n\n"