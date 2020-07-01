
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Sum of elements in the dictionary is 600\n"
     ]
    }
   ],
   "source": [
    "#Python program to sum all the items in a dictionary\n",
    "def returnSum(myDict):\n",
    "    sum = 0\n",
    "    for i in myDict: \n",
    "        sum = sum + myDict[i] \n",
    "    return sum\n",
    "dict1={'a':100,'b':200,'c':300} \n",
    "print(\"The Sum of elements in the dictionary is\",returnSum(dict1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "It is dictionary with the use of Integer Keys: \n",
      "{1: 'One', 2: 'Two', 3: 'Three'}\n",
      "\n",
      "It is dictionary with the use of Mixed Keys: \n",
      "{'Name': 'Shaik', 1: [1, 2, 3, 4]}\n"
     ]
    }
   ],
   "source": [
    "#Python program to demonstrate accessing an element from a Dictionary\n",
    "dict2={1:'One',2:'Two',3:'Three'} \n",
    "print(\"\\nIt is dictionary with the use of Integer Keys: \") \n",
    "print(dict2)\n",
    "dict3={'Name':'Shaik',1:[1, 2, 3, 4]} \n",
    "print(\"\\nIt is dictionary with the use of Mixed Keys: \") \n",
    "print(dict3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Concatenated dictionary is:\n",
      "{'A': 1, 'B': 2, 'C': 3}\n"
     ]
    }
   ],
   "source": [
    "#Python program to concate two dictionaries\n",
    "d1={'A':1,'B':2}\n",
    "d2={'C':3}\n",
    "d1.update(d2)\n",
    "print(\"Concatenated dictionary is:\")\n",
    "print(d1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Current Dict is:  {'key1': 'Shaik', 'key2': 'Afridi'}\n",
      "Updated Dict is:  {'key1': 'Shaik', 'key2': 'Captain', 'key3': 'America'}\n"
     ]
    }
   ],
   "source": [
    "#Python program to add keys/values in a dictionary (update dictionary)\n",
    "dict = {'key1':'Shaik','key2':'Afridi'} \n",
    "print(\"Current Dict is: \",dict) \n",
    "dict['key2'] ='Captain'\n",
    "dict['key3'] ='America'\n",
    "print(\"Updated Dict is: \", dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "len() method : 3\n",
      "len() method with keys() : 3\n",
      "len() method with values() : 3\n"
     ]
    }
   ],
   "source": [
    "#Python program to find the length of a dictionary in Python?\n",
    "dict1 ={'Name':'Shaik','Age':19,'Course':'CSE'}  \n",
    "print(\"len() method :\", len(dict1)) \n",
    "print(\"len() method with keys() :\", len(dict1.keys())) \n",
    "print(\"len() method with values() :\", len(dict1.values()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'a': 1, 'b': 2, 'c': 3, 'd': 4}\n",
      "{'b': 2, 'c': 3, 'd': 4}\n"
     ]
    }
   ],
   "source": [
    "#Python program to remove items from the dictionary in Python\n",
    "dict6={'a':1,'b':2,'c':3,'d':4}\n",
    "print(dict6)\n",
    "if 'a' in dict6: \n",
    "    del dict6['a']\n",
    "print(dict6)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}