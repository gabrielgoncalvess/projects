import 'package:flutter/cupertino.dart';

class AppController extends ChangeNotifier {
  static AppController instance = AppController();

  bool isDartTheme = false;
  changeTheme() {
    isDartTheme = !isDartTheme; // ! para fazer o contrario do bool
    notifyListeners();
  }
}
