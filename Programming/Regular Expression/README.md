# re module

- re module is used to retrieve matches of a specific pattern in a file or string.
- pattern is formed using ASCII letters, digits and Meta Characters.
- Here the ASCII letters are case-sensitive.
- Meta Characters have special meaning. In order to override the special meaning we need to use escape character i.e.; by using Back slash(\).

| Meta Characters |                                    Special meaning |
| --- | --- |
|       Anchors |  |
|            ^ | Used to match starting of a String and negates when used in a char set |
|            $ | Used to match ending of a String |
|    Quantifiers |  |
|            * | Matches 0 or more characters |
|            + | Matches 1 or more characters |
|             ? | Matches exactly 0 or one |
|           {n} | Matches exactly n characters |
|     {min, max} | matches a range of characters |
|     Char set |  |
|            [] | Matches only single characters that specified with in the bracket |
|           [^] | Matches characters, which are NOT in a bracket |
|      Groups |  |
|            () | Creates a group of choices of a character(s) |
|             \| | Either or  ,this acts a separator in a group |
|  |  |
|           /d | matches digit (0-9) |
|           /D | matches everything except digits (0-9) |
|           /w | matches word characters (a-b, A-Z, 0-9 ,_) |
|           /W | matches not word characters |
|           /s | matches space characters (space, tab, new line) |
|           /S | matches not space characters |
|           /b | matches word boundary |
|           /B | matches not word boundary |
|  |  |
|             \ | used as escape character for meta characters. |
|            . | matches every character except new line |
|  |  |

### re.compile()

- Creates a pattern and lets us store this pattern in an object.
- This object later can be used to perform multiple searches using different methods.
- We use a raw string to pass the pattern.
- raw string is a string prefixed with r. This allows us to override the meaning of tab, new line, etc.
- We can also do the pattern matching without using compile() method by simply passing pattern and search text as two arguments respectively to finditer() method as shown below.

```python
matches=re.finditer(r"M(r|s|rs)\.?\s[A-Z]\w*",content)
```

### finditer()

- This method can be performed on compile() object.
- gives us an iteration list and each iteration looks like as shown below.
- finditer() return a matched pattern with some extra information.
- The result of finditer() object allows us to use some methods i.e; group, groups, span, start, end.

```python
<re.Match object; span=(72, 84), match='321-555-8736'>
```

## Examples:

**details.txt file:**

```
Mr. Dileep
234-536-7262
Ms Dileep
827*272*2921
Mrs. Dileep
918.292.0981
Mr Nagraju
928.292.2289
Mrs. Nagraju
393,983,2983
Mrs T
839:938:9292
Mr. Reddappa
928-287-2898
```

1. Write a regular expression to extract Names along with honorifics like Mr. , Ms. and Mrs.

### Code:

```python
import re
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
with open("details.txt","r") as file1:
    content=file1.read()
    matches=pattern.finditer(content)
    # matches=re.finditer(r"M(r|s|rs)\.?\s[A-Z]\w*",content)
    for match in matches:
        print(match.group())
```

### Output:

```
Mr. Dileep
Ms Dileep
Mrs. Dileep
Mr Nagraju
Mrs. Nagraju
Mrs T
Mr. Reddappa
```

1. Write a regular Expression to extract phone numbers from a file.

### Code:

```python
import re
pattern = re.compile(r'/d{3}./d{3}./d{4}')
with open("details.txt","r") as file1:
    content=file1.read()
    matches=pattern.finditer(content)
    for match in matches:
        print(match.group())
```

### Output:

```python
234-536-7262
827*272*2921
918.292.0981
928.292.2289
393,983,2983
839:938:9292
928-287-2898
```

1. Write a regular Expression to match mail pattern from a string.

### Code:

```python
import re

mails='''
dileeproyal4243@gmail.com
dileep.dev@university.edu
aswini-ashu@yahoo.com
surendra-royal@my-work.net
'''

pattern=re.compile(r"[a-zA-Z0-9-.]+@[a-zA-Z-]+\.[a-zA-Z]+")
matches=pattern.finditer(mails)

for match in matches:
    print(match.group())
```

### Output:

```python
dileeproyal4243@gmail.com
dileep.dev@university.edu
aswini-ashu@yahoo.com
surendra-royal@my-work.net
```

### groups()

- groups() method allows us to print a tuple of groups.

### group()

- group() method allows us to fetch the each group value by passing group number.
- By default group index is set to 0, which contains whole content.

1. Write a regular Expression to create groups from a string and fetch each group.

```python
import re

urls='''
https://www.google.com
http://dileep.com
https://www.youtube.com
https://nasa.gov
'''

pattern=re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
matches=pattern.finditer(urls)

for match in matches:
    print(match.groups())    # prints a tuple of groups
print()
for match in matches:
    print(match.group(2))    # prints domain names
    print()
    print(match.group(3))    # prints domain extensions
    print()
```

### Output:

```python
('www.', 'google', '.com')
(None, 'dileep', '.com')
('www.', 'youtube', '.com')
(None, 'nasa', '.gov')

google

.com

dileep

.com

youtube

.com

nasa

.gov
```

### sub()

- Used to fetch a particular groups from a compile() method object.
- sub() method accepts two arguments. one is regular expression to specify groups and second is to pass string.

1. By using Back referencing of a group Create a sub URL with domain name and domain extension.

### Code:

```python
import re

urls='''
https://www.google.com
http://dileep.com
https://www.youtube.com
https://nasa.gov
'''

pattern=re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
subbed_url=pattern.sub(r"\2\3",urls)
print(subbed_url)
```

### Output:

```python
google.com
dileep.com
youtube.com
nasa.gov`
```

### findall()

- findall() is used to get all match occurrences of a given pattern
- It won’t provide us with extra information like finditer() do.

### match()

- match() method only looks for the match of the pattern at the beginning of the string.

### search()

- search() is used to get the first match occurrence of a given pattern.
- Gives us the Match object that have extra information.

### flags:

|           Flag  |                   Use Case |
| --- | --- |
| IGNORECASE / I | To make a pattern case insensitive |
| ASCII / A | To match only ASCII Characters |
| VERBOSE / X | Ignores Comments, White spaces and Line breaks |
| LOCALE / L |  |
| MULTILINE / M | Allows us to search on new lines also |
| DOTALL / S | Allow us to match line breaks and also continues to search in new line |

# Resource

- YouTube [**video**](https://youtu.be/K8L6KVGG-7o) from Corey Schafer Channel.
- [**Article**](https://www.geeksforgeeks.org/python-flags-to-tune-the-behavior-of-regular-expressions/) to learn about Regex Flags.
