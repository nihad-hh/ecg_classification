import pandas as pd


def compare_labels():
    with (open("../data/training2017/REFERENCE.csv", "r") as ref, \
          open("../data/training2017/REFERENCE-original.csv", "r") as orig, \
          open("../data/training2017/REFERENCE-v3.csv", "r") as v3):
        f_ref = ref.readlines()
        f_orig = orig.readlines()
        f_v3 = v3.readlines()

        print("Comparing v3 with ref")
        counter = 0
        for line in f_v3:
            if line not in f_ref:
                counter = counter + 1

        print(counter)

        counter = 0
        print("Comparing orig with ref")
        for line in f_orig:
            if line not in f_ref:
                counter = counter + 1

        print(counter)

        counter = 0
        print("Comparing orig with v3")
        for line in f_orig:
            if line not in f_v3:
                counter = counter + 1

        print(counter)

# load reference.csv into pd.DataFrame ["signal_name", "label"]
# append individual signals to DataFrame ["signal_name", "signal", "label"]
# preprocessing

reference = pd.read_csv(filepath_or_buffer="../data/training2017/REFERENCE-v3.csv", names=["signal_name", "label"])



print(reference)


