PYTHON = python3 
PIP = pip3 
FILE = cpp_to_excel.py

all: build tests clean

build:
	@echo "🚧 Building..."
	$(PIP) install -r requirements.txt

tests:	cpp_to_excel.py
	@echo "🚀 Running tests..."
	$(PYTHON) $(FILE)

clean:
	@echo "🧹 Clearing..."
	rm -rf gmon.out
