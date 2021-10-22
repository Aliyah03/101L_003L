def min_mpg():
    while True:
        try:
            minimum_mpg=float(input("Enter the minimum mpg ==> "))
            if minimum_mpg<0:
                print('Fuel economy given must be greater than 0')
            elif minimum_mpg>100:
                print('Fuel economy must be less than 100')
            else:
                return minimum_mpg
        except:
            print('You must enter a number for the fuel economy')

def input_file():
    while True:
        filename=input('Enter the name of the input vehicle file ==> ')
        try:
            with open(filename,'r') as read_file:
                return [[data.strip() for data in line.strip().split('\t')] for line in read_file.readlines()]

        except:
            print('Could not open file',filename)



def output_file(minimum_mileage,fileinfo):
    while True:
        try:
            filename = input('Enter the name of the file to output to ==> ')
            with open(filename,'w') as write_file:
                for data in fileinfo:
                    try:
                        if minimum_mileage>=float(data[7]):
                            write_file.write('{0:<5}{1:<40}{2:<40}{3:>10}\n'.format(data[0],\
                            data[1],data[2],data[7]))
                    except:
                        print('Could not convert value invalid for vehicle',data[0],data[1],data[2])
        except:
            print('There is an IO Error',filename)


if __name__ == "__main__":
    minimum_mileage=min_mpg()
    fileinfo=input_file()[1:]
    output_file(minimum_mileage,fileinfo)