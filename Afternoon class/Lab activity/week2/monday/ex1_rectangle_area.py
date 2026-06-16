def rectangle_area():
  length = float(input("Enter length: "))
  width = float(input("Enter width: "))
  return length * width


if __name__ == "__main__":
  area = rectangle_area()
  print(f"Area of rectangle: {area}")
