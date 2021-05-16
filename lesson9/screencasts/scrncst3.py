def main():
    #for i in map(func, [1,2,3,4,5]):
    for i in filter(lambda x: x%2, [1,2,3,4,5]):
        print(i)

if __name__ == '__main__':
    main()
