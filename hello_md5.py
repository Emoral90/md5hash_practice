import hashlib


def hash(mes):
    # Encode(translaate) the string to bytes
    mes_bytes = mes.encode()

    # Create md5 hash object
    md5_hash = hashlib.md5(mes_bytes)

    # Save hexidecimal representation of object
    hexidigest = md5_hash.hexdigest()
    return hexidigest

def verify_hash(str_to_chk, og_hash):
    # Get hash object of string to check from Main 
    return hash(str_to_chk) == og_hash

def main():
    # input string to hash
    mes = "Hello World!"

    # save hexidecimal value of hash to variable
    hashed_val = hash(mes)
    print(hashed_val)

    # Compare string to previous hash value
    # print(verify_hash("Hello world!", hashed_val))
    print(verify_hash(mes, hashed_val))


if __name__ == "__main__":
    main()