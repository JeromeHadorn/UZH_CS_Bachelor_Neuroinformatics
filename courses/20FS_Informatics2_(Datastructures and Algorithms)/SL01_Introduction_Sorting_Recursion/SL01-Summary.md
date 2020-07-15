# Summary: SL01 Introduction, Sorting & Recursion
## Sort (basic)
The following Sorting algorithms are all O=n^2 
### Bubble Sort
Scans sequence and swaps unsorted adjacent elements. Repeats the sequence until the sequence is actually sorted.

Loop scans smaller and smaller sequence once the biggest elments start to accumalate at the end.
```c
void bubbleSort(int arr[], int n){
    for (int i = n; i > 1; i--){
        for (int j = 0; j < i; j++){
            if (arr[j]< arr[j-1]){
                int t = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = t;
            }
        }    
    }
}
```
### Selection Sort
Selects smallest element and swaps it with the 1st Element. Repeats the procedure on remaining unsorted sequence.

```c
void selectionSort(int n, int array[]){
    int k;
    for (int i = 0; i < n-1;i++){
        k = i;
        for (int j = i+1; j < n; j++){
            if (array[j] < array[k]){
                k = j;
            }
        }
        // Possible improvement only if i != k
        // exchange i and k element
        int t = array[i];
        array[i] = array[k];
        array[k] = t;
    }
}
```
### Insertion Sort
Take first element and consider it as (sorted) sequence. Continue taking elements and inserting into right place.

Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.

```c
void insertionSort(int n, int array[]){
    for (int i = 1; i < n; i++){
        
        int j = i -1;
        int value = array[i];

        while (j >= 0 && array[j] > value){
            array[j +1] = array[j];
            j = j - 1;
        }
        array[j+1]= value;
    }
}
```
## Recursion
**Recursive object**
* It contains itself as part of it
* It is defined in terms of itself

**Recursive procedure**
* Procedure that calls itself
* Multiple & mutual recursive calls
* Termination condition to stop recursion
### Sierpinski Triangles
Recursive algorithm drawing Sierpinski Triangle of depth d.

```c
void Sierpinski(int x, int y, int h, int d){
    if (d > 0){
        drawTriangle(x-h/2, y);
        drawTriangle(x+h/2, y);
        drawTriangle(x, y+h);
    }
    // Draw three subtriangles
    Sierpinski(x-h/2, y + h/2, h/2, d--); // Left Triangle
    Sierpinski(x+h/2, y + h/2, h/2, d--); // Right Triagle
    Sierpinski(x, y-h, h/2, d--) // Bottom Triangle
}
```
### Hilbert Curve
n/a
### Sierpinski Curve
n/a