
unsortarr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
sortarr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arrmin = 1
arrmax = 10

print("Unsorted array: ")
print(unsortarr)

unsortarr.sort()

print("Array after sorting: ")
print(sortarr)

if unsortarr == sortarr:
    print("The array is sorted")
else:
    print("The array is not sorted")

unsortarrmin = min(unsortarr)
unsortarrmax = max(unsortarr)
print("The min value in the array is: ")
print(unsortarrmin)
print("The max value in the array is: ")
print(unsortarrmax)

if arrmin == unsortarrmin and arrmax == unsortarrmax:
    print("These values are correct")
else:
    print("These values are not correct")
