## Quicksort
#### Rough Idea
* Quicksort is a divide-and-conquer algorithm
    * Divide: partition array into two subarrays such that the items in the lower part <= the items in the upper part
    * Conquer: recursively sort the two subarrays
    * Combine: trivial since sorting is in place


```c
#include <stdio.h>

void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

void QuickSort(int A[], int n, int l, int r)
{
    if (l < r)
    {
        int m = LomutoPartition(A, n, l, r) || HoarePartition(A, n, l, r);
        QuickSort(A, n, l, m - 1); // smallest Elements
        QuickSort(A, n, m + 1, r)  // largest Elements

        // Important no Merge needed at the end
    }
}

int LomutoPartition(int A[], int n, int l, int r)
{
    // pivot (Element to be placed at right position)
    int pivot = A[r]; // middle element (pivot) (we take rightmost element as middle element)
    int i = l - 1;
    for (int j = l; j < r - 1; j++) { // elements l..r-1 are inserted into either the smaller or larger part
         
         // If current element is smaller than the pivot
        if (A[j] < pivot)
        {
            i = i + 1; // increment index of smaller element
            swap(A[i], A[j]);
        }
    }
    swap(A[i + 1], A[r]);
    return i + 1;
}

int HoarePartition(int A[], int n, int l, int r)
{
    int p = A[(l + r) / 2];
	int i = l - 1;
	int j = r + 1;
	while (true) {
		do {
			i++; // searches in the left part for a wrong (too large) element
		} while (A[i] < p);
		
        do {
			j--; // searches in the right part for a wrong (too small) element
		} while (A[j] > p);
		
        if (i >= j) {
            return j;
        } else {
		    swap(&A[i], &A[j]); // Swap of "wrong" elements
        }
            
	}
}

int main()
{
    int A = {7,8,2,6,5,1,3};
    
}
```


**Performance**
Worst Case
* Occurs when the array is already completely sorted
* Partitioning produces one subproblem with $n − 1$ items and one with 0 elements
* If such a partitioning arises at each recursive call then $T (n) = T (n − 1) + T (0) + Θ(n) = T (n − 1) + Θ(n)$
where $Θ(n)$ is the cost of partitioning the array
* Sum of the costs incurred at each level of the recursion yields an arithmetic series (i.e., $\sum_{i=0}^{n}i$)
* It thus follows that, in the worst case, $T(n) = Θ(n^{2})$

Best Case
* Partitioning produces two subproblems of size $n/2$
* If such a partitioning arises at each recursive call then
$T (n) = 2T (n/2) + Θ(n)$
* It thus follows that, in the best case, $T (n) = Θ(n lg n)$

Average case
* Actually much closer to best case than to worst case
* Quick sort’s behavior is determined by the ordering of the array elements
* In average, there is a mix of “good” and “bad” splits
* Underlying assumption: all permutations of the input numbers are equally likely
* Randomized algorithm: partition around random item (instead of last item)
    * Running time is independent of input ordering
    * No specific input triggers worst case behavior
    * Worst case determined only by output of the random-number generator
* Randomization is a general tool to improve algorithms with bad worst-case but good average-case complexity

https://www.geeksforgeeks.org/quick-sort/