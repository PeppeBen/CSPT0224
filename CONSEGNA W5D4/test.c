#include <stdio.h>
#include <math.h>

int main ()
{
    double D;
/*
Input del numero
*/
    printf("Inserisci numero in D: ");
    scanf("%lf", &D);
/*
Calcolo area del quadrato
*/
    double squareArea= D * D;

/*
Calcolo area cerchio
*/
    double radius= D / 2;
    double circleArea= M_PI * (radius * radius);

/*
Calcolo area triangolo equilatero
*/
    double triangleArea= (sqrt(3) / 4) * D * D;

/*
Stampa dei risultati
*/

    printf("L'area del quadrato, avendo lato %lf: è %lf\n", D, squareArea);
    printf("L'area del cerchio, avendo raggio %lf: è %lf\n", D, radius, circleArea);
    printf("L'area del triangolo, avendo lato %lf: è %lf\n", D, triangleArea);

}