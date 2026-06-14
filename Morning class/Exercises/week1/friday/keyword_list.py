# Program to list all Python keywords
import keyword

print("Python Keywords:")
print(keyword.kwlist)
print(f"\nTotal keywords: {len(keyword.kwlist)}")

print("\nFormatted list:")
for kw in keyword.kwlist:
    print(kw, end=", ")