with open("test_2.jpg", 'rb') as test:
    file_byte = test.read()
    for byte in file_byte:
        print(byte)
