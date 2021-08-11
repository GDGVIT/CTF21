#include<stdio.h>
#include<string.h>

void get_record() {
	char record[128] = "";
	printf("Memory location:%llx\n",record);
	printf("Enter record:\n");
	fflush(stdout);
	fflush(stdin);
	gets(record);
}

int main(int argc,char **argv) {
	get_record();
}
