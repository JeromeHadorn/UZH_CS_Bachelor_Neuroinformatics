### Merge Sort
Closely follows the divide-and-conquer paradigm
To sort an n-element sequence proceed as follows
* **Divide**: divide the sequence into two n/2-element sequences
* **Conquer**: sort the two sequences recursively using merge sort
* **Combine**: merge the two sorted sequences to produce the solution

Recursion stops when the sequence that must be sorted has length 1.


```c
void mergeSort(int A[], int l, int r){
    if (l < r){
        int m = floor((l+r)/2);
        mergeSort(A,l,m);
        mergeSort(A,m+1,r);
        merge(A,l,r,m);
    }
}

void merge(int A[], int l, int r, int m){
    int B[100];

    int bSize=0;
    // Copying left side in Auxiliary Array
    for (int i=l; i <= m;i++){
        B[i] = A[i];
        bSize++;
    }

    // Copying right side in Auxiliary Array REVERSED
    for (int i=m+1; i<r; i++){
        //reverse filling
        B[r+m-i+1] = A[i];
        bSize++;
    }

    int nA = sizeof(B)/sizeof(B[0]);
    int i=l;
    int j=r;

    for (int k=l; k<r;k++){
        if (B[i] < B[j]){
            A[k] = B[i];
            i=i+1;
        } else {
            A[k] = B[j];
            j=j-1;
        }
    }
    
}
```

**Time Complexity**: Sorting arrays on different machines. Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation.

**T(n) = 2T(n/2) + Theta(n)**

The above recurrence can be solved either using Recurrence Tree method or Master method. It falls in case II of Master Method and solution of the recurrence is **Theta(nLogn)**.

Time complexity of Merge Sort is **Theta(nLogn)** in all 3 cases (worst, average and best) as merge sort always divides the array into two halves and take linear time to merge two halves.

Auxiliary Space: **O(n)**

Algorithmic Paradigm: Divide and Conquer

Sorting In Place: No in a typical implementation