# makefile for pdflatex

# makefile for pdflatex


SRC = manual.tex \
	introduction.tex \
	skills.tex \
	license.tex 


TARGET = manual
TMP = tmp

$(TARGET).pdf: $(SRC)
	pdflatex --output-director $(TMP) $(TARGET).tex
	mv $(TMP)/$(TARGET).pdf .

clean::
	rm -f $(TMP)/*.aux $(TMP)/*.out $(TMP)/*.log $(TMP)/*.toc 



