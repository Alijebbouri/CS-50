def get_size():
    size = int(input('size ?'))
    while size > 1:
        return size
def print_grid(size):
    for i in range(size):
        print('#'*size)
            
def main():
    s = get_size()
    grid_size = print_grid(s)
    print(get_size)
main()

