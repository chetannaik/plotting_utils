.SUFFIXES: .tex .in .dvi .ps .pdf
all: example.pdf tree.pdf physics.pdf trials.pdf tree.pdf withpgf.pdf
.tex.pdf: 
	pdflatex $<
clean:
	rm -f  *.aux *.dvi *.ps *.bbl *.blg *.out *.log *.toc *.nav *.snm *.bak *~ *.pdf *.table *.gnuplot
