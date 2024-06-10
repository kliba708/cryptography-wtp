import os, sys, time
from transposition import TransCipher

def main():
    input_file = 'woolf.txt'
    output_file = 'woolf_encrypted.txt'
    key = 24
    mode = 'Encrypt' # or 'Decrypt'

    time_start = time.time()

    # check python can actually find the file
    if not os.path.exists(input_file):
        print(f"The file {input_file} does not exist")
        sys.exit()

    # read file
    file_object = open(input_file)
    content = file_object.read()
    file_object.close()

    print(f"{mode}ing {input_file}...")
    
    # TODO: time how long the process takes  

    time_stop = time.time()
    print("Time Elapsed:", (time_stop - time_start))

    # TODO: translate, set to variable translated

    time_start2 = time.time()
    #translated = None

    file_test = TransCipher(content, key)
    file_test.encrypt()

    print(file_test.encrypted)

    translated = file_test.decrypt()
    print(translated)

    time_stop2 = time.time()

    print("Time Elapsed:", (time_stop2 - time_start2))

    # TODO: print how long encryption/decryption took
    
    # write to output file
    output_object = open(output_file, 'w') # write mode
    output_object.write(translated)
    output_object.close()


    print("Done!")

if __name__ == '__main__':
    main()