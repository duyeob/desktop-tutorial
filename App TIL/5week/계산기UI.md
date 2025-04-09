import 'package:flutter/material.dart';

void main() => runApp(Calculator());

class Calculator extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.blue.shade100,
        body: Center(
          child: Container(
            width: 360,
            height: 640,
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(16),
              boxShadow: [
                BoxShadow(
                  color: Colors.grey.shade400,
                  blurRadius: 10,
                  offset: Offset(0, 4),
                ),
              ],
            ),
            child: Column(
              children: [
                Container(
                  height: 120,
                  alignment: Alignment.bottomRight,
                  padding: EdgeInsets.all(20),
                  child: Text(
                    '0',
                    style: TextStyle(color: Colors.black87, fontSize: 48),
                  ),
                
                ),
                Expanded(
                  child: Padding(
                    padding: EdgeInsets.all(8),
                    child: GridView.count(
                      crossAxisCount: 4,
                      physics: NeverScrollableScrollPhysics(),
                      childAspectRatio: 1.1,
                      mainAxisSpacing: 8,
                      crossAxisSpacing: 8,
                      children: [
                        for (var label in [
                          '%', 'CE', 'C', '⌫',
                          '⅟x', 'x²', '√x', '÷',
                          '7', '8', '9', '×',
                          '4', '5', '6', '−',
                          '1', '2', '3', '+',
                          '+/-', '0', '.', '='
                        ])
                          Container(
                            decoration: BoxDecoration(
                              color: getButtonColor(label),
                              borderRadius: BorderRadius.circular(8),
                            ),
                            alignment: Alignment.center,
                            child: Text(
                              label,
                              style: TextStyle(
                                color: Colors.black87,
                                fontSize: 22,
                              ),
                            ),
                          ),
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Color getButtonColor(String label) {
    const numberButtons = [
      '7', '8', '9',
      '4', '5', '6',
      '1', '2', '3',
      '+/-', '0', '.'
    ];

    if (label == '=') {
      return Colors.blueAccent.shade100;
    } else if (numberButtons.contains(label)) {
      return Colors.grey.shade200;
    } else {
      return Colors.grey.shade300;
    }
  }
}
