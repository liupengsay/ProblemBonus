import random
import unittest

from solution import standard_procedure, brute_force
from src.utils.folder_to_zip import zip_folder

random.seed(2024)


class TestGeneral(unittest.TestCase):

    def test_example(self):
        for file in range(1, 11):
            if file == 1:
                n = 2
                edges = [(0, 1, 2)]
            elif file == 2:
                n = 3
                edges = [(0, 1, 1), (1, 2, 1)]
            elif file == 9:
                n = 1000
                edges = []
                for i in range(1, n):
                    edges.append((i-1, i, random.randint(1, 10 ** 9)))
            elif file == 10:
                n = 1000
                edges = []
                for i in range(1, n):
                    edges.append((0, i, random.randint(1, 10 ** 9)))
            else:
                n = random.randint(1, 1000)
                edges = []
                for i in range(1, n):
                    j = random.randint(0, i - 1)
                    edges.append((i, j, random.randint(1, 10 ** 9)))
            ans1 = standard_procedure(edges, n)
            ans2 = brute_force(edges, n)
            with open(f"test_data/example_{file}.in", "w", encoding="utf-8") as fw:
                lst = [f"{n}"]
                for ls in edges:
                    lst.append(" ".join(str(x) for x in ls))
                fw.write("\n".join(lst))
            with open(f"test_data/example_{file}.out", "w", encoding="utf-8") as fw:
                fw.write(str(ans1))
            assert ans1 == ans2

        for file in range(11, 21):

            if file == 19:
                n = 200000
                edges = []
                for i in range(1, n):
                    edges.append((i-1, i, random.randint(1, 10 ** 9)))
            elif file == 20:
                n = 200000
                edges = []
                for i in range(1, n):
                    edges.append((0, i, random.randint(1, 10 ** 9)))
            else:
                n = random.randint(200000 // (file - 10), 200000)
                edges = []
                for i in range(1, n):
                    j = random.randint(0, i - 1)
                    edges.append((i, j, random.randint(1, 10 ** 9)))

            ans1 = standard_procedure(edges, n)
            with open(f"test_data/example_{file}.in", "w", encoding="utf-8") as fw:
                lst = [f"{n}"]
                for ls in edges:
                    lst.append(" ".join(str(x) for x in ls))
                fw.write("\n".join(lst))
            with open(f"test_data/example_{file}.out", "w", encoding="utf-8") as fw:
                fw.write(str(ans1))

        zip_folder("test_data", "test_data.zip")
        return


if __name__ == '__main__':
    unittest.main()
