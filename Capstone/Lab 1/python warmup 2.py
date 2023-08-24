def main():
    num_classes = int(input("How many classes are you taking this semester? "))
    classes = []

    for i in range(num_classes):
        class_name = input(f"Enter the name of class: ")
        classes.append(class_name)

    print("The classes you are taking are:")
    for class_name in classes:
        print(class_name)

    for index, c in enumerate(classes):
        print(f'{index+1} {c}')

if __name__ == "__main__":
    main()


