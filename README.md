# test-s-python

To run this project, you must have python installed in your pc.

## Steps

### Choose where you wanna clone the repo

I have cloned this repo outside my tp directory. Here´s an example:

  - `tp-dir/` This directory represents the tp folder.
      - `bin/`
         - `main`: Is the executable for tp.
        
  - `this_repo/`

### Setup

After `git clone`, open Makefile and check if `PYTHON` and `PIP` are correclty for you environment.

Open `cpp_to_excel.py` file and check if those variables are correclty:

```python
excel_file = "data.xlsx"
# Put your path for tp here
relative_tp_path = "../logic-expressions/bin/"
# As this repository and my tp folder are sibling,
# i just have to comeback one folder to hit the parent and then hit the tp folder.

# Change if is not main
executable_name = "main"

```

Download the sheets and put it on root.

### Running the Project

Run:

```shell
make
``` 
to install pandas and run the tests.

You just need to run `make` once. If you just want to run the tests after build, run:

```shell
make tests
```

### Output

For each failed test, the output will be

```shell
Test "0 | 1 & 2 | ( 3 | 4 )" ee000 failed, expect result was X XXXX and your output is Y YYYYY
Number of failed tests 1

```

If everything has passed, the output will be:

```shell
Number of failed tests 0
```
