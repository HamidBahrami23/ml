import os

# ---- CONFIG ----
folder = "/home/hamid/ML/Datasets/Men-Women/traindata/traindata/men/"
category = "men"   # change to "women" for the other folder

# ---- RENAME ----
files = sorted(os.listdir(folder))  # sorts to rename in stable order

i = 1
for filename in files:
    # skip hidden files or non-images
    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        continue
    
    old_path = os.path.join(folder, filename)
    new_name = f"{category}.{i}.jpg"
    new_path = os.path.join(folder, new_name)

    os.rename(old_path, new_path)
    print(f"Renamed: {filename} --> {new_name}")

    i += 1

print("Done!")