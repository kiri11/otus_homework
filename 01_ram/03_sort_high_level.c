// Сортировка, версия на языке высокого уровня

r1 = read(); // количество элементов

// input
for (i = 0; i < r1-1; ++i){
    read(arr[i]);
}

// sort
for (i = r1; i > 0; --i) {
    for (k = r1; k > i; --k){
        if (arr[i] > arr[k]) {
            arr[i] <=> arr[k];
        }
    }
}

// output
for (i = 0; i < r1-1; ++i){
    write(arr[i]);
}
