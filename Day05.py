import hashlib

DOOR_ID = "ugkcyxxp"
PART_1 = ""
PART_2 = [None] * 8
count = 0

for i in range(100000000):
    current = DOOR_ID + str(i)
    hash = hashlib.md5(current.encode("utf-8")).hexdigest()

    # Part 1
    if hash[:5] == "00000" and len(PART_1) < 8:
        PART_1 += hash[5]
    
    # Part 2
    if hash[:5] == "00000" and hash[5].isdigit() and int(hash[5]) < 8 and PART_2[int(hash[5])] is None:
        idx = int(hash[5])
        PART_2[idx] = hash[6]
        count += 1
    
    if len(PART_1) == 8 and count == 8:
        break


print("PART_1", PART_1)
print("PART_2", "".join(PART_2))


