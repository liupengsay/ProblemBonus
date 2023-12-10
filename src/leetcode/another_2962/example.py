import random
import unittest

from solution import count_subarrays, count_subarrays_brute_force
from src.utils.folder_to_zip import zip_folder

random.seed(2023)


class TestGeneral(unittest.TestCase):

    def test_example(self):
        for file in range(1, 11):
            n = random.randint(1, 1000)
            nums = [random.randint(1, 10) for _ in range(n)]
            k = random.randint(1, 10)
            ans1 = count_subarrays(nums, k)
            ans2 = count_subarrays_brute_force(nums, k)
            with open(f"test_data/example_{file}.in", "w", encoding="utf-8") as fw:
                lst = [f"{n} {k}", " ".join(str(x) for x in nums)]
                fw.write("\n".join(lst))
            with open(f"test_data/example_{file}.out", "w", encoding="utf-8") as fw:
                fw.write(str(ans1))
            assert ans1 == ans2
            print(n, ans1, ans1 >= 2**32 - 1)

        for file in range(11, 21):
            n = random.randint(100000 // (file - 10), 100000)
            nums = [random.randint(100000 // (file - 10), n) for _ in range(n)]
            k = random.randint(1, 5)
            ans1 = count_subarrays(nums, k)
            with open(f"test_data/example_{file}.in", "w", encoding="utf-8") as fw:
                lst = [f"{n} {k}", " ".join(str(x) for x in nums)]
                fw.write("\n".join(lst))
            with open(f"test_data/example_{file}.out", "w", encoding="utf-8") as fw:
                fw.write(str(ans1))
            print(n, ans1, ans1 >= 2**32 - 1)

        zip_folder("test_data", "test_data.zip")
        return


if __name__ == '__main__':
    unittest.main()
