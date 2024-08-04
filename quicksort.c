#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// クイックソートの実装
int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;

    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// 計算時間を測定して表示する関数
void measureAndPrintTime(int arr[], int n, const char *label) {
    clock_t start, end;
    start = clock();
    quickSort(arr, 0, n - 1);
    end = clock();
    printf("Sorted array (%s): ", label);
    // プリントはサイズが大きい場合に見づらいため省略
    // printArray(arr, n);
    printf("Time taken for %s: %f seconds\n", label, ((double)(end - start)) / CLOCKS_PER_SEC);
}

int main() {
    // サイズが異なる3つの配列を用意
    int arr1[1000], arr2[10000], arr3[100000];

    // 各配列にランダムな値をセット
    for (int i = 0; i < 1000; i++) {
        arr1[i] = rand() % 100;
    }

    for (int i = 0; i < 10000; i++) {
        arr2[i] = rand() % 100;
    }

    for (int i = 0; i < 100000; i++) {
        arr3[i] = rand() % 100;
    }

    // 各配列の計算時間を測定して表示
    measureAndPrintTime(arr1, 1000, "n=1000");
    measureAndPrintTime(arr2, 10000, "n=10000");
    measureAndPrintTime(arr3, 100000, "n=100000");

    return 0;
}
