# Quick Sort

### QuickSort

Like [Merge Sort](https://www.geeksforgeeks.org/merge-sort/), QuickSort is **a Divide and Conquer algorithm**. It picks an element as **pivot** and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways. 

1. Always pick first element as pivot.
2. Always pick last element as pivot (implemented below)
3. Pick a random element as pivot.
4. Pick median as pivot.

The key process in quickSort is **partition()**. Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.

* 피봇 설정을 잘하는 것이 핵심이다

#### 병합 정렬과의 차이점

* 단순하게 중앙을 기준으로 두 부분을 나누는 병합 저열과 달리, 기준 아이템(pivot item)을 중심으로 피봇보다 작은 것은 왼쪽에, 큰 것은 오른쪽에 위치 시킨다.
* 각 부분 정렬이 끝난 후 후처리 작업(병합)이 필요하지 않다.

<br/>

### Partition Algorithm





## Reference

[Quick sort Description](https://www.geeksforgeeks.org/quick-sort/)

[Quick sort fork dance](https://www.youtube.com/watch?v=3San3uKKHgg)