
def read_records(No_of=1):
    try:
        f = open('records.txt', 'rt')
        records_list = f.read().split('\n\n')
        no_records = len(records_list)

        count = 0
        for i in records_list:
            if(No_of == 1):
                print(records_list[-2])
                break
            count += 1
            print(i)
            print("-"*4)
            if count == No_of:
                break
        f.close()
    except:
        print()
        print(" [info] There is no records")

def del_records():
    f = open("records.txt", "r+")
    f.truncate(0)
    f.close()