package com.liudonghua.examples;

import com.sun.jna.Library;
import com.sun.jna.Native;

public class App {

    public interface Winmm extends Library {
        public int mciSendStringA(String lpszCommand, String lpszReturnString, int cchReturn, int hwndCallback);
    }

    public static void main(String[] args) {
        Winmm winmm = (Winmm) Native.load("winmm", Winmm.class);
        System.out.println(winmm.mciSendStringA("play mario.mid wait", null, 0, 0));
    }
}
