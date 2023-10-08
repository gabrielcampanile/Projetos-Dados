#include <stdio.h>
#include <string.h>

void erase(char[], int[]);
int quantidade(char[]);
int digito1(int[]);
int digito2(int[]);

int main()
{
    char cpf[20];
    int n[11];

    for(int i=0; i<11; i++)
        n[i]=0;

    printf("Digite seu cpf: ");
    fgets(cpf, sizeof(cpf), stdin);
    cpf[strlen(cpf) - 1] = '\0';
    
    erase(cpf, n);
    
    printf("%s\n%i\n", cpf, strlen(cpf));
    for(int i=0; i<strlen(cpf); i++)
        printf("%i", n[i]);
    printf("\n");

    if(!quantidade(cpf)){
        printf("CPF invalido.\n");
        return 0;
    }

    /*if (!digito1(n))
    {
        printf("CPF inválido.\n");
        return 0;
    }

    if (!digito2(n))
    {
        printf("CPF inválido.\n");
        return 0;
    }*/

    printf("CPF valido.\n");

    return 0;
}

void erase(char cpf[], int n[])
{
    for (int i = 0; i < strlen(cpf); i++)
    {
        if (cpf[i] == '.' || cpf[i] == '-' || cpf[i] == ' ')
        {
            cpf[i] = cpf[i + 1];
            cpf[strlen(cpf) - 1] = '\0';
        }
        n[i] = cpf[i];
    }
}

int quantidade(char cpf[])
{
    if(strlen(cpf)<11 || strlen(cpf)>11)
        return 0;
    return 1;
}

int digito1(int n[])
{
    int soma = 0, aux = 10;
    for (int i = 0; i < 9; i++)
    {
        soma += n[i] * aux;
        aux--;
    }
    soma = (soma * 10) % 11;
    if (soma == 10)
        soma == 0;
    if (soma == n[9])
        return 1;
    else
        return 0;
}

int digito2(int n[])
{
    int soma = 0, aux = 11;
    for (int i = 0; i < 10; i++)
    {
        soma += n[i] * aux;
        aux--;
    }
    soma = (soma * 10) % 11;
    if (soma == 10)
        soma == 0;
    if (soma == n[10])
        return 1;
    else
        return 0;
}