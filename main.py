# python3

def parallel_processing(n, m, data):
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    output = []
    threads =[0]*n

    for i in range(m):
        min = min(threads)
        thread = threads.index(min)

        output.append((thread, min))
        if i < len(data):
            threads[thread]+=data[i]

    return output


def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n,m =map(int,input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data=list(map(int,input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for pav_index, sak_laiks in result:
        print(pav_index, sak_laiks)


if __name__ == "__main__":
    main()
