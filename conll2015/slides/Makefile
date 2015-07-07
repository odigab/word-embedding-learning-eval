# $HeadURL: http://omehani@svn.npc.nicta.com.au/omehani/misc/latex/beamer/Makefile $
# $Id: Makefile 3479 2012-07-13 03:10:36Z omehani $
TEXMFHOME=/usr/local/share/texmf
DESTDIR=$(TEXMFHOME)/tex/latex/beamer

INSTALL=install
TEXHASH=texhash
INKSCAPE=inkscape
PSTOPDF=ps2pdf
LATEX=pdflatex

STYLE=styles/beamerthemeNICTA.sty \
      styles/beamerfontthemeNICTA.sty \
      styles/beamercolorthemeNICTA.sty \
      styles/beamercolorthemeNICTAsidebartab.sty \
      styles/beamerinnerthemeNICTA.sty \
      styles/beamerouterthemeNICTA.sty \
      styles/beamerouterthemeNICTA2008.sty \
      styles/beamerouterthemeNICTAtechfest2010.sty
LOGOSBASE=styles/art/logoNICTA. \
	  styles/art/logoACTGovernment. \
	  styles/art/logoANU. \
	  styles/art/logoANU2011. \
	  styles/art/logoDBCDE-ARC. \
	  styles/art/logoGriffithUniversity. \
	  styles/art/logoMelbourneUni. \
	  styles/art/logoNSWDSRD. \
	  styles/art/logoNSWGovernment. \
	  styles/art/logoQUT. \
	  styles/art/logoQueenslandGovernment. \
	  styles/art/logoQueenslandUniversity. \
	  styles/art/logoSydneyUni. \
	  styles/art/logoSydneyUni2011. \
	  styles/art/logoUNSW. \
	  styles/art/logoUNSW2011. \
	  styles/art/logoVictoriaGovernment. \
	  styles/art/logoVictoriaGovernment2011. \

LOGOSPS=$(LOGOSBASE:.=.ps)
LOGOSPDF=$(LOGOSBASE:.=.pdf)
LOGOS=$(LOGOSPS) $(LOGOSPDF)
ARTWORK=styles/art/header.png styles/art/footer.png \
	styles/art/header2010.pdf styles/art/footer2010.pdf

NICTACorporatePresentation_DEPS=NICTACorporatePresentation.tex graphics/nicta-structure.pdf $(wildcard graphics/*.png) graphics/nicta-map.pdf graphics/downarrow_ng.pdf

PACKAGENAME=nictabeamer-$(shell date +%Y%m%d)

all: $(LOGOS) $(ARTWORK) NICTACorporatePresentation.pdf

NICTACorporatePresentation.aux: NICTACorporatePresentation.tex
	TEXINPUTS=styles:styles/art: $(LATEX) -draftmode -interaction nonstopmode $< > /dev/null
NICTACorporatePresentation.pdf: $(NICTACorporatePresentation_DEPS) NICTACorporatePresentation.aux
	TEXINPUTS=styles:styles/art: $(LATEX) -halt-on-error -interaction nonstopmode $< > /dev/null

install: $(LOGOS) $(ARTWORK) 
	$(INSTALL) -m 0755 -d $(DESTDIR)/art
	-$(INSTALL) -m 0644 $(LOGOS) $(ARTWORK) $(DESTDIR)/art
	$(INSTALL) -m 0755 -d $(DESTDIR)/themes/inner
	$(INSTALL) -m 0644 styles/beamerinnerthemeNICTA.sty $(DESTDIR)/themes/inner
	$(INSTALL) -m 0755 -d $(DESTDIR)/themes/outer
	$(INSTALL) -m 0644 styles/beamerouterthemeNICTA.sty $(DESTDIR)/themes/outer
	$(INSTALL) -m 0644 styles/beamerouterthemeNICTAtechfest2010.sty $(DESTDIR)/themes/outer
	$(INSTALL) -m 0644 styles/beamerouterthemeNICTA2008.sty $(DESTDIR)/themes/outer
	$(INSTALL) -m 0755 -d $(DESTDIR)/themes/color
	$(INSTALL) -m 0644 styles/beamercolorthemeNICTA.sty $(DESTDIR)/themes/color
	$(INSTALL) -m 0644 styles/beamercolorthemeNICTAsidebartab.sty $(DESTDIR)/themes/color
	$(INSTALL) -m 0755 -d $(DESTDIR)/themes/font
	$(INSTALL) -m 0644 styles/beamerfontthemeNICTA.sty $(DESTDIR)/themes/font
	$(INSTALL) -m 0755 -d $(DESTDIR)/themes/theme
	$(INSTALL) -m 0644 styles/beamerthemeNICTA.sty $(DESTDIR)/themes/theme
	$(TEXHASH) $(TEXMFHOME)

package: $(PACKAGENAME).tar.bz2
$(PACKAGENAME).tar.bz2: $(STYLE) $(LOGOS) $(ARTWORK) README Makefile $(NICTACorporatePresentation_DEPS)
	test ! -d $(PACKAGENAME)
	for FILE in $^; do\
		DIR=$(PACKAGENAME)/`dirname $$FILE`; \
		mkdir -p $$DIR; \
		cp $$FILE $$DIR; \
	done
	tar cjvf $@ $(PACKAGENAME)
	rm -rf $(PACKAGENAME)

%.ps: %.svg
	$(INKSCAPE) -P $@ $<
%.pdf: %.svg
	$(INKSCAPE) -A $@ $<

%.pdf: %.ps
	$(PSTOPDF) $< $@

clean:
	# XXX: This is a bit too generic...
	rm -f styles/art/*.pdf styles/art/*.ps graphics/nicta-map.pdf graphics/nicta-structure.pdf
	rm -f NICTACorporatePresentation.pdf *.log *.out *.nav *.snm *.toc
	
real-clean: clean
	rm -f *.aux

.PHONY: all install package clean real-clean
