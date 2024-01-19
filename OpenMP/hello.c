#g++-13 -fopenmp foo.c
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
