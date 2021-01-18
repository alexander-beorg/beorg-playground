class BubbleSort:
    def __init__(self, l: list):
        if isinstance(l, list):
            self.l = l
        else:
            raise ValueError

    @property
    def bubble_sort(self):
        last_item = len(self.l) - 1
        for z in range(0, last_item):
            for x in range(0, last_item - z):
                if self.l[x] > self.l[x + 1]:
                    self.l[x], self.l[x + 1] = self.l[x + 1], self.l[x]


class Binarysearch:
    item_list = [91, 92, 68, 70, 77, 79, 81, 90]
    find = 79

    @staticmethod
    def binary_search(item_list, item):
        first = 0
        last = len(item_list) - 1
        found = False
        ind = 0
        # item_list = sorted(item_list)
        while (first <= last and not found):
            mid = (first + last) // 2
            if item_list[mid] == item:
                found = True
                ind = mid
            else:
                if item < item_list[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
        return f"{found}, {item}, {ind}"


if __name__ == "__main__":
    bs = BubbleSort([10, 75, 43, 15, 25, -4, 27, 91, 92, 68, 70, 77, 79, 81, 90])
    # print(bs.l)
    bs.bubble_sort
    print(bs.l)

    # bb = Binarysearch()
    # print(bb.binary_search(bb.item_list, bb.find))

