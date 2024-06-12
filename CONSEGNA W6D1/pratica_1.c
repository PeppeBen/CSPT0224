#include <stdio.h>
#include <stdlib.h>

void stampaMenu() {
    printf("\nBenvenuto al gioco Q&A:\n");
    printf("\nDovrai rispondere alle domande correttamente per ottenere punti.\n");
    printf("\nA- Nuova partita\n");
    printf("\nB- Esci dal gioco\n");
    printf("\nScegli un'opzione:\n");
}

void nuovaPartita() {
    char nome[10];
    int punteggio = 0;
    char risposta;

    printf("\nInserisci il tuo nome: ");
    scanf("\n%c", nome);

    printf("\nOk %c, iniziamo!\n", nome);

    printf("\nDomanda n.1: Qual'è la capitale d'Italia?\n");
    printf("A) Roma\nB) Milano\nC) Torino\n");
    printf("\nRisposta: ");
    scanf(" %c", &risposta);
    if (risposta == 'a' || risposta == 'A') {
        punteggio ++;
    }

    printf("\nDomanda n.2: Qual'è la capitale della Francia?\n");
    printf("A) Lille\nB) Parigi\nC) Lione\n");
    printf("\nRisposta: ");
    scanf(" %c", &risposta);
    if (risposta == 'b' || risposta == 'B') {
        punteggio ++;
    } 

    printf("\nDomanda n.3: Qual'è la capitale della Germania?\n");
    printf("A) Stoccarda\nB) Monaco\nC) Berlino\n");
    printf("\nRisposta: ");
    scanf(" %c", &risposta);
    if (risposta == 'c' || risposta == 'C') {
        punteggio ++;
    }

    printf("\nComplimenti %c, il tuo punteggio finale è: %d\n", nome, punteggio);
}


int main ()
{
    char scegli = '\0';

    while (scegli != 'b' && scegli != 'B')
    {
        stampaMenu();
        scanf(" %c", &scegli);

        switch(scegli) {
            case 'a':
            case 'A':
                printf("\nBene!\n");
                system ("clear");
                nuovaPartita();
                break;

            case 'b':
            case 'B':
                printf("\nArrivederci!\n");
                break;

            default:
                printf("\nScelta non valida, ritenta!\n");
                    
        }
      
    }
    
    return 0;

}