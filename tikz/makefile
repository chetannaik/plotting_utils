.SUFFIXES: .tex .in .dvi .ps .pdf
all: example.pdf
.tex.pdf: 
	pdflatex $<
clean:
	rm -f  *.aux *.dvi *.ps *.bbl *.blg *.out *.log *.toc *.nav *.snm *.bak *~ *.pdf *.table *.gnuplot
