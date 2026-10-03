import numpy as np
class DataAnalytics:
    def __init__(self):
        self.__array = None
    def __check_array(self):
        if self.__array is None:
            print("\nPlease create a NumPy Array first.")
            return False
        return True
    def create_array(self):
        print("Select the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        try:
            choice=int(input("Enter your choice:"))
            match choice:
                case 1:
                    values = list(map(int,input(" Enter elements separated by space: ").split()))
                    self.__array = np.array(values)
                case 2:
                    rows = int(input("Enter the number of rows:"))
                    columns = int(input("Enter the number of columns:"))
                    values = list(map(int,input(f"Enter {rows*columns} elements for the array separated by space:").split()))
                    if len(values) != rows * columns:
                        print("Invalid number of elements.")
                        return
                    self.__array = np.array(values).reshape(rows,columns)
                case 3:
                    depth= int(input("Enter the depth:"))
                    rows = int(input("Enter the number of rows:"))
                    columns = int(input("Enter the number of columns:"))
                    values = list(map(int,input(f"Enter {depth*rows*columns} elements for the array separated by space:").split()))
                    if len(values) != depth*rows * columns:
                        print("Invalid number of elements.")
                        return
                    self.__array = np.array(values).reshape(depth,rows,columns)
                case _:
                    print("Invalid choice")
                    return
            print("Array created successfully:")
            print(self.__array)
        except ValueError:
            print("Invalid input! Please enter numbers only.")
    def indexing(self):
        if not self.__check_array():
            return
        if self.__array.ndim ==1:
            i = int(input("Enter the index:"))
            print("Element:",self.__array[i])
        elif self.__array.ndim == 2:
            ri = int(input("Enter the row index:"))
            ci = int(input("Enter the column index:"))
            print("Element:",self.__array[ri,ci])
        elif self.__array.ndim==3:
            di = int(input("Enter the depth index:"))
            ri = int(input("Enter the row index:"))
            ci = int(input("Enter the column index:"))
            print("Element:",self.__array[di,ri,ci])
        else:
            print("Invalid choice!")
    def slicing(self):
        if not self.__check_array():
            return
        if self.__array.ndim==1:
            start = int(input("Enter the start index:"))
            end = int(input("Enter the end index:"))
            print("\nSliced Array:")
            print(self.__array[start:end])
        elif self.__array.ndim == 2:
            r1,r2 = map(int,input("Enter the row range (start:end):").split(":"))
            c1,c2 =map(int,input("Enter the column range (start:end):").split(":"))
            print("\nSliced Array:")
            print(self.__array[r1:r2,c1:c2])
        elif self.__array.ndim == 3:
                    d_start = int(input("Enter the depth start:"))
                    d_end =int(input("Enter the depth end:"))
                    print("\nSliced Array:")
                    print(self.__array[d_start:d_end])
        else:
            print("Invalid choice!")
    def mathematical_operations(self):
        if not self.__check_array():
            return
        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        try:
            choice = int(input("Enter your choice:"))
            match choice:
                case 1:
                    try:
                        values = list(map(int, input(f"Enter the same-size array elements ({self.__array.size} elements separated by space):").split()))
                        if len(values)!=self.__array.size:
                            print("Invalid number of elements.")
                            return
                        second_arr = np.array(values).reshape(self.__array.shape)
                        print("\nOriginal Array:")
                        print(self.__array)
                        print("\nSecond Array:")
                        print(second_arr)

                        result = self.__array + second_arr
                        print("\nResult of Addition:")
                        print(result)
                    except ValueError:
                        print("Invalid input! Please enter number only.")

                case 2:
                    try:
                        values = list(map(int, input(f"Enter the same-size array elements ({self.__array.size} elements separated by space):").split()))
                        if len(values)!=self.__array.size:
                            print("Invalid number of elements.")
                            return
                        second_arr = np.array(values).reshape(self.__array.shape)
                        print("\nOriginal Array:")
                        print(self.__array)
                        print("\nSecond Array:")
                        print(second_arr)
                        
                        result = self.__array - second_arr
                        print("\nResult of Subtraction:")
                        print(result)
                    except ValueError:
                        print("Invalid input! Please enter numbers only.")

                case 3:
                    try:
                        values = list(map(int, input(f"Enter the same-size array elements ({self.__array.size} elements separated by space):").split()))
                        if len(values)!=self.__array.size:
                            print("Invalid number of elements.")
                            return
                        second_arr = np.array(values).reshape(self.__array.shape)
                        print("\nOriginal Array:")
                        print(self.__array)
                        print("\nSecond Array:")
                        print(second_arr)
                                        
                        result = self.__array * second_arr
                        print("\nResult of Multiplication:")
                        print(result)
                    except ValueError:
                        print("Invalid input! Please enter numbers only.")

                case 4:
                    try:
                        values = list(map(int, input(f"Enter the same-size array elements ({self.__array.size} elements separated by space):").split()))
                        if len(values)!=self.__array.size:
                            print("Invalid number of elements.")
                            return
                        second_arr = np.array(values).reshape(self.__array.shape)
                        print("\nOriginal Array:")
                        print(self.__array)
                        print("\nSecond Array:")
                        print(second_arr)
                        if np.any(second_arr == 0):
                            print("Division by Zero is not allowed.")
                            return                       
                        result = self.__array / second_arr
                        print("\nResult of Division:")
                        print(result)
                    except ValueError:
                        print("Invalid input! Please enter numbers only.")
                case _:
                    print("Invalid choice!")
        except ValueError:
            print("Invalid Choice! Please enter a number.")
    def combine_arrays(self):
        if not self.__check_array():
            return
        try:
            values = list(map(int,input(f"Enter the elements of another array to combine ({self.__array.size} elements separated by space):").split()))
            if len(values)!=self.__array.size:
                print("Invalid number of elements.")
                return
            second_arr = np.array(values).reshape(self.__array.shape)
            print("\nOriginal Array:")
            print(self.__array)
            print("\nSecond Array:")
            print(second_arr)
            print("\nCombined Array:")
            if self.__array.ndim == 2:
                result = np.vstack((self.__array,second_arr))
                print(result)
            else:
                result = np.concatenate((self.__array,second_arr))
                print(result)
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            return 
    def split(self):
        if not self.__check_array():
            return
        try:
            parts = int(input("\nEnter number of parts: "))
            if parts <=0:
                print("Number of parts must be greater than 0.")
                return
            if self.__array.shape[0]% parts!=0:
                print("Array cannot be split equally into these parts.")
                return
            result = np.split(self.__array,parts,axis=0)
            print("\nSplit Array:")
            num = 1
            for part in result:
                print(f"\npart {num}:\n{part}")
                num +=1
        except ValueError:
            print("Invalid input! Please enter a number.")
            return
    def search(self):
        if not self.__check_array():
            return
        try:
            value = int(input("\nEnter value to search: "))
            pos = np.where(self.__array == value)
            if len(pos[0]) > 0:
                print("Value found at:",pos)
            else:
                print("Value not found.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    def sort(self):
        if not self.__check_array():
            return
        print("\nOriginal Array:")
        print(self.__array)
        result = np.sort(self.__array,axis=-1)
        print("\nSorted Array:")
        print(result)
        print("(Sorting applied row-wise.)")
    def filter_value(self):
        if not self.__check_array():
            return
        print("\nFilter condition:")
        print("1. Greater than")
        print("2. Less than")
        print("3. Equal to")
        print("4. Greater than or equal to")
        print("5. Less than or equal to")
        try:
            choice = int(input("Enter your choice: "))
            value = int(input("Enter value: "))
            match choice:
                case 1:
                    result = self.__array[self.__array > value]
                    print("\nFiltered Values:")
                    print(result)
                case 2:
                    result = self.__array[self.__array < value]
                    print("\nFiltered Values:")
                    print(result)
                case 3:
                    result = self.__array[self.__array == value]
                    print("\nFiltered Values:")
                    print(result)
                case 4:
                    result = self.__array[self.__array >= value]
                    print("\nFiltered Values:")
                    print(result)
                case 5:
                    result = self.__array[self.__array <= value]
                    print("\nFiltered Values:")
                    print(result)
                case _:
                    print("Invalid choice.")
        except ValueError:
            print("Invalid input! Please enter a number.")

           
    def aggregates_statistics(self):
        if not self.__check_array():
            return
        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum")
        print("7. Maximum")
        print("8. Percentiles")
        print("9. Correlation")
        try:
            choice = int(input("Enter your choice:"))
            match choice :
                case 1:
                    print("\nOriginal Array:")
                    print(self.__array)
                    print("\nSum of Array:", np.sum(self.__array))
                case 2:
                    print("\nOriginal Array:")
                    print(self.__array)
                    print("\nMean of Array:", np.mean(self.__array))
                case 3:
                    print("\nOriginal Array:")
                    print(self.__array)
                    print("\nMedian of Array:", np.median(self.__array))
                case 4:
                    print("\nOriginal Array:")
                    print(self.__array)
                    print("\nStandard Deviation of Array:", np.std(self.__array))
                case 5:
                    print("\nOriginal Array:")
                    print(self.__array)
                    print("\nVariance of Array:", np.var(self.__array))
                case 6:
                    print("\nOriginal Array:")
                    print(self.__array)
                    print("\nMinimum Value:", np.min(self.__array))
                case 7:
                    print("\nOriginal Array:")
                    print(self.__array)
                    print("\nMaximum Value:", np.max(self.__array))
                case 8:
                    print("\nOriginal Array:")
                    print(self.__array)
                    p = float(input("Enter the percentile you want to calculate (0-100):"))
                    if p< 0 or p>100:
                        print("Percentile must be between 0 and 100.")
                        return
                    print(f"\n{p}% percentile:", np.percentile(self.__array,p))
                case 9:
                    if self.__array.ndim != 1:
                        print("\nCorrelation requires a 1D array.")
                        return
                    print("\nEnter another array for correlation:")
                    elements = list( map(int, input().split()))
                    second_array = np.array(elements)
                    if len(second_array) != len(self.__array):
                        print("Both arrays must have the same size.")
                        return
                    correlation = np.corrcoef(self.__array,second_array)
                    print("\nCorrelation Matrix:")
                    print(correlation)
                case _:
                    print("Invalid choice!")
        except ValueError:
            print("Invalid input! Please enter a number.")
    @classmethod
    def info(cls):
        print("\nNumPy Analyzer")
        print("Developed using NumPy and OOP concepts.")
    @staticmethod
    def show_dimensions():
        print("\nNumPy supports:")
        print("1D Array")
        print("2D Array")
        print("3D Array")
    
def main():
    analyzer = DataAnalytics()
    DataAnalytics.info()
    print("\nWelcome to the NumPy Analyzer!")
    while True:
        print("Choose an option:")
        print("1. Create a NumPy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")
        try:
            choice = int(input("Enter your choice:"))
            match choice:
                case 1:
                    analyzer.create_array()
                    while True:
                        print("choose an operation:")
                        print("1.Indexing")
                        print("2.Slicing")
                        print("3.Go Back")
                        choice1 = int(input("Enter your choice:"))
                        match choice1:
                            case 1:
                                analyzer.indexing()
                            case 2:
                                analyzer.slicing()
                            case 3:
                                break
                            case _:
                                print("Invalid choice!")
                case 2:
                    analyzer.mathematical_operations()
                case 3:
                    print("Choose an option:")
                    print("1.Combine Arrays")
                    print("2.Split Array")
                    print("3.Go Back:")
                    option = int(input("Enter your choice:"))
                    match option:
                        case 1:
                            analyzer.combine_arrays()
                        case 2:
                            analyzer.split()
                        case 3:
                            pass
                        case _:
                            print("Invalid choice!")
                case 4:
                    print("Choose an option:")
                    print("1.Search a value:")
                    print("2.Sort the Array")
                    print("3.Filter values")
                    option1 = int(input("enter your choice:"))
                    match option1:
                        case 1:
                            analyzer.search()
                        case 2:
                            analyzer.sort()
                        case 3:
                            analyzer.filter_value()
                        case _:
                            print("Invalid choice!")
                case 5:
                    analyzer.aggregates_statistics()
                case 6:
                    print("Thank you for using NumPy Analyzer! Goodbye!")
                    break
                case _:
                    print("Invalid choice!")
        except ValueError:
            print("Invalid input! Please enter numbers only.")
if __name__ == "__main__":
    main()
