import heapq


def test_heapsort():
    nums = [1, 5, 3, 4, 2]
    heap = []
    for n in nums:
        heapq.heappush(heap, n)

    ordered = [heapq.heappop(heap) for n in range(len(heap))]
    assert ordered == [1, 2, 3, 4, 5]


def test_heap_max():
    nums = [1, 5, 3, 4, 2]
    top3 = heapq.nlargest(3, nums)
    print(top3)


if __name__ == '__main__':
    # test_heapsort()
    test_heap_max()
