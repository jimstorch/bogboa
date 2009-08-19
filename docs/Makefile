# makefile for pdflatex

INCLUDE = ".:./include:"
TARGET = bogboa_manual
TMP = tmp
SRC = $(wildcard ./*.tex)


$(TARGET).pdf:: 
	TEXINPUTS=$(INCLUDE) pdflatex --output-directory $(TMP) $(TARGET).tex
	mv $(TMP)/$(TARGET).pdf .

clean::
	rm -f $(TMP)/*.aux $(TMP)/*.out $(TMP)/*.log $(TMP)/*.toc $(TARGET).pdf



