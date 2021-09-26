#include<stdio.h>

char * decrypt(char * enc){
	return "Pay first then I will fix this for you\n";
}

int main() {
	char secret_code[] = "ZHNje3BVMjJMM19QaTNjMzJ9";
	char * decrypted_code = decrypt(&secret_code);
	puts(decrypted_code);
}
