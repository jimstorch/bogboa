# makefile for pdflatex

TARGET = bogboa_manual
TMP = tmp
SRC = $(wildcard ./*.tex)


$(TARGET).pdf: $(SRC)
	pdflatex --output-director $(TMP) $(TARGET).tex
	mv $(TMP)/$(TARGET).pdf .

clean::
	rm -f $(TMP)/*.aux $(TMP)/*.out $(TMP)/*.log $(TMP)/*.toc 



