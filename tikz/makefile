.SUFFIXES: .tex .in .dvi .ps .pdf
all: example.pdf physics.pdf trees.pdf withpgf.pdf intersection.pdf process_diag.pdf
.tex.pdf: 
	pdflatex $<
clean:
	rm -f  *.aux *.dvi *.ps *.bbl *.blg *.out *.log *.toc *.nav *.snm *.bak *~ *.pdf *.table *.gnuplot
