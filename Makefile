PYTHON = python3 
FILE = cpp_to_excel.py

all: tests clean

tests:	cpp_to_excel.py
	$(PYTHON) $(FILE)

clean:
	@echo "🧹 Clearing..."
	rm -rf gmon.out
