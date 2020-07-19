"""
"Good practices" exercise. Every approach will be contrasted with its counterpart.
"""
# %%

import time
import pandas as pd
import numpy as np

with open('data/udacity/ud090/books_published_last_two_years.txt') as f:
    recent_books = f.read().split('\n')

with open('data/udacity/ud090/all_coding_books.txt') as f:
    coding_books = f.read().split('\n')

start = time.time()
recent_coding_books = []
for book in recent_books:
    if book in coding_books:
        recent_coding_books.append(book)
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))

# Get >500 times improvement with numpy's intersection
start = time.time()
recent_coding_books = np.intersect1d(coding_books, recent_books)
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))


# Get >500 * 3 times improvement with set's intersection
start = time.time()
recent_coding_books = set(coding_books).intersection(recent_books)
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))
