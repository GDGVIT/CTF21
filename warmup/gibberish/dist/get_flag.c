#include <stdio.h>
#include <string.h>

int main() {
    char passwd[64];
    printf("Password: ");
    scanf("%s", passwd);
    if (strcmp(passwd, "goodbye") == 0) {
        printf("dsc{nc_c4n_4ls0_trnsmit_f1les}\n");
    } else {
        printf("Wrong password.\n");
    }
    return 0;
}
