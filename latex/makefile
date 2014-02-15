LATEX = platex
DVIPDF = dvipdfmx

TEXFILE = $(shell ls *.tex)
DVIFILE = $(TEXFILE:%.tex=%.dvi)
PDFFILE = $(TEXFILE:%.tex=%.pdf)


%.dvi: %.tex
	echo $<
	$(LATEX) $<
	$(LATEX) $<

%.pdf: %.dvi
	$(DVIPDF) $<

.PHONY: pdf
pdf: $(PDFFILE)

.PHONY: clean
all: 
	echo $(DVIFILE)
	make $(DVIFILE)

.PHONY: clean
clean:
	rm *.dvi *.pdf

