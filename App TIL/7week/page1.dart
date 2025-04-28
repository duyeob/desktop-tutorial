import 'package:flutter/material.dart';
import 'package:carousel_slider/carousel_slider.dart';

class Page1 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ListView(
      children: [
        TopSection(),
        SizedBox(height: 20),
        MiddleSection(),
        SizedBox(height: 20),
        BottomSection(),
      ],
    );
  }
}

// 상단 메뉴 (자동차 아이콘 + 글자)
class TopSection extends StatelessWidget {
  final List<String> menuLabels = ['택시', '블랙', '바이크', '대리', '택시', '블랙', '바이크'];

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(12.0),
      child: Wrap(
        spacing: 20,
        runSpacing: 20,
        children:
            menuLabels.map((label) {
              return Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Container(
                    width: 60,
                    height: 60,
                    decoration: BoxDecoration(
                      color: Colors.blue[100],
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: Icon(
                      Icons.directions_car, // 무조건 자동차 아이콘
                      size: 30,
                      color: Colors.black,
                    ),
                  ),
                  SizedBox(height: 5),
                  Text(label, style: TextStyle(fontSize: 12)),
                ],
              );
            }).toList(),
      ),
    );
  }
}

// 중단 슬라이드 광고
class MiddleSection extends StatelessWidget {
  final List<String> imageUrls = [
    'https://cdn.pixabay.com/photo/2018/11/12/18/44/thanksgiving-3811492_1280.jpg',
    'https://cdn.pixabay.com/photo/2019/10/30/15/33/tajikistan-4589831_1280.jpg',
    'https://cdn.pixabay.com/photo/2019/11/25/16/15/sfari-4652364_1280.jpg',
  ];

  @override
  Widget build(BuildContext context) {
    return CarouselSlider(
      options: CarouselOptions(
        height: 180,
        autoPlay: true,
        enlargeCenterPage: true,
      ),
      items:
          imageUrls.map((url) {
            return ClipRRect(
              borderRadius: BorderRadius.circular(12),
              child: Image.network(
                url,
                fit: BoxFit.cover,
                width: double.infinity,
              ),
            );
          }).toList(),
    );
  }
}

// 하단 공지사항
class BottomSection extends StatelessWidget {
  final List<String> notices = [
    '공지사항 1: 요요!',
    '공지사항 2: 점검 일정 안내',
    '공지사항 3: 새로운 기능 출시',
  ];

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children:
          notices.map((notice) {
            return ListTile(
              leading: Icon(Icons.notifications),
              title: Text(notice),
            );
          }).toList(),
    );
  }
}
