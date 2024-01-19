//g++-13 -fopenmp foo.c
#include <omp.h>
#include <cstdio>

int main() {
    #pragma omp parallel
    {
        int ID=omp_get_thread_num();
        printf("Hello %d", ID);
        printf("World %d \n", ID);
    }
}
//OutPut is
/*
Hello 1World 1 
Hello 4World 4 
Hello 3World 3 
Hello 0World 0 
Hello 6World 6 
Hello 5World 5 
Hello 2World 2 
Hello 7World 7
*/
