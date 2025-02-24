#include <stdio.h>
int main () {
    int a = 10;
    // scanf("%d", &a, 10);
    int *pa= &a;
    printf("%p\n", &a);
    printf("%p\n", pa);
    return 0;
}