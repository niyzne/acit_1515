# ================================
# == NOT FINISHED AT THE MOMENT ==
# ================================

KB = 1024
MB = 1048576
GB = 1073741824

num_entries = input("Please enter the number of entries per second: ")
entry_size = input("Please enter the average number of bytes per entry: ")

float_num_entries = float(num_entries)
float_entry_size = float(entry_size)

kb_size = (float_num_entries * float_entry_size) / KB

print("Storage Estimates")
print(f"Per minute: {kb_size}KB")

# ================================
# == NOT FINISHED AT THE MOMENT ==
# ================================
