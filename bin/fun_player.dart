import 'dart:ffi';
import 'dart:io';
import 'package:ffi/ffi.dart';
import 'package:win32/win32.dart';

void main(List<String> arguments) {
  // check if the input file arguments are provided
  if (arguments.isEmpty) {
    print('Usage: dart bin/fun_player.dart <filename>');
    return;
  }
  // check if the file exists
  final file = File(arguments.first);
  if (!File(arguments.first).existsSync()) {
    print('File not found: ${file.path}');
    return;
  }
  int result = mciSendString('play ${arguments.first} wait'.toNativeUtf16(),
      Pointer<Utf16>.fromAddress(0), 0, 0);
  print('Result: $result');
}
