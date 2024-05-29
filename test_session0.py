# DO NOT MAKE CHANGES TO THIS FILE
import pytest
import session0

def test_function_correctness():
  assert session0.myfunc(4, 5) == 9, 'Your function does not work!'

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r', encoding="utf-8") for word in line.split()]
    assert len(readme_words) >= 50, "Make your README.md file interesting! Add at least 100 words"
