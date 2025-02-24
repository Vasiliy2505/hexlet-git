#include <stdio.h>
    void change_value_to_0(int *ptr){ *ptr = 0; } 
    int main() {
    int a = 21;
    printf("%d\n", a);
    int *pa= &a; 
    change_value_to_0(pa);
    printf("%d\n", a);    

    return 0;
}