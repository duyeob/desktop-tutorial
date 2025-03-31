import 'dart:async'; // Timer 클래스를 사용하기 위해 가져옴
import 'package:flutter/material.dart'; // Flutter UI 라이브러리

void main() {
runApp(MyApp()); // 애플리케이션 시작
}

class MyApp extends StatelessWidget {
@override
Widget build(BuildContext context) {
return MaterialApp(
debugShowCheckedModeBanner: false, // 디버그 배너 숨기기
home: CurrentTimeScreen(), // 기본 화면 설정
);
}
}

class CurrentTimeScreen extends StatefulWidget {
@override
_CurrentTimeScreenState createState() => _CurrentTimeScreenState(); // 상태 관리 클래스 생성
}

class _CurrentTimeScreenState extends State<CurrentTimeScreen> {
String _currentTime = ""; // 현재 시각을 저장할 변수
late Timer _timer; // 주기적으로 시간 업데이트를 위한 Timer

@override
void initState() {
super.initState();
_updateTime(); // 초기 현재 시간을 설정
// 1초 간격으로 시간 업데이트
_timer = Timer.periodic(Duration(seconds: 1), (Timer t) => _updateTime());
}

void _updateTime() {
setState(() {
// 현재 시각을 문자열 형태로 저장
DateTime now = DateTime.now();
_currentTime =
"${now.year}-${now.month.toString().padLeft(2, '0')}-${now.day.toString().padLeft(2, '0')}\n" // 날짜 (연-월-일)
"${now.hour.toString().padLeft(2, '0')}:${now.minute.toString().padLeft(2, '0')}:${now.second.toString().padLeft(2, '0')}"; // 시간 (시:분:초)
});
}

@override
void dispose() {
_timer.cancel(); // Timer 해제하여 리소스 누수 방지
super.dispose();
}

@override
Widget build(BuildContext context) {
return Scaffold(
appBar: AppBar(
title: Text("현재 시각"), // 앱바 제목 설정
centerTitle: true, // 제목을 중앙 정렬
),
body: Center(
// 중앙에 시간 텍스트 배치
child: Text(
_currentTime, // 업데이트된 시간 표시
style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold), // 텍스트 스타일 설정
textAlign: TextAlign.center, // 텍스트를 중앙 정렬
),
),
);
}
}