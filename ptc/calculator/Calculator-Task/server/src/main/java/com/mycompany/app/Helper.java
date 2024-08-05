package com.mycompany.app;

public class Helper {

    public static boolean isFirst(char op1, char op2) {

        if (op2 == '(' || op2 == ')') {
            return false;
        }
        if ((op1 == '*' || op1 == '/') && (op2 == '+' || op2 == '-')) {
            return false;
        } else {
            return true;
        }
    }

    public static boolean isDigit(char input) {
        return String.valueOf(input).matches("[0-9]+$");
    }

    public static boolean isDigitOrDot(char input) {
        return String.valueOf(input).matches("[0-9.,]*$");
    }
}