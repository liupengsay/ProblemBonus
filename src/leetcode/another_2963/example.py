import random
import unittest

from solution import standard_procedure, brute_force, brute_force_2
from src.utils.folder_to_zip import zip_folder


random.seed(2023)


class TestGeneral(unittest.TestCase):

    def test_example(self):
        for file in range(1, 11):
            n = random.randint(1, 1000)
            nums = [random.randint(1, 10) for _ in range(n)]
            ans1 = standard_procedure(nums)
            ans2 = brute_force(nums)
            ans3 = brute_force_2(nums)
            with open(f"test_data/example_{file}.in", "w", encoding="utf-8") as fw:
                lst = [f"{n}", " ".join(str(x) for x in nums)]
                fw.write("\n".join(lst))
            with open(f"test_data/example_{file}.out", "w", encoding="utf-8") as fw:
                fw.write(str(ans1))
            assert ans1 == ans2 == ans3
            print(n, ans1)

        for file in range(11, 21):
            n = random.randint(10**5 // (file - 10), 10**5)
            nums = [random.randint(10**9 - n, 10**9) for _ in range(n)]
            ans1 = standard_procedure(nums)
            with open(f"test_data/example_{file}.in", "w", encoding="utf-8") as fw:
                lst = [f"{n}", " ".join(str(x) for x in nums)]
                fw.write("\n".join(lst))
            with open(f"test_data/example_{file}.out", "w", encoding="utf-8") as fw:
                fw.write(str(ans1))
            print(n, ans1)

        zip_folder("test_data", "test_data.zip")
        return


if __name__ == '__main__':
    unittest.main()
