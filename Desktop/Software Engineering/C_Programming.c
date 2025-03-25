#include <stdio.h>
/* Python function example */
int add_one(int num) {
    int ans = num + 1 ;
    return ans;
}

int main() {
    int num = 5;
    printf("Number + 1 = %d\n", add_one(num));
    return 0;
}