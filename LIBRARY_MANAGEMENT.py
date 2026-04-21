lib_books={
    "MATHS":{"CLASS 10 MATHS":{"QUANTITY":100},"CLASS 12 MATHS":{"QUANTITY":50}},
    "SCIENCE":{"CLASS 10 SCIENCE":{"QUANTITY":100},"CLASS 12 SCIENCE":{"QUANTITY":50}}
}
quantity=0
for i in lib_books:
    for j in lib_books[i]:
        quantity+=lib_books[i][j]["QUANTITY"]
print("Total quantity of books in the library:", quantity)
subject=input("enter subject:")
class_=input("enter class:")
quantity=input("enter quantity:")
lib_books[subject][class_]={"QUANTITY":quantity}
print(lib_books)