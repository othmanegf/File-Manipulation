import re

# Given text containing product information
text = "P1 est un produit composé de P2 et P3 \nP2 est un produit élémentaire \nP5 est un produit composé de P1 et P4 \nP4 est un produit élémentaire \nP9 est un produit composé de P1, P6 et P4 \nP10 est un produit composé de P3 et P5 \nP11 est un produit composé de P5 et P3 "

# Find products that are elementary
x = re.findall(r"(P\d+ est un produit élémentaire)", text)
for i in x:
    print(i)

# Find products that are composed of other products
p = re.findall(r"(P\d+ est un produit composé de P\d+, P\d+ et P\d)", text)
print(*p)

# Find products that are composed of specific products (P3 and P5)
v = re.findall(r"(P\d+ est un produit composé de P3 et P5)", text)
v += re.findall(r"(P\d+ est un produit composé de P5 et P3)", text)
for i in v:
    print(i)

# Find products that are composed of products other than P2
r = re.findall(r"(P\d+ est un produit composé+) de P[^2]", text)
for i in r:
    print(i)

# Find products that are composed of specific products (P1, P6, and P4)
s = re.findall(r"(P9 est un produit composé de P\d+, P\d+ et P\d)", text)
for i in s:
    print(i)