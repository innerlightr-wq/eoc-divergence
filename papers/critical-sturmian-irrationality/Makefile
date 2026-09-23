# Build the paper, and re-run the verification it cites.

PAPER = main

.PHONY: all clean verify verify-deep verify-slopes-deep

all: $(PAPER).pdf

$(PAPER).pdf: $(PAPER).tex refs.bib
	pdflatex -interaction=nonstopmode $(PAPER).tex
	bibtex $(PAPER)
	pdflatex -interaction=nonstopmode $(PAPER).tex
	pdflatex -interaction=nonstopmode $(PAPER).tex

# Everything except the deepest depth computation (a few seconds).
verify:
	python3 scripts/verify.py all

# Theorem 5.3 checked 2-adically out to n = 14, i.e. the shell (190537, 301994).
# Needs a few minutes and about 0.5 GB.
verify-deep:
	python3 scripts/verify.py depths 14

# Theorem 8.3 at the seven test slopes out to depth 400000 rather than the
# 50000 used by `verify`.  Needs a few minutes.
verify-slopes-deep:
	python3 scripts/verify.py slopes 400000

clean:
	rm -f $(PAPER).aux $(PAPER).log $(PAPER).bbl $(PAPER).blg $(PAPER).out
