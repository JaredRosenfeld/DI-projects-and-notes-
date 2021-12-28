def box_printer(*strings):
    print("******************")
    for word in strings:
        t = 15 - len(word)
        spaces = " " * t
        print(f"* {word}{spaces}*")
    print("******************")


box_printer("Hello", "World", "in", "reallylongword", "a", "frame")





def insertion_sort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)