#include <stdio.h>
#include <math.h>

int main ()
{
    double d;
/*
Input del numero
*/
    printf("Inserisci numero in D: ");
    scanf("%lf", &d);
/*
Calcolo area del quadrato
*/
    double squareArea= d * d;

/*
Calcolo area cerchio
*/
    double radius= d / 2;
    double circleArea= M_PI * (radius * radius);

/*
Calcolo area triangolo equilatero
*/
    double triangleArea= (sqrt(3) / 4) * d * d;

/*
Stampa dei risultati
*/

    printf("L'area del quadrato, avendo lato %lf: è %lf\n", d, squareArea);
    printf("L'area del cerchio, avendo raggio %lf: è %lf\n", d, radius, circleArea);
    printf("L'area del triangolo, avendo lato %lf: è %lf\n", d, triangleArea);

}