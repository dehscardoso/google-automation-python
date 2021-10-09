# If a filesystem has a block size of 4096 bytes, this means that a file comprised of 
# only one byte will still use 4096 bytes of storage. A file made up of 4097 bytes will 
# use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the calculate_storage 
# function below, which calculates the total number of bytes needed to store a file of a given size?

def calculate_storage(filesize):
    block_size = 4096
    full_blocks = filesize // block_size
    partial_block_remainder = filesize % block_size
    if partial_block_remainder > 0:
        return block_size * (full_blocks + 1)
    return block_size * full_blocks

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192