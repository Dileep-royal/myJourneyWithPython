# random module

The name itself speaks for it, it used to pick random data, to get a random number between a range, to shuffle the data and to create a dummy data.

## **Different methods:**

### random()

This allows us to get a random floating point value between 0(inclusive) and 1(exclusive)

```python
rand=random.random()  # gives us a random floating point between 0 and 1(exclusive)
print(rand)
```

**OUTPUT:** 0.025500358743770102

### uniform()

This allows us to get a random floating point value between a specified range starting is inclusive and ending are exclusive.

```python
rand=random.uniform(0,10)  # gives us a random floating point in a specified range.
print(rand)
```

**OUTPUT:**  2.9719022299691336

### randint()

This allows us to get a random value between a specified range both starting and ending are inclusive.

```python
rand=random.randint(0,10) # gives us a random integer in a specified range inclusively.
print(rand)
```

**OUTPUT:**  7

### choice()

This allows us to randomly pick a one choice from a sequence.

```python
sequence=["Violet","Blue","Green","Yellow","Orange","Red"]
choice=random.choice(sequence)        
print(choice)                 # gives us a random item from the sequence list
```

**OUTPUT:**  Red

### choices()

- This allows us to randomly pick a choice k number of times from a sequence.
- K arguments is set to choose k number of time choices
- This method also have weights argument to set how likely a item is choose from a sequence.

In the below code, the colors Blue, Orange, Yellow repeats mostly.

```python
choices=random.choices(sequence,weights=[10,87,9,45,82,8],k=10)  # gives us a random k number of items from the list
print(choices)
```

**OUTPUT:**  ['Orange', 'Orange', 'Blue', 'Blue', 'Orange', 'Orange', 'Orange', 'Violet', 'Yellow', 'Blue']

### shuffle()

- to shuffle the data in a sequence.

```python
random.shuffle(sequence)  # shuffles the items in a sequence
print(sequence)
```

**OUTPUT:**  ['Red', 'Green', 'Violet', 'Blue', 'Yellow', 'Orange']

### sample()

- Sample() is used to get a unique data from a sequence and it is unlike of choices() method it won’t give you repetitive data.
- It also have k argument to get k no. of sample data.

```python
sample=random.sample(sequence,k=4)   # gives us a sample unique values from a sequence unlike the choices() method i.e.; it gives us repititive values
print(sample)
```

**OUTPUT:**  ['Violet', 'Red', 'Yellow', 'Orange']