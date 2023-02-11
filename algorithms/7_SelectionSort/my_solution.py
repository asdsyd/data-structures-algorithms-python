def selection_sort(arr, choice):
    size = len(arr)
    if choice[0] == 'A':
        for i in range(size - 1):
            min_index = i
            for j in range(min_index + 1, size):
                if arr[j]['First Name'] < arr[min_index]['First Name']:
                    min_index = j
            if i != min_index:
                arr[i], arr[min_index] = arr[min_index], arr[i]

        for i in range(size - 1):
            min_index = i
            for j in range(min_index + 1, size):
                if arr[j]['First Name'] == arr[min_index]['First Name'] and arr[j]['Last Name'] < arr[min_index]['Last Name']:
                    min_index = j
            if i != min_index:
                arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr
    else:
        for i in range(size - 1):
            min_index = i
            for j in range(min_index + 1, size):
                if arr[j]['Last Name'] < arr[min_index]['Last Name']:
                    min_index = j
            if i != min_index:
                arr[i], arr[min_index] = arr[min_index], arr[i]

        for i in range(size - 1):
            min_index = i
            for j in range(min_index + 1, size):
                if arr[j]['Last Name'] == arr[min_index]['Last Name'] and arr[j]['First Name'] < arr[min_index]['First Name']:
                    min_index = j

            if i != min_index:
                arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr


listofd = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]

choice = input('enter sort order(A,B)or (B,A):')
selection_sort(listofd, choice)
for i in listofd:
    print(i)
