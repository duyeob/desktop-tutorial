import 'package:flutter/material.dart';
import 'first_page.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    print('MyApp build()');
    return MaterialApp(title: 'Flutter Lifecycle Demo', home: FirstPage());
  }
}
