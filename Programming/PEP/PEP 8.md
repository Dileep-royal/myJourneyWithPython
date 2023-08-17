# PEP 8

PEP stands for **Python Enhancement Proposal**. A PEP is a technical design doc for the Python community which describes a new feature for the language itself, its processes, or its environment.

We need PEP-8 to enhance Readability  “Readability counts.”

1. **Naming Conventions**

> **“**Explicit is better than implicit.**”**
> 
- **Naming Styles**

      Choosing names for identifiers that makes your code more readable and make sense to reader.

1. **Code Layout**

> **“**Beautiful is better than ugly.**”**
> 
- **Blank Lines** - Surround top-level functions and classes with two blank lines and Surround method definitions inside classes with a single blank line.
- **Maximum Line Length**  - lines should be limited to 79 characters.
- **Line Breaking** - use backslash(\) to imply continuation.

1. ****Indentation****

> **“**There should be one—and preferably only one—obvious way to do it.**”**
> 

**Indentation** determines how statements are grouped together.

Use 4 consecutive spaces to indicate indentation.

1. **Comments**

> **“**If the implementation is hard to explain, it’s a bad idea.**”**
> 

**Comments** are used to document code you are written.

- **Block Comments** - Use block comments to document a small section of code. (**#**)
- **Inline Comments** - Inline comments explain a single statement in a piece of code. (**#**)
- ****Documentation Strings**** - ********Use this to explain and document a specific block of code. (**“””**)

1. ****Whitespace in Expressions and Statements****

> **“**Sparse is better than dense.**”**
> 

****Whitespace Around Binary Operators**** - ********Use whitespaces before and after the binary operators.

## Linters

Linters are programs that analyze code and flag errors. They provide suggestions on how to fix the error. Linters are particularly useful when installed as extensions to your text editor, as they flag errors and stylistic problems while you write.

Some Examples are:

- **`[pycodestyle](https://pypi.org/project/pycodestyle/)`**
- **`[flake8](https://pypi.org/project/flake8/)`** is a tool that combines a debugger, `pyflakes`, with `pycodestyle`.

## ****Auto formatters****

Refactor your code to conform with PEP 8 automatically.

> `[black](https://pypi.org/project/black/)`, which autoformats code following *most* of the rules in PEP 8.
> 

## Resources

- Refer [Documentation](https://peps.python.org/pep-0008/)