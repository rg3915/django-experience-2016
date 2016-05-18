pdf:
	latexmk -pdf ${f}
	latexmk -c

# usage: make pdf f="01fk.tex"

pvc:
	latexmk -pdf -pvc ${f}

clear:
	latexmk -c
	rm *.nav *.snm *.vrb

convert:
	convert -density 300 01fk.pdf 01fk.jpg
	convert -density 300 02oneToone.pdf 02oneToone.jpg
	convert -density 300 03m2m.pdf 03m2m.jpg
	convert -density 300 04m2m.pdf 04m2m.jpg
	convert -density 300 05abstract.pdf 05abstract.jpg
	convert -density 300 06multitable.pdf 06multitable.jpg
