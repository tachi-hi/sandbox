#
# This script executes
# all the `makefile' in all the subdirectory.
#

SUBMAKE = $(wildcard ./*/makefile)
SUBDIR = $(subst /makefile, , $(SUBMAKE) )

define applySubdir
	for directory in $(SUBDIR); do\
		make $1 -C $${directory}; \
	done
endef

.PHONY: all 
all: 
	$(call applySubdir, all)

.PHONY: pdf
pdf: 
	$(call applySubdir, pdf)

.PHONY: clean
clean:
	$(call applySubdir, clean)

