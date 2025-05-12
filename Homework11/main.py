from math_operations import add, subtract
from my_string_utils import reverse_string, count_vowels
from geometry.circle import calculate_area, calculate_circumference
from file_operations import write_file, read_file

print(add(2, 3))
print(reverse_string("hello"))
print(count_vowels("hello world"))
print(calculate_area(4))
print(calculate_circumference(4))

write_file("test.txt", "Hello file!")
print(read_file("test.txt"))
