KB = 1024
MB = 1048576
GB = 1073741824

num_entries = int(input("Please enter the number of entries per second: "))
entry_size = int(input("Please enter the average number of bytes per entry: "))

kb_size_per_s = (num_entries * entry_size) / KB
mb_size_per_s = (num_entries * entry_size) / MB
gb_size_per_s = (num_entries * entry_size) / GB

print("Storage Estimates")
print(f"Per minute: {kb_size_per_s * 60}KB")
print(f"Per hour: {mb_size_per_s * 60 * 60}MB")
print(f"Per day: {gb_size_per_s * 60 * 60 * 24}GB")
