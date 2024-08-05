package com.mycompany.app;

import static com.mycompany.app.Helper.isDigit;
import static com.mycompany.app.Helper.isDigitOrDot;
import static com.mycompany.app.Helper.isFirst;

import java.util.Hashtable;
import java.util.Stack;

public class Calculator {

    Character currentOperator;
    static Hashtable<Character, Operator> calculateOperator = new Hashtable<>();
    Stack<Double> operands = new Stack<>();
    Stack<Character> operators = new Stack<>();

    static {
        calculateOperator.put('+', new Add());
        calculateOperator.put('-', new Subtraction());
        calculateOperator.put('*', new Multiplication());
        calculateOperator.put('/', new Division());
    }

    public double calculate(String input) {

        input = input.replace(" ", "");
        char[] inputArr = input.toCharArray();

        for (int i = 0; i < inputArr.length; i++) {
            if (isDigit(inputArr[i])) {
                i = pushOperand(i, inputArr);

            } else if (inputArr[i] == '(') {
                operators.push(inputArr[i]);

            } else if (inputArr[i] == ')') {
                solvingExerciseInBrackets();

            } else{
                emptyingOperatorStack(inputArr[i]);
            }
        }
        emptyingStacks();
        return operands.pop();
    }

    public int pushOperand(int index, char[] inputArr) {
        StringBuilder sb = new StringBuilder();
        while (index < inputArr.length && isDigitOrDot(inputArr[index])) {
            sb.append(inputArr[index++]);
        }
        operands.push(Double.parseDouble(sb.toString()));
        return index - 1;
    }

    public void solvingExerciseInBrackets() {
        while (operators.peek() != '(') {
            currentOperator = operators.pop();
            operands.push(calculateOperator.get(currentOperator).calc(operands.pop(), operands.pop()));
        }
        operators.pop();
    }

    public void emptyingOperatorStack(char input) {
        while (!operators.empty() && isFirst(input, operators.peek())) {
            currentOperator = operators.pop();
            operands.push(calculateOperator.get(currentOperator).calc(operands.pop(), operands.pop()));
        }
        operators.push(input);
    }

    public void emptyingStacks() {
        while (!operators.empty()) {
            currentOperator = operators.pop();
            operands.push(calculateOperator.get(currentOperator).calc(operands.pop(), operands.pop()));
        }
    }
}