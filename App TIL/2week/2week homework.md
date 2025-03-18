● 실행해볼 코드
1. 구구단 출력
2. 여러 모형 출력
3. 날짜 출력

● 실행 코드
1. void main() {
  for (int i = 2; i <= 9; i++) {
    for (int j = 1; j <= 9; j++) {
      print("$i × $j = ${i * j}");
    }
    print(" ");
  }
}

2. 
void main() {
  int n = 10; // 정사각형 크기

  for (int i = 0; i < n; i++) {
    print('*' * n);
  }
  print("");
  for (int i = 0; i < n; i++) {
    if (i == 0 || i == n - 1) {
      print('*' * n);
    } else {
      print('*' + ' ' * (n - 2) + '*');
    }
  }
  print("");
  for (int i = 0; i < n; i++) {
    print(' ' * i + '/');
  }
  print("");
  for (int i = 0; i < n; i++) {
    print(' ' * (n - i - 1) + '\\');
  }
  print("");
  for (int i = 0; i < n; i++) {
    String line = "";
    for (int j = 0; j < n; j++) {
      if (i == j || j == n - i - 1) {
        line += '*';
      } else {
        line += ' ';
      }
    }
    print(line);
  }
}

3. void main() {
int year = 2002;
int month = 08;
int day = 31;

List weekdays = ["월", "화", "수", "목", "금", "토", "일"];

DateTime date = DateTime(year, month, day);

print("입력하신 날짜의 요일은 ${weekdays[date.weekday - 1]}요일입니다.");
}