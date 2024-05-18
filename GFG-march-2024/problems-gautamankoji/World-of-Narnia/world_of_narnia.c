#include <stdio.h>

int leap(int year) {
	return (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0));
}

int days(int month, int year) {
	int d[] = {31, 28 + leap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	return d[month - 1];
}

int main(){
	int t;
	scanf("%d", &t);
	while(t--) {
		int day, month, year;
		scanf("%d %d %d",  &day, &month, &year);
		int res = day;
		for (int i = 1; i < month; i++) {
			res += days(i, year);
		}
		printf("%d\n", res);
	}

}
