#include <stdio.h>
int main () {
    int a = 5;
    
    int *pa= &a;
    printf("%d\n", a);
    *pa = 20;
    printf("%d\n", a);
    return 0;
}